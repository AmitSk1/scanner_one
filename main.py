import yfinance as yf
import datetime
from sectors.tickers_module import tickers
import os
from calculate_indicator import calculate_ema, calculate_rsi, \
    calculate_heikin_ashi, calculate_ema_signal, calculate_bollinger_bands, \
    buy_signal_basic, buy_signal_bollinger_rsi


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
            df = yf.download(ticker, period="3mo", interval='1d')
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


if __name__ == '__main__':
    main()
    # send_file()
