import yfinance as yf
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


check_ticker = ['BTC-USD', 'ETH-USD', 'BNB-USD', 'SOL-USD',
                'XRP-USD', 'ADA-USD', 'AVAX-USD', 'DOGE-USD',
                'TRX-USD', 'LINK-USD', 'DOT-USD', 'MATIC-USD',
                'ICP-USD', 'SHIB-USD', 'DAI-USD', 'LTC-USD',
                'BCH-USD', 'UNI7083-USD', 'ATOM-USD', 'ETC-USD',
                'LEO-USD', 'OP-USD', 'TIA22861-USD', 'IMX10603-USD',
                'XLM-USD', 'INJ-USD', 'TAO22974-USD', 'NEAR-USD',
                'APT21794-USD', 'KAS-USD', 'FDUSD-USD',
                'FIL-USD', 'LDO-USD', 'HBAR-USD', 'XMR-USD',
                'CRO-USD', 'VET-USD', 'MNT27075-USD', 'SUI20947-USD',
                'RUNE-USD', 'MKR-USD', 'RNDR-USD', 'GRT6719-USD',
                'BSV-USD', 'EGLD-USD', 'ALGO-USD', 'ORDI-USD',
                'AAVE-USD', 'QNT-USD', 'MINA-USD', 'FLOW-USD',
                'HNT-USD', 'DYM-USD', 'FTM-USD', 'SNX-USD',
                'BEAM28298-USD', 'THETA-USD', 'SAND-USD', 'BTT-USD',
                'AXS-USD', 'ASTR-USD', 'XTZ-USD', 'KCS-USD',
                '1000SATS-USD', 'FLR-USD', 'BGB-USD', 'CHEEL-USD',
                'CHZ-USD', 'ETHDYDX-USD', 'MANA-USD', 'CFX-USD',
                'NEO-USD', 'OSMO-USD', 'EOS-USD', 'BLUR-USD',
                'ROSE-USD', 'WEMIX-USD', 'KAVA-USD', 'IOTA-USD',
                'PYTH-USD', 'BONK-USD', 'RON14101-USD', 'KLAY-USD',
                'RVN-USD', 'SUSHI-USD', 'XAI28933-USD', 'API3-USD',
                'STORJ-USD', 'BDX-USD', 'DCR-USD', 'CHR-USD', 'T-USD',
                'WAVES-USD', 'ANKR-USD', 'YFI-USD', 'LYX-USD',
                'BICO-USD', 'USTC-USD', 'MEME28301-USD', 'LCX-USD',
                'FNSA-USD', 'LPT-USD', 'AUDIO-USD',
                'JTO-USD', 'GAL11877-USD', 'CTSI-USD', 'ERC20-USD',
                'ICX-USD', 'OM-USD', 'OAS-USD', 'GLM-USD',
                'ONE3945-USD', 'WE20456-USD', 'ONT-USD', 'BAL-USD',
                'FLUX-USD', 'BTRST-USD', 'MOVR-USD', 'POND-USD',
                'WAXP-USD', 'SXP-USD', 'ACE28674-USD', 'TRIBE-USD',
                'SFUND-USD', 'FLEX-USD', 'IOST-USD',
                'JOE-USD', 'LSK-USD', 'ALPH-USD', 'XVS-USD', 'DOGE-USD',
                'USDJ-USD', 'CTC-USD', 'C98-USD', 'BORG-USD', 'Forged',
                'RLC-USD', 'ARK-USD', 'XYM-USD', 'POWR-USD', 'COTI-USD']

# Sort stocks by their sector
sorted_stocks = sort_stocks_by_sector(crypto_ticker)
print(sorted_stocks)

"""# Print the sorted stocks
for sector, symbols in sorted_stocks.items():
    print(f"Sector: {sector}, Stocks: {symbols}")

for sector in sorted_stocks.items():
    print(sector)
    print()"""
