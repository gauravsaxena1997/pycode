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

# At dec 2000 hpi is perfect 100

states = pd.read_pickle ('pct_change_initial.pickle')
benchmark = pd.read_pickle ('USA_pct_change_initial.pickle')


states.plot(ax  = ax1)
benchmark.plot(ax  = ax1, color='k', linewidth=5)


plt.legend().remove()
plt.show()