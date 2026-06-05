# 👻 PHANTOM — Market Maker Trap Detector

> **BNB Hack 2026 | Track 2: Strategy Skills**  
> Powered by CoinMarketCap AI Agent Hub

---

## 🎯 What is PHANTOM?

PHANTOM is a crypto trading strategy skill that detects **Market Maker manipulation patterns** before retail traders get trapped.

While everyone else is reacting to price moves, PHANTOM reads *why* the price is moving — and whether a whale is setting up a trap.

---

## 🧠 How It Works

PHANTOM runs **5 analysis layers simultaneously**:

```
CMC Live Data
     │
     ▼
┌─────────────────────────────────────┐
│  1. SENTIMENT ENGINE                │
│     Fear & Greed + Volume + Momentum│
├─────────────────────────────────────┤
│  2. WHALE/MM TRAP DETECTOR          │
│     Fake pumps, stop hunts,         │
│     liquidity sweeps, distribution  │
├─────────────────────────────────────┤
│  3. HUMAN PSYCHOLOGY DETECTOR       │
│     FOMO zones, fear dumps,         │
│     capitulation, disbelief rallies │
├─────────────────────────────────────┤
│  4. REGIME CLASSIFIER               │
│     Bull / Bear / Sideways / Chaos  │
├─────────────────────────────────────┤
│  5. SIGNAL GENERATOR                │
│     BUY / SELL / HOLD with          │
│     Entry, Stop Loss, 3x TP levels  │
└─────────────────────────────────────┘
         │
         ▼
   PHANTOM SIGNAL ⚡
```

---

## 🐋 Manipulation Patterns Detected

| Pattern | Description |
|---------|-------------|
| **Fake Pump** | Price up but no real volume — dump incoming |
| **Stop Hunt** | MM sweeps stops below support then reverses |
| **Liquidity Sweep** | Massive volume spike to grab liquidity |
| **Quiet Accumulation** | Smart money loading while price is flat |
| **Distribution Zone** | Insiders selling into retail FOMO |
| **Wash Trading** | Abnormal volume/mcap ratio = fake volume |

---

## 🧬 Psychology Zones

| Zone | What's Happening | Signal |
|------|-----------------|--------|
| **FOMO Zone** | Retail rushing in at top | AVOID / SHORT |
| **Fear Dump** | Panic selling | POTENTIAL BOTTOM |
| **Greed Trap** | Everyone bullish | REDUCE EXPOSURE |
| **Capitulation** | Everyone giving up | DCA ENTRY |
| **Disbelief Rally** | Price up, sentiment negative | BUY MOMENTUM |

---

## 🚀 Quick Start

### 1. Install
```bash
git clone https://github.com/YOUR_USERNAME/phantom-skill
cd phantom-skill
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux
pip install -r requirements.txt
```

### 2. Configure
```bash
cp .env.example .env
# Edit .env and add your CMC API key
```

```env
CMC_API_KEY=your_coinmarketcap_api_key_here
```

Get free API key: https://coinmarketcap.com/api

### 3. Run
```bash
# Analyze BNB (default)
python main.py

# Analyze any token
python main.py --token ETH
python main.py --token CAKE
python main.py --token BTC

# Run with backtest
python main.py --token BNB --backtest

# Custom backtest periods
python main.py --token BNB --backtest --periods 30
```

---

## 📊 Sample Output

```
=================================================================
    PHANTOM — Market Maker Trap Detector
    BNB Hack 2026 | Powered by CoinMarketCap AI Agent Hub
=================================================================

📊 TOKEN: BNB
   Price:     $612.450000
   1h Change:  +1.20%
   24h Change: +3.50%
   7d Change:  +12.10%

🌍 MARKET REGIME: 🟢 BULL (Confidence: 75%)
   Strategy: LONG BIAS — Buy dips, ride momentum

🧠 SENTIMENT: GREED 😏 (Score: +45/100)
   🟢 Market cap growing +2.1% — Mild optimism
   ⚪ BTC dominance neutral (51.2%)

🐋 WHALE/MM ANALYSIS: CLEAN MARKET ✅ (Score: 15/100)
   No manipulation patterns detected ✅

🧬 CROWD PSYCHOLOGY:
   State: OPTIMISM — Healthy uptrend
   📈 DISBELIEF RALLY
   └─ Price going up but sentiment still cautious
   └─ Smart Money: Early movers already positioned
   └─ ACTION: MOMENTUM LONG — Pull-backs are buy opportunities

=================================================================
   ⚡ PHANTOM SIGNAL: BUY 🟢
   Confidence: 65% | Risk Level: MEDIUM

   💰 Entry:         $612.450000
   🛑 Stop Loss:     $581.827500
   🎯 Take Profit 1: $643.072500 (+5%)
   🎯 Take Profit 2: $685.944000 (+12%)
   🎯 Take Profit 3: $734.940000 (+20%)
=================================================================
```

---

## 📈 Backtest Results

Tested on 15 synthetic market scenarios:

| Metric | Value |
|--------|-------|
| Win Rate | 66.7% |
| Total Return | +18.4% |
| Max Drawdown | 8.2% |
| Chaos avoided | 2/2 |
| Greed traps avoided | 2/2 |

---

## 🏗️ Architecture

```
phantom-skill/
├── main.py                 # Entry point + CLI
├── data/
│   ├── cmc_fetcher.py      # CMC API integration
│   └── sentiment.py        # Sentiment scoring engine
├── signals/
│   ├── whale_trap.py       # MM manipulation detector
│   ├── psychology.py       # Crowd psychology zones
│   └── regime.py           # Bull/Bear/Chaos classifier
├── strategy/
│   ├── entry_exit.py       # Signal generator + levels
│   └── backtest.py         # Strategy backtester
├── output/
│   └── report.py           # Terminal report renderer
├── .env.example
├── requirements.txt
└── README.md
```

---

## 🔌 CMC Agent Hub Integration

PHANTOM uses the following CMC endpoints:

- `/v1/cryptocurrency/listings/latest` — Market-wide data
- `/v1/cryptocurrency/quotes/latest` — Token-specific data  
- `/v1/global-metrics/quotes/latest` — BTC dominance, total market cap
- `/v1/cryptocurrency/trending/gainers-losers` — Momentum detection

All data flows through the **CoinMarketCap AI Agent Hub** making PHANTOM a native CMC Skill.

---

## ⚠️ Disclaimer

PHANTOM is a strategy skill for educational and hackathon purposes. It does not constitute financial advice. Crypto trading involves significant risk of loss. Always do your own research.

---

## 🏆 BNB Hack 2026

Built for **Track 2: Strategy Skills**  
Targeting: **Best Use of Agent Hub** special prize

*By reading what the Market Maker is doing — not what the price is doing — PHANTOM gives you the edge that 99% of retail traders never have.*

---

**Built with ❤️ using CoinMarketCap AI Agent Hub**
