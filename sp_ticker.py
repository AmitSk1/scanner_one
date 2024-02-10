import pandas as pd


def fetch_sp500_tickers():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    sp500_table = pd.read_html(url, header=0)
    sp500_df = sp500_table[0]  # The first table contains the constituents
    tickers = sp500_df['Symbol'].tolist()
    tickers = [ticker.replace('.', '-') for ticker in tickers]
    return tickers


sp500_tickers = fetch_sp500_tickers()
