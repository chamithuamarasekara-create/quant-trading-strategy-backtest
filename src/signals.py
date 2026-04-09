
import pandas as pd

def momentum_signal(prices, lookback=20):
    """
    Momentum = past lookback-day return
    """
    momentum = prices.pct_change(periods=lookback, fill_method=None)
    return momentum


def momentum_positions(momentum):
    """
    Convert momentum signal into positions:
    1 = long
    0 = no position
    """
    positions = (momentum > 0).astype(int)
    return positions
