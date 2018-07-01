import matplotlib.pyplot as plt
import numpy as np
import pandas
import urllib
import matplotlib.dates as mdates

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter
    

fig = plt.figure()
ax1 = plt.subplot2grid ((1,1),(0,0))

stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
source_code = urllib.request.urlopen(stock_price_url).read().decode()
stock_data = []
split_source = source_code.split('\n')
print(split_source)
f = open('yahoo.txt','a')

for line in split_source:
	print(line)
	f.write(line)

f.close()