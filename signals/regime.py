"""
Market Regime Detector
Identifies Bull / Bear / Sideways / Chaos regime
"""

def detect_regime(token_data: dict, global_metrics: dict, sentiment: dict) -> dict:
    """
    Detect current market regime.
    Regime determines which strategy to apply.
    """
    p1h = token_data.get("percent_change_1h", 0)
    p24h = token_data.get("percent_change_24h", 0)
    p7d = token_data.get("percent_change_7d", 0)
    vol_change = token_data.get("volume_change_24h", 0)
    btc_dom = global_metrics.get("btc_dominance", 50)
    mcap_change = global_metrics.get("total_market_cap_yesterday_percentage_change", 0)
    sentiment_score = sentiment.get("score", 0)

    bull_points = 0
    bear_points = 0
    chaos_points = 0

    # Price trend scoring
    if p7d > 20: bull_points += 3
    elif p7d > 8: bull_points += 2
    elif p7d > 2: bull_points += 1
    elif p7d < -20: bear_points += 3
    elif p7d < -8: bear_points += 2
    elif p7d < -2: bear_points += 1

    if p24h > 5: bull_points += 2
    elif p24h > 2: bull_points += 1
    elif p24h < -5: bear_points += 2
    elif p24h < -2: bear_points += 1

    if p1h > 2: bull_points += 1
    elif p1h < -2: bear_points += 1

    # Volume scoring
    if vol_change > 40 and p24h > 0: bull_points += 2
    elif vol_change > 40 and p24h < 0: bear_points += 2
    elif vol_change < -30: chaos_points += 1

    # Sentiment scoring
    if sentiment_score > 40: bull_points += 2
    elif sentiment_score < -40: bear_points += 2

    # Market cap scoring
    if mcap_change > 3: bull_points += 1
    elif mcap_change < -3: bear_points += 1

    # Chaos detection
    if abs(p1h) > 8: chaos_points += 3
    if abs(p24h - p7d/7) > 10: chaos_points += 2

    # Determine regime
    total = bull_points + bear_points + chaos_points

    if chaos_points >= 4:
        regime = "CHAOS"
        color = "🔴"
        strategy = "STAY OUT — Unpredictable, MM playing games"
        confidence = min(95, chaos_points * 15)
    elif bull_points > bear_points * 1.5:
        regime = "BULL"
        color = "🟢"
        strategy = "LONG BIAS — Buy dips, ride momentum"
        confidence = min(95, int((bull_points / max(total, 1)) * 100))
    elif bear_points > bull_points * 1.5:
        regime = "BEAR"
        color = "🔴"
        strategy = "SHORT BIAS — Sell rallies, avoid catching knives"
        confidence = min(95, int((bear_points / max(total, 1)) * 100))
    elif abs(bull_points - bear_points) <= 2:
        regime = "SIDEWAYS"
        color = "🟡"
        strategy = "RANGE TRADE — Buy support, sell resistance"
        confidence = 60
    else:
        regime = "TRANSITION"
        color = "🟠"
        strategy = "WAIT — Regime changing, risky to trade"
        confidence = 45

    return {
        "regime": regime,
        "color": color,
        "strategy": strategy,
        "confidence": confidence,
        "bull_points": bull_points,
        "bear_points": bear_points,
        "chaos_points": chaos_points,
        "btc_dominance": btc_dom
    }
