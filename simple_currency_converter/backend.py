import requests
import pandas as pd

def exchange_rates(pln_amount, currencies):
    data_nbp = requests.get("http://api.nbp.pl/api/exchangerates/tables/a/").json()
    codes = []
    rates = []
    pln_values = []

    for rate in data_nbp[0]['rates']:
        codes.append(rate['code'])
        rates.append(rate['mid'])
        pln_values.append(round(float(pln_amount) / rate['mid'], 2))

    exchanged_amount = pd.DataFrame({'rates': rates, 'pln value': pln_values}, index=codes)

    return exchanged_amount.loc[currencies].to_html()
