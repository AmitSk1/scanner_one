from concurrent.futures import ThreadPoolExecutor
import yfinance as yf
import time
from main import calculate_ema_signal, calculate_rsi, calculate_heikin_ashi, buy_signal_basic, calculate_ema

def fetch_and_process(ticker):
    try:
        print(f"Attempting to download data for {ticker}...")
        df = yf.download(ticker, period="2y", interval='1d')
        if not df.empty:
            print(f"Processing {ticker}...")
            df = calculate_rsi(df)
            df['EMA9'] = calculate_ema(df, 9)
            df['EMA26'] = calculate_ema(df, 26)
            strategies_found = []

            ha_df = calculate_heikin_ashi(df)
            buy_signal, stop_loss, target_price, entry_range = buy_signal_basic(ha_df, df)
            if buy_signal:
                strategies_found.append(
                    f"Basic. Entry range: {entry_range[0]:.2f}-{entry_range[1]:.2f}, Target Price: {target_price:.2f}, Stop loss: {stop_loss:.2f}")
                print(f"Strategy found for {ticker}: {strategies_found}")
            else:
                print(f"No strategy found for {ticker}.")
        else:
            print(f"No data for {ticker}")
    except Exception as e:
        print(f"Failed to process {ticker}: {e}")

def main():
    tickers = ['CAT', 'UNP', 'GE', 'HON', 'BA', 'UPS', 'RTX', 'ETN', 'DE',
               'LMT', 'ADP', 'ITW', 'WM', 'GD', 'CSX', 'NOC', 'PH', 'TT',
               'CTAS', 'TDG', 'FDX', 'EMR', 'NSC', 'PCAR', 'RSG', 'CARR',
               'CPRT', 'MMM', 'GWW', 'ODFL', 'PAYX', 'URI', 'WCN', 'FERG',
               'FAST', 'LHX', 'AME', 'JCI', 'OTIS', 'VRSK', 'CMI', 'GPN',
               'IR', 'ROK', 'EFX', 'PWR', 'XYL', 'SYM', 'DAL', 'WAB',
               'VRT', 'HWM', 'BLDR', 'HEI-A', 'DOV', 'JBHT', 'AXON',
               'VLTO', 'HUBB', 'LUV', 'BAH', 'EXPD', 'J', 'IEX', 'TXT',
               'CSL', 'WSO', 'MAS', 'LII', 'AER', 'CNHI', 'NDSN', 'SAIA',
               'POOL', 'GGG', 'XPO', 'UAL', 'SNA', 'SWK', 'TRU', 'LECO',
               'OC', 'GFL', 'WMS', 'BLD', 'PNR', 'ACM', 'UHAL', 'AOS',
               'ALLE', 'EME', 'HII', 'NVT', 'TTC', 'FBIN', 'RRX', 'ITT',
               'WCC', 'TREX', 'WSC', 'AAL', 'CLH', 'KNX', 'TTEK', 'CNM',
               'AGCO', 'CW', 'CHRW', 'RHI', 'FIX', 'APG', 'WWD', 'DCI',
               'ARMK', 'MIDD', 'GNRC', 'BWXT', 'RBC', 'DLB', 'AYI', 'OSK',
               'KBR', 'AIT', 'SITE', 'CR', 'WTS', 'MSA', 'FCN', 'LSTR',
               'FLR', 'GXO', 'AAON', 'AZEK', 'ADT', 'HXL', 'CAR', 'TKR',
               'TNET', 'MLI', 'MTZ', 'BECN', 'MSM', 'ZWS', 'ATKR', 'FLS',
               'ESAB', 'FTAI', 'ATI', 'GTLS', 'DRS', 'R', 'CWST', 'MMS',
               'KEX', 'LPX', 'VMI', 'SPXC', 'FSS', 'ALK', 'MOG-A', 'AL',
               'AWI', 'FELE', 'GATX', 'SRCL', 'SNDR', 'HRI', 'CAAP',
               'MATX', 'CPA', 'MDU', 'AEIS', 'JOBY', 'ACA', 'TEX', 'EXPO',
               'WIRE', 'VRRM', 'BCO', 'ENS', 'KAI', 'NSP', 'CSWI', 'MAN',
               'AVAV', 'GFF', 'GMS', 'SEB', 'CXT', 'DY', 'ARCB', 'SPR',
               'GTES', 'NPO', 'ENOV', 'CBZ', 'JBT', 'HI', 'UNF', 'MGRC']  # Example ticker list

    # Adjust max_workers based on your system's capabilities and the API's rate limit policy
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(fetch_and_process, tickers)

if __name__ == '__main__':
    main()
