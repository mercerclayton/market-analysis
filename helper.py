import numpy as np
import pandas as pd
import yfinance as yf

def get_price(ticker, period='10y'):
    """
    Retrieves closing price data for a given ticker. Default period is 10 years.
    """
    data = yf.Ticker(ticker).history(period=period)
    data.index = data.index.date # removes timezone info
    data = data.rename(columns={'Close': ticker})
    return data[[ticker]]