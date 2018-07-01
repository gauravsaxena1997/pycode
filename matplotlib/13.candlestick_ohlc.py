import matplotlib.pyplot as plt
import numpy as np
import pandas
import urllib
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter
    
#Define subplot
fig = plt.figure()
ax1 = plt.subplot2grid ((1,1),(0,0))

stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
source_code = urllib.request.urlopen(stock_price_url).read().decode()
stock_data = []
split_source = source_code.split('\n')
for line in split_source[1:]:
    split_line = line.split(',')
    stock_data.append(line)

date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,delimiter=',',unpack=True,converters={0: bytespdate2num('%Y-%m-%d')})

x = 0
y = len(date)
ohlc = []

while x < y:
    append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
    ohlc.append(append_me)
    x+=1

candlestick_ohlc(ax1, ohlc)

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.subplots_adjust (left=0.12, bottom=0.21, right=0.90, top=0.90, wspace=0.20, hspace=0.20)
plt.show()

















