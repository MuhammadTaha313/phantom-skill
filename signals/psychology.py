"""
Human Psychology Detector
Identifies FOMO zones, Fear dumps, and crowd behavior patterns
"""

def detect_psychology_zones(token_data: dict, sentiment: dict) -> dict:
    """
    Detect crowd psychology states:
    - FOMO Zone: Retail rushing in at tops
    - Fear Dump: Panic selling at bottoms  
    - Greed Trap: Everyone bullish = top signal
    - Capitulation: Everyone bearish = bottom signal
    - Disbelief Rally: Price going up but no one believes it
    """
    zones = []
    psychology_score = 0  # Positive = retail FOMO, Negative = retail FEAR

    p1h = token_data.get("percent_change_1h", 0)
    p24h = token_data.get("percent_change_24h", 0)
    p7d = token_data.get("percent_change_7d", 0)
    vol_change = token_data.get("volume_change_24h", 0)
    sentiment_score = sentiment.get("score", 0)
    sentiment_label = sentiment.get("label", "NEUTRAL")

    # --- FOMO Zone ---
    # Price pumping hard, volume surging, sentiment euphoric
    if p7d > 30 and p24h > 8 and sentiment_score > 50:
        psychology_score = 90
        zones.append({
            "zone": "🚨 FOMO ZONE — DANGER",
            "detail": f"Up {p7d:.0f}% this week + {p24h:.0f}% today + Extreme greed = Classic retail top",
            "psychology": "Retail traders seeing green candles and rushing in",
            "smart_money": "Smart money SELLING into this FOMO",
            "action": "AVOID LONG — This is where MM distributes to retail",
            "risk": "HIGH"
        })

    # --- Fear Dump Zone ---
    # Price dumping, volume spiking, panic selling
    elif p7d < -25 and p24h < -8 and sentiment_score < -40:
        psychology_score = -90
        zones.append({
            "zone": "🔥 FEAR DUMP ZONE — OPPORTUNITY?",
            "detail": f"Down {abs(p7d):.0f}% this week + {abs(p24h):.0f}% today + Extreme Fear",
            "psychology": "Retail panic selling, weak hands exiting",
            "smart_money": "Smart money ACCUMULATING during this fear",
            "action": "WATCH for reversal signals — Potential bottom",
            "risk": "MEDIUM (contrarian)"
        })

    # --- Greed Trap ---
    elif sentiment_score > 70 and p24h > 5:
        psychology_score = 75
        zones.append({
            "zone": "⚠️ GREED TRAP",
            "detail": "Everyone is euphoric — Classic sign of market top approaching",
            "psychology": "When everyone is bullish, there are no buyers left",
            "smart_money": "Insiders taking profits quietly",
            "action": "REDUCE positions, set tight stop losses",
            "risk": "HIGH"
        })

    # --- Capitulation ---
    elif sentiment_score < -70 and p24h < -5:
        psychology_score = -75
        zones.append({
            "zone": "💎 CAPITULATION ZONE",
            "detail": "Everyone giving up — Historic bottoms form here",
            "psychology": "Last weak hands selling, smart money absorbing",
            "smart_money": "Accumulation phase beginning",
            "action": "DCA entry possible — High reward/risk",
            "risk": "LOW-MEDIUM (long term)"
        })

    # --- Disbelief Rally ---
    elif p7d > 15 and sentiment_score < 0:
        psychology_score = 40
        zones.append({
            "zone": "📈 DISBELIEF RALLY",
            "detail": "Price going up but sentiment still negative — Most miss this move",
            "psychology": "People don't believe the rally, staying on sidelines",
            "smart_money": "Early movers already positioned",
            "action": "MOMENTUM LONG — Pull-backs are buy opportunities",
            "risk": "MEDIUM"
        })

    # --- Normal Zone ---
    else:
        psychology_score = sentiment_score // 2
        zones.append({
            "zone": "⚪ NORMAL MARKET CONDITIONS",
            "detail": f"No extreme psychology detected. Sentiment: {sentiment_label}",
            "psychology": "Mixed signals, no crowd extreme",
            "smart_money": "Waiting for clearer setup",
            "action": "WAIT for better entry or trade with small size",
            "risk": "LOW-MEDIUM"
        })

    return {
        "psychology_score": psychology_score,
        "zones": zones,
        "crowd_state": _get_crowd_state(psychology_score)
    }

def _get_crowd_state(score: int) -> str:
    if score >= 80:
        return "EUPHORIA — Everyone bullish, sell signal"
    elif score >= 50:
        return "GREED — Caution, tops forming"
    elif score >= 20:
        return "OPTIMISM — Healthy uptrend"
    elif score >= -20:
        return "NEUTRAL — No clear bias"
    elif score >= -50:
        return "ANXIETY — Weakness showing"
    elif score >= -80:
        return "FEAR — Selling pressure"
    else:
        return "PANIC — Capitulation, potential bottom"
