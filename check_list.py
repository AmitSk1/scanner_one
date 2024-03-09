import yfinance as yf
import re


def get_price_movement(symbol, start_date):
    try:
        data = yf.download(symbol, start=start_date)
        if data.empty:
            return None, "No data available"
        start_price = data.iloc[0]['Close']
        current_price = data.iloc[-1]['Close']
        price_change_percent = ((
                                            current_price - start_price) / start_price) * 100
        return price_change_percent, None
    except Exception as e:
        return None, str(e)


def read_symbols_from_file(file_path):
    symbols = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()  # Assuming space is the delimiter
            if len(parts) >= 2:
                symbols.append(parts[1])  # Second word in each line
            else:
                symbols.append(parts[0])  # First word in each line
    return symbols


def process_symbols(file_path, start_date):
    symbols = read_symbols_from_file(file_path)
    movements = {}
    for symbol in symbols:
        movement, error = get_price_movement(symbol, start_date)
        if movement is not None:
            movements[symbol] = f"{movement:.2f}"
        else:
            movements[symbol] = "Error: " + error
    return movements


file_path = "C:\\finance\\all_sectors_2024-02-15.txt"  # Replace with the path to your file


def extract_date_from_path(file_path):
    # Regular expression to match the date format YYYY-MM-DD
    match = re.search(r'\d{4}-\d{2}-\d{2}', file_path)
    if match:
        return match.group()  # Returns the matched date string
    else:
        return None  # No date found in the path


date = extract_date_from_path(file_path)

# Example usage
start_date = date  # Adjust as needed year/ month/ day
print(f"starting scan for {file_path} from date{start_date} until today")
print(file_path)
print(start_date)

price_movements = process_symbols(file_path, start_date)
for symbol, movement in price_movements.items():
    print(movement)
    if int(movement[0:2]) > 0:
        status = "BULLISH"
    else:
        status = "BEARISH"

    print(f"{status} Price movement for {symbol} since {start_date}: {movement}")
