"""
Entry / Exit Strategy Generator
Combines all signals into actionable trade recommendations
"""

def generate_signal(token_data: dict, regime: dict, whale_trap: dict, psychology: dict, sentiment: dict) -> dict:
    """
    Generate final BUY / SELL / HOLD signal with entry, SL, TP
    """
    price = token_data.get("price", 0)
    regime_type = regime.get("regime", "SIDEWAYS")
    trap_score = whale_trap.get("trap_score", 0)
    psych_score = psychology.get("psychology_score", 0)
    sentiment_score = sentiment.get("score", 0)

    # --- Signal Logic ---
    signal = "HOLD"
    confidence = 0
    reasons = []

    # Chaos = always stay out
    if regime_type == "CHAOS":
        return {
            "signal": "STAY OUT",
            "confidence": 95,
            "entry": None,
            "stop_loss": None,
            "take_profit_1": None,
            "take_profit_2": None,
            "take_profit_3": None,
            "reasons": ["🔴 Market in CHAOS regime — No trade"],
            "risk_level": "EXTREME"
        }

    # Heavy manipulation = avoid
    if trap_score >= 70:
        return {
            "signal": "AVOID",
            "confidence": 85,
            "entry": None,
            "stop_loss": None,
            "take_profit_1": None,
            "take_profit_2": None,
            "take_profit_3": None,
            "reasons": ["🚨 Heavy market manipulation detected — MM trap active"],
            "risk_level": "HIGH"
        }

    # LONG signal conditions
    long_score = 0
    short_score = 0

    if regime_type == "BULL":
        long_score += 30
        reasons.append("✅ Bull regime confirmed")

    if regime_type == "BEAR":
        short_score += 30
        reasons.append("⚠️ Bear regime — Short bias")

    if psych_score < -60:  # Extreme fear = buy opportunity
        long_score += 25
        reasons.append("✅ Extreme fear = contrarian BUY signal")

    if psych_score > 70:  # Extreme greed = sell opportunity
        short_score += 25
        reasons.append("⚠️ Extreme greed = SELL signal")

    if sentiment_score > 30 and trap_score < 30:
        long_score += 15
        reasons.append("✅ Positive sentiment with clean market")

    if sentiment_score < -30 and trap_score < 30:
        short_score += 15

    if trap_score < 20:
        long_score += 10
        reasons.append("✅ No manipulation detected")
    elif trap_score > 40:
        long_score -= 20
        reasons.append("⚠️ Manipulation risk reduces confidence")

    # Determine final signal
    if long_score >= 50:
        signal = "BUY 🟢"
        confidence = min(90, long_score)
        risk_level = "LOW" if confidence > 70 else "MEDIUM"

        # Calculate levels
        entry = price
        stop_loss = round(price * 0.95, 6)      # 5% SL
        take_profit_1 = round(price * 1.05, 6)  # 5% TP1
        take_profit_2 = round(price * 1.12, 6)  # 12% TP2
        take_profit_3 = round(price * 1.20, 6)  # 20% TP3

    elif short_score >= 50:
        signal = "SELL/SHORT 🔴"
        confidence = min(90, short_score)
        risk_level = "MEDIUM"

        entry = price
        stop_loss = round(price * 1.05, 6)       # 5% above for shorts
        take_profit_1 = round(price * 0.95, 6)   # 5% down
        take_profit_2 = round(price * 0.88, 6)   # 12% down
        take_profit_3 = round(price * 0.80, 6)   # 20% down

    else:
        signal = "HOLD / WAIT ⚪"
        confidence = 50
        risk_level = "LOW"
        entry = None
        stop_loss = None
        take_profit_1 = None
        take_profit_2 = None
        take_profit_3 = None
        reasons.append("⚪ No clear edge — Wait for better setup")

    return {
        "signal": signal,
        "confidence": confidence,
        "entry": entry,
        "stop_loss": stop_loss,
        "take_profit_1": take_profit_1,
        "take_profit_2": take_profit_2,
        "take_profit_3": take_profit_3,
        "reasons": reasons,
        "risk_level": risk_level
    }
