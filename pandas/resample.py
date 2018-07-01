#! /usr/bin/python3.4

import pandas
import datetime
# from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas_datareader as web
from matplotlib import style
import matplotlib.pyplot as plt

style.use('ggplot')
df = pandas.read_csv ('/root/Desktop/yahoo.txt',parse_dates=True, index_col=0)

# print(df.tail())
df_ohlc = df['Adjusted_close'].resample('10D').ohlc()
df_vol = df['Volume'].resample('10D').sum()

print (df_ohlc.head())


# ax1.plot(df.index,df['Adjusted_close'])
# ax1.plot(df.index,df['100ma'])
# ax2.bar(df.index,df['Volume'])


plt.show()
