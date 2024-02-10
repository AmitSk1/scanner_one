import datetime

import yfinance as yf
import pandas as pd
import datetime
from email_protocol import send_email
from ticker import tickers
import os


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


def find_pattern(ha_df, df):
    if len(ha_df) < 7:
        return False
    recent_ha = ha_df.iloc[-2:]
    past_ha = ha_df.iloc[-7:-2]
    recent_rsi = df['RSI'].iloc[-1] > 30
    ema9 = df['EMA9'].iloc[-1]
    ema26 = df['EMA26'].iloc[-1]
    ema_condition = ema9 > ema26
    if all(recent_ha['HA_Close'] > recent_ha['HA_Open']) and all(
            past_ha['HA_Close'] < past_ha[
                'HA_Open']) and recent_rsi and ema_condition:
        return True
    return False


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


def scan_stocks(tickers, file_path):
    matching_tickers = []

    for ticker in tickers:
        try:
            print(f"Processing {ticker}...")
            df = yf.download(ticker, period="1d", interval='5m')
            if df.empty:
                print(f"No data for {ticker}")
                continue
            df = calculate_rsi(df)
            df['EMA9'] = calculate_ema(df, 9)
            df['EMA26'] = calculate_ema(df, 26)
            ha_df = calculate_heikin_ashi(df)

            if find_pattern(ha_df, df):
                matching_tickers.append(ticker)
                print(f"Pattern found in: {ticker}")
                with open(file_path, 'a') as file:
                    file.write(ticker + '\n')
        except Exception as e:
            print(f"Failed to process {ticker}: {e}")

    return matching_tickers


def main():
    while True:
        print("\nAvailable sectors:")
        for sector in tickers.keys():
            print(sector)
        print("Enter 'all' to scan all sectors or 'exit' to quit the program.")

        chosen_sector = input("Please choose a sector to scan: ")

        if chosen_sector == 'exit':
            print("Exiting program. Goodbye!")
            break
        # Format the date to be appended to the file name
        date_str = datetime.date.today().strftime("%Y-%m-%d")
        if chosen_sector.lower() == 'all':
            file_name = "all_sectors_" + date_str + ".txt"
        else:
            file_name = chosen_sector + "_" + date_str + ".txt"

        print(f"File name: {file_name}")  # Optional: for confirmation
        file_path = ensure_the_directory_exists(file_name)

        if chosen_sector == 'all':
            print("\nStarting scan for all sectors...")
            for sector in tickers.keys():
                print(f"\nScanning sector: {sector}")
                matching_tickers = scan_stocks(tickers[sector], file_path)
                print(f"Tickers matching the pattern in {sector} sector:",
                      matching_tickers)

        elif chosen_sector in tickers:
            print(f"\nStarting scan for {chosen_sector} sector...")
            matching_tickers = scan_stocks(tickers[chosen_sector], file_path)
            print(f"Tickers matching the pattern in {chosen_sector} sector:",
                  matching_tickers)
        else:
            print("Sector not found. Please enter a valid sector.")
            continue

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
