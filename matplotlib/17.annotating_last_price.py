import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
import pandas
import numpy as np
import urllib
import datetime as dt


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter
    

def graph_data(stock):

    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))
    stock_data = open('small.txt').read().splitlines()
    
    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,
                                                          converters={0: bytespdate2num('%Y-%m-%d')})

    x = 0
    y = len(date)
    ohlc = []

    while x < y:
        append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        print (append_me)
        ohlc.append(append_me)
        x+=1

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    ax1.grid(True)
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    candlestick_ohlc(ax1, ohlc, width=0.4, colorup='#77d879', colordown='#db3f3f')


    # ax1.xaxis.set_major_locator(mticker.MaxNLocator(7))
    bbox_props = dict(boxstyle='round',fc='w', ec='k',lw=1)

    ax1.annotate(str(closep[-1]), (date[-1], closep[-1]),
                 xytext = (date[0]+1, closep[-1]), bbox=bbox_props)


    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(stock)
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()


graph_data('EBAY')