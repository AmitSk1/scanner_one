import yfinance as yf
import pandas as pd
from ticker import tickers
import os


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


def find_pattern(ha_df):
    if len(ha_df) < 7:
        return False
    if all(ha_df['HA_Close'].iloc[-2:] > ha_df['HA_Open'].iloc[-2:]) and all(
            ha_df['HA_Close'].iloc[-7:-2] < ha_df['HA_Open'].iloc[-7:-2]):
        return True
    return False


def ensure_the_directory_exists():
    output_dir = 'C:/finance'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    file_path = os.path.join(output_dir, 'scan_result.txt')
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
            df = yf.download(ticker, period="1mo", interval='1d')
            if df.empty:
                print(f"No data for {ticker}")
                continue
            ha_df = calculate_heikin_ashi(df)
            if find_pattern(ha_df):
                matching_tickers.append(ticker)
                print(f"Pattern found in: {ticker}")
                # Write the matching ticker to the file
                with open(file_path, 'a') as file:
                    file.write(ticker + '\n')
        except Exception as e:
            print(f"Failed to process {ticker}: {e}")
    return matching_tickers


def main():
    print("Available sectors:")
    for sector in tickers.keys():
        print(sector)
    print("Enter 'all' to scan all sectors.")
    chosen_sector = input(
        "Which sector do you want to scan (or 'all' for all sectors)? ")

    if chosen_sector.lower() == 'all':
        # Scan all sectors
        print("Starting scan for all sectors.")
        file_path = ensure_the_directory_exists()
        for sector in tickers.keys():
            print(f"Scanning sector: {sector}")
            matching_tickers = scan_stocks(tickers[sector], file_path)
            print(f"Tickers matching the pattern in {sector} sector:",
                  matching_tickers)
    elif chosen_sector in tickers:
        # Scan chosen sector
        chosen_tickers = tickers[chosen_sector]
        print(f"Starting scan for {chosen_sector} sector.")
        file_path = ensure_the_directory_exists()
        matching_tickers = scan_stocks(chosen_tickers, file_path)
        print(f"Tickers matching the pattern in {chosen_sector} sector:",
              matching_tickers)
    else:
        print("Sector not found. Please enter a valid sector or 'all'.")


if __name__ == '__main__':
    main()
