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

states['TX1yr'] = states['TX'].resample('A').mean() 

print(states[['TX','TX1yr']].head())
#drop all rows consisting NaN
# states.dropna(inplace=True)

#drop rows when all elements in a row consisting NaN
# states.dropna(how="all",inplace=True)

# states.fillna(method="ffill",inplace=True)   #take data from the previous
# states.fillna(method="bfill",inplace=True)   #take data from the the data below it

states.fillna(0,inplace=True)   #take data from the the data below it
print(states[['TX','TX1yr']])

states[['TX','TX1yr']].plot(ax  = ax1, colors=['b','k'], linewidth=1)


plt.legend(loc=2)
plt.show()

