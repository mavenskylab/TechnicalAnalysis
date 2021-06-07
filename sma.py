def sma(close, period=10):
    """Indicator: Simple Moving Average (SMA)"""

    # Validate params
    period = int(period) if period > 1 else 10

    return close.rolling(period).mean()

sma.__doc__ = \
"""
Simple Moving Average (SMA)

A simple moving average (SMA) calculates the average of a selected 
range of prices, usually closing prices, by the number of periods in 
that range.

Sources:
    https://www.investopedia.com/terms/s/sma.asp

Calculation:
    close.rolling(period).mean()

Params:
    close (Pandas Series): Series of closing prices
    period (int): The period. Default 10


Returns:
    Pandas Series
"""