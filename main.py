"""
PHANTOM — Market Maker Trap Detector
BNB Hack 2026 | Track 2 Strategy Skill
Powered by CoinMarketCap AI Agent Hub

Usage:
    python main.py                    # Analyze BNB (default)
    python main.py --token ETH        # Analyze specific token
    python main.py --backtest         # Run backtest
    python main.py --token CAKE --backtest   # Both
"""

import argparse
import sys

from data.cmc_fetcher import get_listings, get_fear_and_greed, get_token_info
from data.sentiment import analyze_sentiment
from signals.whale_trap import detect_whale_trap
from signals.psychology import detect_psychology_zones
from signals.regime import detect_regime
from strategy.entry_exit import generate_signal
from strategy.backtest import run_backtest
from output.report import (
    print_header,
    print_market_overview,
    print_regime,
    print_sentiment,
    print_whale_traps,
    print_psychology,
    print_final_signal,
    print_backtest_results
)

def analyze(token_symbol: str = "BNB"):
    print_header()

    print(f"  ⏳ Fetching live data for {token_symbol}...\n")

    # 1. Fetch data
    global_metrics = get_fear_and_greed()
    token_data = get_token_info(token_symbol)
    listings = get_listings(50)

    if not token_data or token_data.get("price", 0) == 0:
        print(f"  ❌ Could not fetch data for {token_symbol}")
        print(f"  Make sure your CMC_API_KEY is set in .env file")
        sys.exit(1)

    # 2. Run all analysis modules
    sentiment = analyze_sentiment(global_metrics, token_data)
    whale_trap = detect_whale_trap(token_data, listings)
    psychology = detect_psychology_zones(token_data, sentiment)
    regime = detect_regime(token_data, global_metrics, sentiment)
    signal = generate_signal(token_data, regime, whale_trap, psychology, sentiment)

    # 3. Print full report
    print_market_overview(token_data, global_metrics)
    print_regime(regime)
    print_sentiment(sentiment)
    print_whale_traps(whale_trap)
    print_psychology(psychology)
    print_final_signal(signal, token_symbol)

    return signal

def main():
    parser = argparse.ArgumentParser(
        description="PHANTOM — Market Maker Trap Detector"
    )
    parser.add_argument(
        "--token",
        type=str,
        default="BNB",
        help="Token symbol to analyze (default: BNB)"
    )
    parser.add_argument(
        "--backtest",
        action="store_true",
        help="Run backtest simulation"
    )
    parser.add_argument(
        "--periods",
        type=int,
        default=15,
        help="Number of backtest periods (default: 15)"
    )

    args = parser.parse_args()

    # Run live analysis
    analyze(args.token.upper())

    # Run backtest if requested
    if args.backtest:
        bt_results = run_backtest(args.token.upper(), args.periods)
        print_backtest_results(bt_results)

if __name__ == "__main__":
    main()
