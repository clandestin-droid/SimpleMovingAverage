# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 16:20:59 2021

@author: danie
"""

from pandas_datareader import data
import matplotlib.pyplot as plt
import datetime as dt


start = dt.datetime(2015,1,1)
end = dt.datetime.now()

#Getting the data
data = data.DataReader('BTC-USD', 'yahoo', start, end)

#Calculate MA_42
data["MA_42"] = data.Close.rolling(42).mean()
data["difference"] = data["Close"]-data.MA_42
data["returns"] = data.Close.pct_change()

#Defining the strategy
signal = data.difference > 0  

#Backtesting
signal_perf = (data.returns.shift(-1) * signal + 1).cumprod()

#Benchmark
holding_perf = (data.returns.shift(-1) + 1).cumprod()

#Plotting results daily
plt.style.use("fivethirtyeight")
plt.figure(figsize=(20,10))
plt.title("Backtest")
plt.ylabel("multiple of the returns")
plt.plot(signal_perf, label="daily strat")
plt.plot(holding_perf, label="daily holding")
plt.legend()
plt.show()

print(data.difference[-1])












