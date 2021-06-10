from TechnicalAnalysis.ema import ema


def macd(close, fast=12, slow=26):
    """Indicator: Moving Average Convergence Divergence (MACD)"""

    # Validate params
    fast = int(fast) if fast > 1 else 12
    slow = int(slow) if slow > 1 else 26

    if fast < slow:
        return ema(close, fast) - ema(close, slow)

macd.__doc__ = \
"""
Moving Average Convergence Divergence (MACD)

Moving average convergence divergence (MACD) is a trend-following 
momentum indicator that shows the relationship between two moving 
averages of a security’s price.

Sources:
    https://www.investopedia.com/terms/m/macd.asp

Calculation:
    EMA = Exponential Moving Average

    EMA(close, fast) - EMA(close, slow)

Params:
    close (Pandas Series): Series of closing prices
    fast (int): The fast period. Default 12
    slow (int): The slow period. Default 26


Returns:
    Pandas Series
"""