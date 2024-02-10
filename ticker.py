from sectors.industrials import tickers_industrials
from sectors.industrials import tickers_industrials
from sectors.crypto import tickers_crypto
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
    'Crypto': tickers_crypto}

print(tickers)