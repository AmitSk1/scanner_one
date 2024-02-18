import yfinance as yf
import re

def get_price_movement(symbol, start_date):
    try:
        data = yf.download(symbol, start=start_date)
        if data.empty:
            return None, "No data available"
        start_price = data.iloc[0]['Close']
        current_price = data.iloc[-1]['Close']
        price_change_percent = ((current_price - start_price) / start_price) * 100
        return price_change_percent, None
    except Exception as e:
        return None, str(e)

def read_symbols_from_file(file_path):
    symbols = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 2:
                symbols.append(parts[1])
            else:
                symbols.append(parts[0])
    return symbols

def process_symbols(file_path, start_date):
    symbols = read_symbols_from_file(file_path)
    movements = {}
    for symbol in symbols:
        movement, error = get_price_movement(symbol, start_date)
        if movement is not None:
            movements[symbol] = f"{movement:.2f}%"
        else:
            movements[symbol] = "Error: " + error
    return movements

def extract_date_from_path(file_path):
    match = re.search(r'\d{4}-\d{2}-\d{2}', file_path)
    return match.group() if match else None

# Example usage
file_path = "C:\\finance\\all_sectors_2024-02-15.txt"
date = extract_date_from_path(file_path)
print(f"Starting scan for {file_path} from date {date} until today")

price_movements = process_symbols(file_path, date)
for symbol, movement in price_movements.items():
    if "Error" not in movement:
        try:
            numeric_movement = float(movement.rstrip('%'))
            status = "BULLISH" if numeric_movement > 0 else "BEARISH"
            print(f"{status} Price movement for {symbol} since {date}: {movement}")
        except ValueError:
            # This block will be executed if movement is not a valid float, which should not happen due to earlier checks
            print(f"Invalid movement data for {symbol}: {movement}")
    else:
        print(f"Error for {symbol}: {movement}")
