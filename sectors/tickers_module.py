
from .ai import tickers_ai
from .airlines import tickers_airlines
from .biotech import tickers_biotech
from .canabis import tickers_canbis
from .car import tickers_car
from .crypto_stock import tickers_crypto_stock
from .industrials import tickers_industrials
from .crypto import tickers_crypto
from .robotics import tickers_robotics
from .space import tickers_space
from .utilities import tickers_utilities
from .healthcare import tickers_healthcare
from .technology import tickers_technology
from .basic_materials import tickers_basic_materials
from .communication_services import tickers_communication_services
from .consumer_cyclical import tickers_consumer_cyclical
from .consumer_defensive import tickers_consumer_defensive
from .energy import tickers_energy
from .financial_services import tickers_financial_services
from .real_estate import tickers_real_estate
from .etf import tickers_etf

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
    'Test': ['MINA-USD']
}