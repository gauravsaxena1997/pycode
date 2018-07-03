import bs4 as bs
import datetime as dt
import os
import pandas_datareader.data as web
import pickle
import requests
from getting_SandP_list_3 import save_sp500

def get_data_from_morningstar( reload_sp500=False ):
	if reload_sp500:
		tickers = save_sp500()
	else:
		with open("sp500tickers.pickle","rb") as f:
			tickers = pickle.load(f)

	if not os.path.exists('stock_dfs'):
		os.makedirs('stock_dfs')

	start = dt.datetime (2000,1,1)
	end = dt.datetime (2018,6,30)

	for ticker in tickers[50:51]:
		if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
			df = web.DataReader ( ticker,'morningstar', start, end )
			df.to_csv ('stock_dfs/{}.csv'.format(ticker))
			print ('{}.csv'.format(ticker) +" downloaded.")
		else:
			print ('Already have {}.csv'.format(ticker))


get_data_from_morningstar()