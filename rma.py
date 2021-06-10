def rma(close, period=10):
    """Wilder's Moving Average (RMA)"""

    # Validate params
    period = int(period) if period > 1 else 10

    return close.ewm(alpha=1/period, min_periods=period).mean()


rma.__doc__ = \
"""
Wilder's Moving Average (RMA)

The Wilder's Smoothing study is similar to the Exponential Moving Average 
with the difference that Wilder's Smoothing uses a smoothing factor of 
1/length which makes it respond more slowly to price changes compared to 
other moving averages.

Sources:
    https://tlc.thinkorswim.com/center/reference/Tech-Indicators/studies-library/V-Z/WildersSmoothing
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.ewm.html

Calculation:
    close.ewm(alpha=1/period, min_periods=period).mean()

Params:
    close (Pandas Series): Series of closing prices
    period (int): The period. Default 10


Returns:
    Pandas Series
"""