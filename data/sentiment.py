"""
Sentiment Analysis Module
Detects market sentiment from CMC data signals
"""

def analyze_sentiment(global_metrics: dict, token_data: dict) -> dict:
    """
    Analyze sentiment from available market data.
    Returns sentiment score -100 (extreme fear) to +100 (extreme greed)
    """
    score = 0
    signals = []

    # --- Market Cap Change Signal ---
    mcap_change = global_metrics.get("total_market_cap_yesterday_percentage_change", 0)
    if mcap_change > 5:
        score += 25
        signals.append(f"🟢 Market cap surging +{mcap_change:.1f}% — Greed building")
    elif mcap_change > 2:
        score += 12
        signals.append(f"🟡 Market cap growing +{mcap_change:.1f}% — Mild optimism")
    elif mcap_change < -5:
        score -= 25
        signals.append(f"🔴 Market cap crashing {mcap_change:.1f}% — Fear spreading")
    elif mcap_change < -2:
        score -= 12
        signals.append(f"🟠 Market cap declining {mcap_change:.1f}% — Caution zone")
    else:
        signals.append(f"⚪ Market cap stable — Neutral sentiment")

    # --- BTC Dominance Signal ---
    btc_dom = global_metrics.get("btc_dominance", 50)
    if btc_dom > 60:
        score -= 15
        signals.append(f"🔴 BTC dominance HIGH ({btc_dom:.1f}%) — Altcoins bleeding, risk-off")
    elif btc_dom < 40:
        score += 15
        signals.append(f"🟢 BTC dominance LOW ({btc_dom:.1f}%) — Altseason possible")
    else:
        signals.append(f"⚪ BTC dominance neutral ({btc_dom:.1f}%)")

    # --- Token Price Momentum ---
    p1h = token_data.get("percent_change_1h", 0)
    p24h = token_data.get("percent_change_24h", 0)

    if p1h > 3 and p24h > 10:
        score += 20
        signals.append(f"🟢 Strong momentum: +{p1h:.1f}% (1h), +{p24h:.1f}% (24h) — Buyers in control")
    elif p1h > 1 and p24h > 3:
        score += 10
        signals.append(f"🟡 Mild momentum: +{p1h:.1f}% (1h), +{p24h:.1f}% (24h)")
    elif p1h < -3 and p24h < -8:
        score -= 20
        signals.append(f"🔴 Selling pressure: {p1h:.1f}% (1h), {p24h:.1f}% (24h) — Bears winning")
    elif p1h < -1:
        score -= 10
        signals.append(f"🟠 Slight weakness: {p1h:.1f}% (1h)")

    # --- Volume Analysis ---
    vol_change = token_data.get("volume_change_24h", 0)
    if vol_change > 50:
        score += 15
        signals.append(f"🟢 Volume exploding +{vol_change:.0f}% — Smart money moving")
    elif vol_change > 20:
        score += 8
        signals.append(f"🟡 Volume increasing +{vol_change:.0f}% — Interest growing")
    elif vol_change < -50:
        score -= 15
        signals.append(f"🔴 Volume dying {vol_change:.0f}% — Liquidity leaving")
    elif vol_change < -20:
        score -= 8
        signals.append(f"🟠 Volume declining {vol_change:.0f}% — Weak conviction")

    # Clamp score
    score = max(-100, min(100, score))

    # Label
    if score >= 60:
        label = "EXTREME GREED 🤑"
    elif score >= 30:
        label = "GREED 😏"
    elif score >= 10:
        label = "MILD GREED 🙂"
    elif score > -10:
        label = "NEUTRAL 😐"
    elif score > -30:
        label = "MILD FEAR 😟"
    elif score > -60:
        label = "FEAR 😨"
    else:
        label = "EXTREME FEAR 😱"

    return {
        "score": score,
        "label": label,
        "signals": signals
    }
