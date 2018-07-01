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
    
#Define subplot
fig = plt.figure()
ax1 = plt.subplot2grid ((1,1),(0,0))

stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
source_code = urllib.request.urlopen(stock_price_url).read().decode()
stock_data = []
split_source = source_code.split('\n')
print(split_source)
for line in split_source[1:]:
    split_line = line.split(',')
    stock_data.append(line)

date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                      delimiter=',',
                                                      unpack=True,
                                                      converters={0: bytespdate2num('%Y-%m-%d')})

ax1.plot_date(date, closep,'-', label='Price', alpha=0.7)

# -----------------------fill---------------
# ax1.fill_between (date, closep, 200, label='Price')
# ax1.fill_between (date, closep, alpha=0.3)
# ax1.fill_between (date, closep, closep[0], alpha=0.3)                                     # starting from first closing price to see profit up and lose down

ax1.fill_between (date, closep,closep[0], where=(closep>closep[0]), facecolor='g', alpha=0.3, label='gain')
ax1.fill_between (date, closep,closep[0], where=(closep<closep[0]), facecolor='r', alpha=0.3, label='loss')

for label in ax1.xaxis.get_ticklabels():
  label.set_rotation(45)


#show grids
ax1.grid(True,color='#bdbdbd',linestyle='-',linewidth=0.2)

#set labelcolors
ax1.xaxis.label.set_color('r')
ax1.yaxis.label.set_color('m')

#set y ticks (no that shows in y axis)
ax1.set_yticks([0,100,200,300,400,500,600,700])                                              #can be set to show specific ranges


plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.subplots_adjust (left=0.12, bottom=0.21, right=0.90, top=0.90, wspace=0.20, hspace=0.20)
plt.show()

















