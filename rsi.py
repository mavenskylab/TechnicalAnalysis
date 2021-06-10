from TechnicalAnalysis.rma import rma


def rsi(close, period=14):
    """Indicator: Relative Strength Index (RSI)"""

    # Validate params
    period = int(period) if period > 1 else 14

    gain = close.diff()
    loss = gain * -1

    gain[gain < 0] = 0
    loss[loss < 0] = 0

    avg_gain = rma(gain, period)
    avg_loss = rma(loss, period)

    rs = avg_gain / avg_loss

    return 100 - (100 / (1 + rs))


rsi.__doc__ = \
"""
Relative Strength Index (RSI)

The relative strength index (RSI) is a momentum indicator used in 
technical analysis that measures the magnitude of recent price changes to
evaluate overbought or oversold conditions in the price of a stock or 
other asset.

Sources:
    https://www.investopedia.com/terms/e/ema.asp
    https://www.tradingview.com/support/solutions/43000502338-relative-strength-index-rsi/
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.ewm.html

Calculation:
    RMA = Wilder's Moving Average

    gain = close.diff()
    loss = gain * -1

    gain[gain < 0] = 0
    loss[loss < 0] = 0

    avg_gain = RMA(gain, period)
    avg_loss = RMA(loss, period)

    rs = avg_gain / avg_loss

    100 - (100 / (1 + rs))

Params:
    close (Pandas Series): Series of closing prices
    period (int): The period. Default 14


Returns:
    Pandas Series
"""