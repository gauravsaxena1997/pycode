import numpy as np
import pandas as pd
import pickle

def proces_data_for_labels (ticker):
	hm_days = 7
	df = pd.read_csv ('combined_data.csv', index_col=0)
	tickers = df.columns.values.tolist()
	df.fillna (0, inplace=True)
	print (tickers)

	for i in range (1, hm_days+1):
		
		df['{}_{}d'.format(ticker,i)] = ( df[ticker].shift(-i) - df[ticker] ) / df[ticker]
		print (df['{}_{}d'.format(ticker,i)])
	
	df.fillna (0, inplace=True)

	return tickers, df



proces_data_for_labels('GOOGL')