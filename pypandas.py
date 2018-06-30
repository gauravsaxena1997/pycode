#! /usr/bin/python3.4

import pandas
import datetime
import pandas_datareader as web
from matplotlib import style
import matplotlib.pyplot as plt

style.use('ggplot')

# start = datetime.datetime (2016,1,1)
# end = datetime.datetime (2017,12,31)

# df = web.DataReader ('TSLA', 'morningstar', start, end)
# print (df.head())

# df.to_csv('/root/Desktop/tesla.txt')

df = pandas.read_csv ('/root/Desktop/tesla.txt',parse_dates=True, index_col=0)
print (df.head())

print (df[['Open']].head())

df.plot()
plt.show()
