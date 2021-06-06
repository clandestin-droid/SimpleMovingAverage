# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 12:10:01 2021

@author: clandestine-droid
"""

# Getting the BTC historical data from yahoo

import datetime as dt
import pandas_datareader as web

crypto_currency = "BTC"
against_currency = "USD"

start = dt.datetime(2016,1,1)
end = dt.datetime.now()

data = web.DataReader(f'{crypto_currency}-{against_currency}', 'yahoo', start, end)

close = data['Close']

# Calculate the past returns from the last 4 months for the relative strength model

close_price_start = close[-85] #access the value before 84 days
close_price_end= close[-1] #access the last value of the pandas

close_price_difference = close_price_end - close_price_start

past_return = close_price_difference/close_price_start
past_return_percentage = past_return*100

# Calculate the moving average from the last 2 month for risk control
selected_timeframe = close.iloc[-60:]  #iloc is used to select the time frame

total_sum = selected_timeframe.sum()

MA_sixty = total_sum/60

# Compare to the current price
price_MA_difference = close_price_end - MA_sixty

print(past_return_percentage)
print(price_MA_difference)


