"""
Whale / Market Maker Trap Detector
Identifies manipulation patterns before retail gets trapped
"""

def detect_whale_trap(token_data: dict, listings: list) -> dict:
    """
    Detect Market Maker manipulation signals.
    
    Patterns detected:
    1. Fake pump — price up but volume suspicious
    2. Stop hunt — price dip below support then reversal
    3. Liquidity sweep — rapid spike then dump
    4. Accumulation — quiet buying with suppressed price
    """
    traps = []
    trap_score = 0  # 0 = clean, 100 = heavy manipulation

    price = token_data.get("price", 0)
    p1h = token_data.get("percent_change_1h", 0)
    p24h = token_data.get("percent_change_24h", 0)
    p7d = token_data.get("percent_change_7d", 0)
    vol_change = token_data.get("volume_change_24h", 0)
    vol_24h = token_data.get("volume_24h", 0)
    mcap = token_data.get("market_cap", 1)

    # --- Pattern 1: Fake Pump Detection ---
    # Price pumping hard but volume not proportional
    if p1h > 5 and vol_change < 10:
        trap_score += 35
        traps.append({
            "type": "FAKE PUMP ⚠️",
            "detail": f"Price +{p1h:.1f}% in 1h but volume only +{vol_change:.0f}% — No real buyers!",
            "action": "AVOID LONG — Dump incoming"
        })

    # --- Pattern 2: Stop Hunt Setup ---
    # Price dropped recently then recovering fast = stops were hunted
    if p1h > 3 and p24h < -5:
        trap_score += 30
        traps.append({
            "type": "STOP HUNT DETECTED 🎯",
            "detail": f"24h down {p24h:.1f}% then 1h recovery +{p1h:.1f}% — MM swept stops below",
            "action": "POTENTIAL LONG after confirmation"
        })

    # --- Pattern 3: Liquidity Sweep ---
    # Massive volume spike with price reversal
    if vol_change > 100 and abs(p1h) > 5:
        trap_score += 40
        traps.append({
            "type": "LIQUIDITY SWEEP 🌊",
            "detail": f"Volume +{vol_change:.0f}% with {p1h:.1f}% price move — MM taking liquidity",
            "action": "Wait for direction confirmation — High volatility zone"
        })

    # --- Pattern 4: Quiet Accumulation ---
    # Price stable but volume slowly increasing = smart money buying
    if abs(p1h) < 1 and abs(p24h) < 3 and vol_change > 30:
        trap_score -= 20  # Actually BULLISH signal
        traps.append({
            "type": "ACCUMULATION DETECTED 🐋",
            "detail": f"Price flat ({p24h:.1f}% 24h) but volume +{vol_change:.0f}% — Smart money loading",
            "action": "POTENTIAL LONG — Watch for breakout"
        })

    # --- Pattern 5: Distribution ---
    # Price still high but volume declining = insiders selling into strength
    if p7d > 20 and p24h > 5 and vol_change < -30:
        trap_score += 45
        traps.append({
            "type": "DISTRIBUTION ZONE 📤",
            "detail": f"Up {p7d:.1f}% this week, volume dropping {vol_change:.0f}% — Insiders exiting",
            "action": "DO NOT BUY — Take profits if holding"
        })

    # --- Pattern 6: Volume/MCap ratio anomaly ---
    vol_mcap_ratio = (vol_24h / mcap) if mcap > 0 else 0
    if vol_mcap_ratio > 0.5:
        trap_score += 25
        traps.append({
            "type": "WASH TRADING ALERT 🚨",
            "detail": f"Volume is {vol_mcap_ratio:.1%} of market cap — Abnormally high, possible fake volume",
            "action": "Be very cautious — Volume may not be real"
        })

    trap_score = max(0, min(100, trap_score))

    if trap_score >= 70:
        overall = "HEAVY MANIPULATION 🚨"
    elif trap_score >= 40:
        overall = "SUSPICIOUS ACTIVITY ⚠️"
    elif trap_score >= 20:
        overall = "MILD SIGNALS 🟡"
    else:
        overall = "CLEAN MARKET ✅"

    return {
        "trap_score": trap_score,
        "overall": overall,
        "patterns": traps,
        "count": len(traps)
    }
