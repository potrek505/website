import requests, os
from binance.client import Client
from pybit.unified_trading import HTTP

session = HTTP(
    api_key= os.environ.get('bybit_api_key'),
    api_secret= os.environ.get('bybiy_api_secret'),
    testnet=False,
)

def profit(capital_in_pln,deposit_fee,p2p_price):
    data_nbp = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/eur/").json()
    data_bybit = session.get_orderbook(category="spot", symbol="USDTEUR")
    client = Client(os.environ.get('binance_api_key'), os.environ.get('binance_api_secret'))
    ticker = client.get_symbol_ticker(symbol='USDTPLN')

    eur_pln_exchange_rate = float(data_nbp['rates'][0]['mid'])
    usdt_eur_exchange_rate = float(data_bybit['result']['b'][0][0])
    binance_spot_exchange_rate = float(ticker['price'])

    eur_amount = round((round(capital_in_pln/eur_pln_exchange_rate,2)) * (1 - deposit_fee),2)
    usdt_amount = eur_amount/usdt_eur_exchange_rate

    return f"""W przypadku ceny p2p wynoszącej {p2p_price}, zwrot wynosi {round(usdt_amount * p2p_price,2)},
Przy sprzedaży na rynku spot na Binance, zwrot wynosi {round((usdt_amount - 1) * binance_spot_exchange_rate,2)}"""