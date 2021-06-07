import matplotlib.pyplot as plt

def plot_line(df):
    """Graph: Plot close with indicators"""

    plt.plot(df.index, df['close'])

    for col in df.columns:
        if col not in ['open', 'high', 'low', 'volume']:
            plt.plot(df.index, df[col], label=col)

    plt.ylabel("Price")
    plt.xlabel("Date")
    plt.legend()
    plt.show()


plot_line.__doc__ = \
"""
Grpahs the closing price along side other indicators included in the 
pandas dataframe. Ignores open, high, low and volume columns.

Sources:
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

Method:
    plt.plot(df.index, df['close'])

    for col in df.columns:
        if col not in ['open', 'high', 'low', 'volume']:
            plt.plot(df.index, df[col], label=col)

Params:
    df (Pandas Dataframe): Dataframe of ohlc and indicator data

Returns:
    None
"""