import datetime

import yfinance as yf
import pandas as pd
import datetime
from email_protocol import send_email
from sectors.tickers_module import tickers
import os


def calculate_ema_signal(df, ema_length=300):
    """
    Calculates buy or sell signals based on EMA criteria.

    :param df: DataFrame containing stock price data.
    :param ema_length: Length of the EMA. Default is 300.
    :return: Tuple (buy_signal, sell_signal) indicating whether there are buy or sell signals.
    """
    df['EMA'] = df['Close'].ewm(span=ema_length, adjust=False).mean()
    # Define buy and sell signals
    buy_signal = (df['Low'] > df['EMA']) & (
            df['Low'].shift(1) <= df['EMA'].shift(1))
    sell_signal = (df['High'] < df['EMA']) & (
            df['High'].shift(1) >= df['EMA'].shift(1))
    return buy_signal.iloc[-1], sell_signal.iloc[-1]


def calculate_rsi(df, period=14):
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))

    df['RSI'] = rsi
    return df


def calculate_ema(df, period=9):
    ema = df['Close'].ewm(span=period, adjust=False).mean()
    return ema


def calculate_heikin_ashi(df):
    ha_df = pd.DataFrame(index=df.index)
    ha_df['HA_Close'] = (df['Open'] + df['High'] + df['Low'] + df['Close']) / 4
    ha_df['HA_Open'] = 0.0
    ha_df['HA_High'] = 0.0
    ha_df['HA_Low'] = 0.0
    for i in range(len(df)):
        ha_df['HA_Open'].iloc[i] = ((df['Open'].iloc[i - 1] + df['Close'].iloc[
            i - 1]) / 2) if i > 0 else (df['Open'].iloc[0] + df['Close'].iloc[
            0]) / 2
        ha_df['HA_High'].iloc[i] = max(df['High'].iloc[i],
                                       ha_df['HA_Open'].iloc[i],
                                       ha_df['HA_Close'].iloc[i])
        ha_df['HA_Low'].iloc[i] = min(df['Low'].iloc[i],
                                      ha_df['HA_Open'].iloc[i],
                                      ha_df['HA_Close'].iloc[i])
    return ha_df


def calculate_bollinger_bands(df, period=20, num_std_dev=2):
    """Calculate Bollinger Bands for a given DataFrame."""
    rolling_mean = df['Close'].rolling(window=period).mean()
    rolling_std = df['Close'].rolling(window=period).std()

    upper_band = rolling_mean + (rolling_std * num_std_dev)
    lower_band = rolling_mean - (rolling_std * num_std_dev)

    df['Bollinger_Upper'] = upper_band
    df['Bollinger_Lower'] = lower_band
    df['Bollinger_Middle'] = rolling_mean

    return df


def buy_signal_bollinger_rsi(df):
    last_row = df.iloc[-1]
    if last_row['Close'] < last_row['Bollinger_Lower'] and last_row[
        'RSI'] > 30:
        stop_loss = last_row['Bollinger_Lower'] * 0.97
        target_price = last_row['Bollinger_Upper']
        # Define entry point range as from the lower Bollinger Band up to 2% above it
        entry_point_start = last_row['Bollinger_Lower']
        entry_point_end = last_row['Bollinger_Lower'] * 1.02
        return True, stop_loss, target_price, (
            entry_point_start, entry_point_end)
    return False, None, None, None


def buy_signal_basic(ha_df, df):
    if len(ha_df) < 7:
        return False, None, None, None
    recent_ha = ha_df.iloc[-2:]
    past_ha = ha_df.iloc[-7:-2]
    recent_rsi = df['RSI'].iloc[-1] > 30
    ema9 = df['EMA9'].iloc[-1]
    ema26 = df['EMA26'].iloc[-1]
    ema_condition = ema9 > ema26
    if all(recent_ha['HA_Close'] > recent_ha['HA_Open']) and all(
            past_ha['HA_Close'] < past_ha[
                'HA_Open']) and recent_rsi and ema_condition:
        stop_loss = past_ha['HA_Low'].min()
        entry_price = df['Close'].iloc[-1]
        risk_amount = entry_price - stop_loss
        target_price = entry_price + (2 * risk_amount)
        # Define entry point range as from the EMA9 up to 1% above it
        entry_point_start = ema9
        entry_point_end = ema9 * 1.01
        return True, stop_loss, target_price, (
            entry_point_start, entry_point_end)
    return False, None, None, None


def ensure_the_directory_exists(file_name):
    output_dir = 'C:/finance'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    file_path = os.path.join(output_dir, file_name)
    clear_file_contents(file_path)
    return file_path


