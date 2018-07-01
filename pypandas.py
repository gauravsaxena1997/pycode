#! /usr/bin/python3.4

import pandas
import datetime
import pandas_datareader as web
from matplotlib import style
import matplotlib.pyplot as plt

style.use('ggplot')

# ----------------------1----------------------------
# start = datetime.datetime (2016,1,1)
# end = datetime.datetime (2017,12,31)

# df = web.DataReader ('TSLA', 'morningstar', start, end)
# print (df.head())

# df.to_csv('/root/Desktop/tesla.txt')

# ----------------------2----------------------------
# df = pandas.read_csv ('/root/Desktop/tesla.txt',parse_dates=True, index_col=0)
# print (df.head())

# print (df[['Open']].head())

# df[['Open','Close']].plot()
# plt.show()

# ----------------------3----------------------------
df = pandas.read_csv ('/root/Desktop/yahoo.txt',parse_dates=True, index_col=0)


df ['100ma'] = df ['Adjusted_close'].rolling(window=100, min_periods=0).mean()                                                  
# df.dropna (inplace=True)                                                                                

ax1 = plt.subplot2grid ( (6,1),(0,0),rowspan=5, colspan=1 )
ax2 = plt.subplot2grid ( (6,1),(5,0),rowspan=1, colspan=1, sharex=ax1 )

ax1.plot(df.index,df['Adjusted_close'])
ax1.plot(df.index,df['100ma'])
ax2.bar(df.index,df['Volume'])


plt.show()


'''
 
- ma(moving avg)=avg of current and 99 prior
- inplace = modyfing data without creating new dataframe
- index_col=0  : not showing index_col
- min_periods  : if there are not 100 operands it calculate whatever it has,like:
							  Open      100ma
							                     
							 240.01   240.010000
							 230.72   235.365000
							 226.36   232.363333
							 220.00   229.272500
							 214.19   226.256000


 '''