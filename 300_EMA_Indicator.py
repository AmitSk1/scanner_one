import yfinance as yf
import pandas as pd


def calculate_ema_signal(stock_list, ema_length=300):
    """
    Scan stocks for buy or sell signals based on EMA.

    Parameters:
    - stock_list: List of stock ticker symbols to scan.
    - ema_length: Length of the EMA window. Default is 300.

    Returns:
    A dictionary with stock symbols as keys and their signals ('Buy', 'Sell', or 'None') as values.
    """
    signals = {}

    for ticker in stock_list:
        print(f"Processing {ticker}...")
        df = yf.download(ticker, period="2y", interval="1d")

        if df.empty:
            print(f"No data for {ticker}")
            continue

        df['EMA'] = df['Close'].ewm(span=ema_length, adjust=False).mean()

        # Check for buy and sell signals in the last 3 candles
        # Corrected buy and sell signal calculation
        buy_signal = (df['Low'] > df['EMA']) & (
                df['Low'].shift(1) <= df['EMA'].shift(1))
        sell_signal = (df['High'] < df['EMA']) & (
                df['High'].shift(1) >= df['EMA'].shift(1))

        if buy_signal.iloc[-1]:
            signals[ticker] = 'Buy'
        elif sell_signal.iloc[-1]:
            signals[ticker] = 'Sell'
        else:
            signals[ticker] = 'None'

    return signals


# Example usage:
stock_list = ['ZBRA']  # Add your stocks here
signals = calculate_ema_signal(stock_list)
print(signals)
