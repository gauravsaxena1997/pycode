#! /usr/bin/python3.4
import pickle
import pandas as pd
import datetime
import matplotlib.dates as mdates
import pandas_datareader as web
from matplotlib import style
import matplotlib.pyplot as plt
import quandl

api_key = 'Kmpb5iKczd7kYD-XYj3c'

def state_list():
	states = pd.read_html ('https://simple.wikipedia.org/wiki/List_of_U.S._states')
	return states[0][1][1:]

def grab_intial_state_data():
	states =  state_list()
	main_df = pd.DataFrame()

	for abbr in states:
		query = 'FMAC/HPI_'+str(abbr) 
		df = quandl.get (query, authtoken =api_key)
		df.columns = [abbr]

		# To pct change from the prior hpi value
		# df = df.pct_change()

		# To pct change from the initial hpi value
		df[abbr] = (df[abbr]-df[abbr][0]) / df[abbr][0] * 100.0

		if main_df.empty:
			main_df = df
		else:
			main_df = main_df.join(df)
		print (abbr+" is joined")

	print (main_df.head())

	pickle_out = open('pct_change_initial.pickle','wb')
	pickle.dump(main_df, pickle_out)
	pickle_out.close()  


'''
# grab_intial_state_data() 
pickle_in = open('combined_data.pickle','rb')
HPI_data = pickle.load(pickle_in)

print (HPI_data)
'''

def HPI_Benchmark():
	df = quandl.get ('FMAC/HPI_USA', authtoken =api_key)
	df.columns = ['USA']
	df['USA'] = (df['USA']-df['USA'][0]) / df['USA'][0] * 100.0
	df.to_pickle ('USA_pct_change_initial.pickle')
	# print (df.head())

# HPI_Benchmark()

# by pandas pickling function
'''
HPI_data.to_pickle ('pickle.pickle')
pickle_data = pd.read_pickle ('pickle.pickle')
print (pickle_data)
'''