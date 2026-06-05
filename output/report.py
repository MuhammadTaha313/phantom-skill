"""
PHANTOM Report Generator
Beautiful terminal output with all signals
"""
from colorama import init, Fore, Back, Style
from tabulate import tabulate
import datetime

init(autoreset=True)

def print_header():
    print("\n" + "=" * 65)
    print(Fore.CYAN + Style.BRIGHT + """
    ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
    ██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
    ██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
    ██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
    ██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
    """)
    print(Fore.YELLOW + "    Market Maker Trap Detector | BNB Hack 2026")
    print(Fore.WHITE + "    Powered by CoinMarketCap AI Agent Hub")
    print("=" * 65)
    print(f"    {Fore.WHITE}Analysis Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print("=" * 65 + "\n")

def print_market_overview(token_data: dict, global_metrics: dict):
    symbol = token_data.get("symbol", "?")
    price = token_data.get("price", 0)
    p1h = token_data.get("percent_change_1h", 0)
    p24h = token_data.get("percent_change_24h", 0)
    p7d = token_data.get("percent_change_7d", 0)
    vol = token_data.get("volume_24h", 0)

    print(Fore.CYAN + Style.BRIGHT + f"📊 TOKEN: {symbol}")
    print(f"   Price:     ${price:,.6f}")

    def color_pct(val):
        if val > 0:
            return Fore.GREEN + f"+{val:.2f}%" + Style.RESET_ALL
        elif val < 0:
            return Fore.RED + f"{val:.2f}%" + Style.RESET_ALL
        return f"{val:.2f}%"

    print(f"   1h Change:  {color_pct(p1h)}")
    print(f"   24h Change: {color_pct(p24h)}")
    print(f"   7d Change:  {color_pct(p7d)}")
    print(f"   Volume 24h: ${vol:,.0f}")
    print(f"   BTC Dom:    {global_metrics.get('btc_dominance', 0):.1f}%")
    print()

def print_regime(regime: dict):
    color_map = {
        "BULL": Fore.GREEN,
        "BEAR": Fore.RED,
        "SIDEWAYS": Fore.YELLOW,
        "CHAOS": Fore.RED + Style.BRIGHT,
        "TRANSITION": Fore.YELLOW
    }
    r = regime.get("regime", "?")
    c = color_map.get(r, Fore.WHITE)
    print(c + Style.BRIGHT + f"🌍 MARKET REGIME: {regime['color']} {r} (Confidence: {regime['confidence']}%)")
    print(Fore.WHITE + f"   Strategy: {regime['strategy']}")
    print()

def print_sentiment(sentiment: dict):
    score = sentiment.get("score", 0)
    label = sentiment.get("label", "?")
    if score > 30:
        color = Fore.GREEN
    elif score < -30:
        color = Fore.RED
    else:
        color = Fore.YELLOW
    print(color + Style.BRIGHT + f"🧠 SENTIMENT: {label} (Score: {score:+d}/100)")
    for sig in sentiment.get("signals", []):
        print(Fore.WHITE + f"   {sig}")
    print()

def print_whale_traps(whale_trap: dict):
    score = whale_trap.get("trap_score", 0)
    overall = whale_trap.get("overall", "?")
    if score >= 60:
        color = Fore.RED + Style.BRIGHT
    elif score >= 30:
        color = Fore.YELLOW
    else:
        color = Fore.GREEN

    print(color + f"🐋 WHALE/MM ANALYSIS: {overall} (Manipulation Score: {score}/100)")
    patterns = whale_trap.get("patterns", [])
    if patterns:
        for p in patterns:
            print(Fore.WHITE + f"   {p['type']}")
            print(Fore.LIGHTBLACK_EX + f"   └─ {p['detail']}")
            print(Fore.CYAN + f"   └─ ACTION: {p['action']}")
    else:
        print(Fore.GREEN + "   No manipulation patterns detected ✅")
    print()

def print_psychology(psychology: dict):
    print(Fore.MAGENTA + Style.BRIGHT + "🧬 CROWD PSYCHOLOGY:")
    print(Fore.WHITE + f"   State: {psychology.get('crowd_state', '?')}")
    for zone in psychology.get("zones", []):
        print(Fore.YELLOW + f"   {zone['zone']}")
        print(Fore.WHITE + f"   └─ {zone['detail']}")
        print(Fore.CYAN + f"   └─ Smart Money: {zone['smart_money']}")
        print(Fore.GREEN + f"   └─ ACTION: {zone['action']}")
    print()

def print_final_signal(signal_data: dict, symbol: str):
    sig = signal_data.get("signal", "?")
    conf = signal_data.get("confidence", 0)
    entry = signal_data.get("entry")
    sl = signal_data.get("stop_loss")
    tp1 = signal_data.get("take_profit_1")
    tp2 = signal_data.get("take_profit_2")
    tp3 = signal_data.get("take_profit_3")
    risk = signal_data.get("risk_level", "?")

    print("=" * 65)
    if "BUY" in sig:
        color = Fore.GREEN + Style.BRIGHT
    elif "SELL" in sig or "SHORT" in sig:
        color = Fore.RED + Style.BRIGHT
    elif "AVOID" in sig or "STAY OUT" in sig:
        color = Fore.RED
    else:
        color = Fore.YELLOW

    print(color + f"\n   ⚡ PHANTOM SIGNAL: {sig}")
    print(Fore.WHITE + f"   Confidence: {conf}% | Risk Level: {risk}")

    print(Fore.WHITE + "\n   Reasons:")
    for r in signal_data.get("reasons", []):
        print(f"   • {r}")

    if entry:
        print(f"\n   💰 Entry:       ${entry:,.6f}")
        print(Fore.RED + f"   🛑 Stop Loss:   ${sl:,.6f}")
        print(Fore.YELLOW + f"   🎯 Take Profit 1: ${tp1:,.6f} (+5%)")
        print(Fore.GREEN + f"   🎯 Take Profit 2: ${tp2:,.6f} (+12%)")
        print(Fore.GREEN + Style.BRIGHT + f"   🎯 Take Profit 3: ${tp3:,.6f} (+20%)")

    print("\n" + "=" * 65)

def print_backtest_results(bt: dict):
    print(Fore.CYAN + Style.BRIGHT + "\n📈 BACKTEST RESULTS")
    print("=" * 65)
    print(f"   Symbol:         {bt['symbol']}")
    print(f"   Periods:        {bt['periods']} days")
    print(f"   Starting Cap:   ${bt['starting_capital']:,.2f}")
    print(f"   Ending Cap:     ${bt['ending_capital']:,.2f}")

    ret = bt['total_return_pct']
    print(Fore.GREEN + f"   Total Return:   +{ret:.2f}%" if ret > 0 else Fore.RED + f"   Total Return:   {ret:.2f}%")

    wr = bt['win_rate']
    print(Fore.GREEN + f"   Win Rate:       {wr:.1f}%" if wr >= 55 else Fore.YELLOW + f"   Win Rate:       {wr:.1f}%")

    print(Fore.WHITE + f"   Wins/Losses:    {bt['wins']}W / {bt['losses']}L")
    print(Fore.YELLOW + f"   Max Drawdown:   {bt['max_drawdown_pct']:.2f}%")
    print(f"\n   {bt['verdict']}")
    print("=" * 65 + "\n")
