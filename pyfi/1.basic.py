#! /usr/bin/python3.4
import pandas
import datetime
import pandas_datareader as web
from matplotlib import style
import matplotlib.pyplot as plt

style.use('ggplot')


df = pandas.read_csv ('small.txt',parse_dates=True, index_col=0)


df['100ma'] = df['Adjusted_close'].rolling(window=100, min_periods=0).mean()                                                  
# df.dropna (inplace=True)                                                                                

print (df['100ma'])

ax1 = plt.subplot2grid ( (6,1),(0,0),rowspan=5, colspan=1 )
ax2 = plt.subplot2grid ( (6,1),(5,0),rowspan=1, colspan=1, sharex=ax1 )

ax1.plot(df.index,df['Adjusted_close'])
ax1.plot(df.index,df['100ma'])
ax2.bar(df.index,df['Volume'])

plt.show()