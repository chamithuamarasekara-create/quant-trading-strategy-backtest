import numpy as np
import pandas as pd

def performance_metrics(returns):
    """
    Calculate key performance metrics for a strategy.
    returns: Series of daily portfolio returns
    """

    
    total_return = (1 + returns).prod() - 1

    
    volatility = returns.std() * np.sqrt(252)

    
    sharpe_ratio = returns.mean() / returns.std() * np.sqrt(252)

    
    equity_curve = (1 + returns).cumprod()

    
    rolling_max = equity_curve.cummax()
    drawdown = equity_curve / rolling_max - 1
    max_drawdown = drawdown.min()

    
    hit_ratio = (returns > 0).mean()

    return {
        "Total Return": total_return,
        "Volatility": volatility,
        "Sharpe Ratio": sharpe_ratio,
        "Max Drawdown": max_drawdown,
        "Hit Ratio": hit_ratio
    }