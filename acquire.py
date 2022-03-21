import pandas as pd
import numpy as np

def acquire():
    '''Reads csv's from cryptodatadownload's Gemini database and combines them into a dataframe'''
    btc = 'https://www.cryptodatadownload.com/cdd/Gemini_BTCUSD_day.csv'
    btc = pd.read_csv(btc, skiprows=[0])
    eth = 'https://www.cryptodatadownload.com/cdd/Gemini_ETHUSD_day.csv'
    eth = pd.read_csv(eth, skiprows=[0])
    ltc = 'https://www.cryptodatadownload.com/cdd/Gemini_LTCUSD_day.csv'
    ltc = pd.read_csv(ltc, skiprows=[0])
    df = pd.concat([btc, eth, ltc])
    return df