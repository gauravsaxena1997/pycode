#! /usr/bin/python3.4

import pandas
import datetime
import matplotlib.dates as mdates
import pandas_datareader as web
from matplotlib import style
import matplotlib.pyplot as plt
import quandl

# df = quandl.get('FMAC/HPI_AK')

# print(df.head())

df = pandas.read_html ('https://simple.wikipedia.org/wiki/List_of_U.S._states')
# print(df[0][1])

for abbr in df[0][1][1:]:
	print ('FMAC/HPI_'+str(abbr)) 