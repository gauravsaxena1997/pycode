import matplotlib.pyplot as plt
import numpy as np
import urllib



stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
source_code = urllib.request.urlopen (stock_price_url).read().decode()
source_code = source_code.split ('\n')
stock_data = []

for line in source_code:
	split_line = line.split(',')
	print(split_line)
	split_line.pop(0)
	print(split_line)
	stock_data.append(split_line)
	
stock_data.pop(0)
print (stock_data)

# Open,High,Low,Close,Adjusted_close,Volume = np.loadtxt ( stock_data, delimiter=',', unpack=True )



plt.plot_date (Low,Open,label='Label')
# 	plt.plot (x1,y1,label='Second Line')
# 	plt.xlabel('xlabel')
# 	plt.ylabel('ylabel')

# 	plt.title('matplotlib\nfirst graph')
# 	plt.legend()
# 	plt.show()

# graph_data('TSLA')