def clear_file_contents(file_path):
    with open(file_path, 'w'):
        pass


def scan_stocks(tickers, file_path, strategy_choice):
    buy_tickers = []

    for ticker in tickers:
        try:
            print(f"Processing {ticker}...")
            df = yf.download(ticker, period="2y", interval='1d')
            if df.empty:
                print(f"No data for {ticker}")
                continue
            df = calculate_rsi(df)
            df['EMA9'] = calculate_ema(df, 9)
            df['EMA26'] = calculate_ema(df, 26)
            strategies_found = []

            # Inside scan_stocks, adjust the if conditions where strategies are called
            if strategy_choice in ['2', '4']:
                df = calculate_bollinger_bands(df)
                buy_signal, stop_loss, target_price, entry_range = buy_signal_bollinger_rsi(
                    df)
                if buy_signal:
                    strategies_found.append(
                        f"Bollinger Bands & RSI. Entry range: {entry_range[0]:.2f}-{entry_range[1]:.2f}, Target Price: {target_price:.2f}, Stop loss: {stop_loss:.2f}")

            if strategy_choice in ['1', '4']:
                ha_df = calculate_heikin_ashi(df)
                buy_signal, stop_loss, target_price, entry_range = buy_signal_basic(
                    ha_df,
                    df)
                if buy_signal:
                    strategies_found.append(
                        f"Basic.Entry range: {entry_range[0]:.2f}-{entry_range[1]:.2f}, Target Price: {target_price:.2f}, Stop loss: {stop_loss:.2f}")

            if strategy_choice in ['3', '4']:
                buy_signal, sell_signal = calculate_ema_signal(df, 300)
                if buy_signal:
                    strategies_found.append("EMA Buy Signal")
                if sell_signal:
                    strategies_found.append("EMA Sell Signal")

            if strategies_found:
                buy_tickers.append(ticker)
                # Fetch Yahoo Finance link
                yahoo_finance_link = f"https://finance.yahoo.com/quote/{ticker}"
                with open(file_path, 'a') as file:
                    strategy_names = ', '.join(strategies_found)
                    file.write(
                        f"BUY {ticker} - found in strategies: {strategy_names}."
                        f" link for yahoo: {yahoo_finance_link}\n")
                print(f"Pattern found in {ticker} using {strategy_names}")

        except Exception as e:
            print(f"Failed to process {ticker}: {e}")

    return buy_tickers


def main():
    while True:
        print("\nAvailable sectors:")
        for sector in tickers.keys():
            print(sector)
        print(
            "Enter 'all' to scan all sectors, 'exit' to quit the program, or choose a specific sector.")

        chosen_sector = input("Please choose a sector to scan: ")

        if chosen_sector == 'exit':
            print("Exiting program. Goodbye!")
            break

        print(
            "Choose strategy: 1 for Basic, 2 for Bollinger Bands & RSI, 3 for EMA, 4 for all")
        strategy_choice = input("Strategy number: ")
        print(f"you chose: {strategy_choice}")
        date_str = datetime.date.today().strftime("%Y-%m-%d")
        file_name = f"{chosen_sector}_{date_str}.txt" if chosen_sector.lower() != 'all' else f"all_sectors_{date_str}.txt"
        file_path = ensure_the_directory_exists(file_name)

        if chosen_sector.lower() == 'all':
            all_buy_tickers = []
            for sector in tickers.keys():
                buy_tickers = scan_stocks(tickers[sector], file_path,
                                          strategy_choice)
                all_buy_tickers.extend(buy_tickers)
        else:
            all_buy_tickers = scan_stocks(tickers[chosen_sector], file_path,
                                          strategy_choice)

        print("\nSummary of Buy Signals:")
        print(f"Total Buy Signals Found: {len(all_buy_tickers)}")
        print("Tickers with Buy Signals:", all_buy_tickers)

        user_choice = input(
            "\nWould you like to continue? (y/n): ").strip().lower()
        if user_choice != 'y':
            print("Exiting program. Goodbye!")
            break


def send_file():
    file_path = 'C:/finance/scan_result.txt'
    with open(file_path, 'r') as file:
        scan_results = file.read()

    subject = "Scan Results"
    body = "Here are the scan results:\n\n" + scan_results
    recipient_email = "amitskarbin1@gmail.com"  # Replace with your email
    sender_email = "amitskarbincrypto@gmail.com"  # Replace with your email
    sender_password = "Joker123$"  # Replace with your email password

    send_email(subject, body, recipient_email, sender_email, sender_password)
    print("Email sent with scan results.")


if __name__ == '__main__':
    main()
    # send_file()
