#! /usr/bin/python3.4
import pickle
import pandas as pd
import datetime
import matplotlib.dates as mdates
import pandas_datareader as web
from matplotlib import style
import matplotlib.pyplot as plt
import quandl
style.use('ggplot')


fig = plt.figure()
ax1 = plt.subplot2grid ((1,1),(0,0))

states = pd.read_pickle ('pct_change_initial.pickle')

TX = states['TX'] 

# Default is mean

TX1yr = states['TX'].resample('H').mean() 
# TX1yr = states['TX'].resample('A').ohlc() 
print (TX1yr.head())


TX.plot(ax  = ax1, color='b', linewidth=1, label='ALA')
TX1yr.plot(ax  = ax1, color='r', linewidth=1, label='ALA anually')


plt.legend(loc=2)
plt.show()

# We can also down-sample / supersample the data