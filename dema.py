from TechnicalAnalysis.ema import ema


def dema(close, period=10):
    """Indicator: Double Exponential Moving Average (DEMA)"""

    # Validate params
    period = int(period) if period > 1 else 10

    eman = ema(close, period)
    return 2 * eman - ema(eman)


dema.__doc__ = \
"""
DoubleExponential Moving Average (DEMA)

The Double Exponential Moving Average (DEMA) is a technical indicator that 
uses two moving averages to help confirm uptrends when price moves above 
average, and confirm downtrends when the price moves below average.

Sources:
    https://www.tradingview.com/support/solutions/43000589132-double-exponential-moving-average-ema/

Calculation:
    eman = ema(close, period)
    2 * eman - ema(eman)

Params:
    close (Pandas Series): Series of closing prices
    period (int): The period. Default 10


Returns:
    Pandas Series
"""
