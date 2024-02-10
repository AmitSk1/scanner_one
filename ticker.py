from sectors.ai import tickers_ai
from sectors.airlines import tickers_airlines
from sectors.biotech import tickers_biotech
from sectors.canabis import tickers_canbis
from sectors.car import tickers_car
from sectors.crypto_stock import tickers_crypto_stock
from sectors.industrials import tickers_industrials
from sectors.crypto import tickers_crypto
from sectors.robotics import tickers_robotics
from sectors.space import tickers_space
from sectors.utilities import tickers_utilities
from sectors.healthcare import tickers_healthcare
from sectors.technology import tickers_technology
from sectors.basic_materials import tickers_basic_materials
from sectors.communication_services import tickers_communication_services
from sectors.consumer_cyclical import tickers_consumer_cyclical
from sectors.consumer_defensive import tickers_consumer_defensive
from sectors.energy import tickers_energy
from sectors.financial_services import tickers_financial_services
from sectors.real_estate import tickers_real_estate
from sectors.etf import tickers_etf

tickers = {
    'Industrials': tickers_industrials,
    'Healthcare': tickers_healthcare,
    'Technology': tickers_technology,
    'Utilities': tickers_utilities,
    'Financial Services': tickers_financial_services,
    'Basic Materials': tickers_basic_materials,
    'Consumer Cyclical': tickers_consumer_cyclical,
    'Real Estate': tickers_real_estate,
    'Communication Services': tickers_communication_services,
    'Consumer Defensive': tickers_consumer_defensive,
    'Energy': tickers_energy,
    'Crypto': tickers_crypto,
    'ETF': tickers_etf,
    'Ai': tickers_ai,
    'Robotics': tickers_robotics,
    'Space': tickers_space,
    'Car': tickers_car,
    'Crypto stocks': tickers_crypto_stock,
    'Airlines': tickers_airlines,
    'Biotech': tickers_biotech,
    'Canbis': tickers_canbis,
    'Test': ['MINA-USD']}
counter = 0


def count_tickers(tickers_dict):
    total_tickers = 0
    for sector, ticker_list in tickers_dict.items():
        count = len(ticker_list)
        total_tickers += count
        print(f"{sector}: {count} tickers")
    print(f"Total tickers across all sectors: {total_tickers}")


if __name__ == '__main__':
    count_tickers(tickers)
