import yfinance as yf
from sp_ticker import sp500_tickers
from etf import etf_ticker
from crypto import crypto_ticker

def sort_stocks_by_sector(stock_symbols):
    # Dictionary to hold lists of stocks by sector
    sectors_dict = {}

    for symbol in stock_symbols:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        sector = info.get('sector')

        # If the sector is available, sort the symbol into the correct sector list
        if sector:
            print(f"symbol: {ticker}, sector: {sector}")
            # If the sector doesn't exist in the dictionary, create a new list
            if sector not in sectors_dict:
                sectors_dict[sector] = [symbol]
            else:
                sectors_dict[sector].append(symbol)
        else:
            print(f"symbol: {ticker}, sector: not found")
            # Handle stocks with no sector information
            if 'Unknown Sector' not in sectors_dict:
                sectors_dict['Unknown Sector'] = [symbol]
            else:
                sectors_dict['Unknown Sector'].append(symbol)

    return sectors_dict

check_ticker = ['UNI7083-USD']
# Sort stocks by their sector
sorted_stocks = sort_stocks_by_sector(crypto_ticker)
print(sorted_stocks)

"""# Print the sorted stocks
for sector, symbols in sorted_stocks.items():
    print(f"Sector: {sector}, Stocks: {symbols}")

for sector in sorted_stocks.items():
    print(sector)
    print()"""
