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


states = pd.read_pickle ('pct_change_initial.pickle')

states_corr = states.corr()

print (states_corr.head())

# Descibe the corelation
desc = states_corr.describe()
print (desc)

