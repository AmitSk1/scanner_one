import yfinance as yf


def get_investment_value(symbol, start_date, end_date):
    try:
        data = yf.download(symbol, start=start_date, end=end_date)
        if data.empty:
            return 0, "No data available for symbol: " + symbol
        start_price = data.iloc[0]['Open']
        end_price = data.iloc[-1]['Close']
        shares_bought = 50 / start_price
        return shares_bought * end_price, None
    except Exception as e:
        return 0, str(e)


def calculate_total_value(symbols, start_date, end_date):
    total_value = 0
    investment_amount = 0
    for symbol in symbols:
        investment_value, error = get_investment_value(symbol, start_date,
                                                       end_date)
        investment_amount = investment_amount + 50
        if error is None:
            total_value += investment_value
        else:
            print(error)  # Handling errors by printing them
    percentage = ((total_value - investment_amount) / investment_amount) * 100
    return investment_amount, (total_value - investment_amount), percentage


# Example usage
symbols = ['HON', 'OC', 'GFL', 'RHI', 'FCN', 'ADT', 'R', 'JOBY', 'MDT', 'BIIB',
           'RMD', 'ILMN', 'IONS', 'ALKS', 'SGRY', 'ITGR', 'CERT', 'WRBY',
           'ADUS', 'SAGE', 'FNA', 'GYRE', 'MCHP', 'FIS', 'ON', 'EPAM', 'TER',
           'ZBRA', 'EXLS', 'BLKB', 'PEGA', 'CXM', 'FSLY', 'ESE', 'NATL',
           'MLNK', 'PDFS', 'DGII', 'RDZN', 'FARO', 'VPG', 'LUNA', 'PCG', 'MTB',
           'BEN', 'KEY', 'FAF', 'ZION', 'PB', 'OZK', 'HOMB', 'UBSI', 'ONB',
           'AB', 'CATY', 'UPST', 'NAD', 'AUB', 'BOH', 'BANC', 'PAX', 'FFBC',
           'TOWN', 'HTH', 'FRME', 'EVT', 'GCMG', 'FBNC', 'NTB', 'HOPE', 'NMFC',
           'ECPG', 'LMND', 'NIC', 'GABC', 'LC', 'DOW', 'AVNT', 'SLVM', 'TMST',
           'ACNT', 'ROL', 'FIVE', 'CHDN', 'HGV', 'YETI', 'QS', 'KSS', 'TNL',
           'LCII', 'AIN', 'ACVA', 'OXM', 'PHIN', 'MYE', 'FLWS', 'BWMX', 'LE',
           'CPHC', 'RGS', 'IVT', 'AIV', 'PLYM', 'RMR', 'ACR', 'FWONA', 'TWLO',
           'MANU', 'THRY', 'SJM', 'BJ', 'FIZZ', 'AM', 'CHX', 'VAL', 'CNX',
           'CEIX', 'VTOL', 'VTS', 'NC', 'PNRG', 'XLRE',
           'EPI', 'EMLP', 'SDOG', 'PID', 'BAB', 'ICF', 'IEO', 'FTXN', 'FXZ',
           'FXG', 'INDS', 'AGZ', 'CSB', 'FILL', 'LQDI', 'FFIU', 'SOUN', 'OSS',
           'NMTC', 'SPOFF']
# List of stock symbols
start_date = '2024-02-15'  # Start date of the investment
end_date = '2024-02-19'  # Target date for the investment's value calculation
invest_amount, change_in_usd, preantege = calculate_total_value(symbols,
                                                                start_date,
                                                                end_date)
print(f"Total value of the account move by {end_date}: {change_in_usd:.2f}$, "
      f"preantege: {preantege}%, investment amount: {invest_amount}$")
