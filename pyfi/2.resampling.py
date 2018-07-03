#! /usr/bin/python3.4
import pandas
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
from matplotlib import style
import matplotlib.pyplot as plt
style.use('ggplot')

df = pandas.read_csv ('small.txt',parse_dates=True, index_col=0)

# ohlc(): Building our own ohlc data baed on Adjusted_close, we can use any col that we want
df_ohlc = df['Adjusted_close'].resample('5D').ohlc()
df_volume = df['Volume'].resample('5D').sum()

# Change date format according to matplotlib
df_ohlc.reset_index(inplace=True)
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)
print(df_ohlc.head())
print (df_volume.head())

# Define Subplots
ax1 = plt.subplot2grid ( (6,1),(0,0),rowspan=4, colspan=1)
ax2 = plt.subplot2grid ( (6,1),(5,0),rowspan=1, colspan=1, sharex=ax1 )

ax1.xaxis_date()
for label in ax1.xaxis.get_ticklabels():
  label.set_rotation(45)
for label in ax2.xaxis.get_ticklabels():
  label.set_rotation(45)

candlestick_ohlc(ax1 , df_ohlc.values,width=2,colorup='g')
ax2.fill_between(df_volume.index,df_volume.values,0, color='b', alpha=0.3)
ax2.plot(df_volume.index,df_volume.values,color='b', alpha=0.7)

plt.subplots_adjust (left=0.08, bottom=0.15, right=0.93, top=0.88, wspace=0.20, hspace=0.34)
plt.show()