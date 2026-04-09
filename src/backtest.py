import pandas as pd

def run_backtest(prices, positions, transaction_cost=0.001):
    """
    prices: DataFrame of asset prices
    positions: DataFrame of positions (1 or 0)
    transaction_cost: cost per trade (default 0.1%)
    """


    returns = prices.pct_change().fillna(0)

    strategy_returns = positions * returns


    portfolio_returns = strategy_returns.mean(axis=1)


    trades = positions.diff().abs()
    costs = trades.mean(axis=1) * transaction_cost

    net_returns = portfolio_returns - costs

    return net_returns
