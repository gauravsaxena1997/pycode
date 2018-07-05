import pandas_datareader.data as web
import pickle
import pandas as pd

def compile_data():
	with open("sp500tickers.pickle","rb") as f:
		tickers = pickle.load(f)

	main_df = pd.DataFrame()

	for count,ticker in enumerate(tickers):
		try:
			df = pd.read_csv ('stock_dfs/{}.csv'.format(ticker))
			df.set_index ('Date',inplace=True)
			df.rename (columns = {'Open':ticker}, inplace=True)
			df.drop(['Symbol','Close','High','Low','Volume'], 1, inplace=True)

			if main_df.empty:
				main_df = df
			else:
				main_df = main_df.join (df,how='outer')
			print (ticker + ' joined' )  
		except:
			pass

	print (main_df.tail())
	main_df.to_csv('combined_data.csv')

compile_data()