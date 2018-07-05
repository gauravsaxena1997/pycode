import pandas_datareader.data as web
import numpy as np
import pickle
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('mystyle')

def vizualize_data():
	df = pd.read_csv('combined_data.csv')
	df_corr = df.corr()
	print(df_corr.head())
	df_corr.to_csv('correlation.csv')
	data1 = df_corr.values
	fig1 = plt.figure()
	ax1 = fig1.add_subplot(111)

	# Heatmap color bar
	heatmap1 = ax1.pcolor(data1, cmap=plt.cm.RdYlGn)
	fig1.colorbar(heatmap1)

	ax1.set_xticks(np.arange(data1.shape[1]) + 0.5, minor=False)
	ax1.set_yticks(np.arange(data1.shape[0]) + 0.5, minor=False)
	ax1.invert_yaxis()
	ax1.xaxis.tick_top()
	column_labels = df_corr.columns
	row_labels = df_corr.index
	ax1.set_xticklabels(column_labels)
	ax1.set_yticklabels(row_labels)
	plt.xticks(rotation=90)
	heatmap1.set_clim(-1, 1)
	plt.tight_layout()
	# plt.savefig("correlations.png", dpi = (300))
	plt.show()


vizualize_data()