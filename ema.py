def ema(close, period=10):
    """Indicator: Exponential Moving Average (EMA)"""

    # Validate params
    period = int(period) if period > 1 else 10

    return close.ewm(span=period, adjust=False).mean()

ema.__doc__ = \
"""
Exponential Moving Average (EMA)

An exponential moving average (EMA) is a type of moving average (MA) 
that places a greater weight and significance on the most recent data 
points.

Sources:
    https://www.investopedia.com/terms/e/ema.asp
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.ewm.html

Calculation:
    close.ewm(span=period, adjust=False).mean()

Params:
    close (Pandas Series): Series of closing prices
    period (int): The period. Default 10


Returns:
    Pandas Series
"""