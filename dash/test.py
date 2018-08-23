from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json, time, sqlite3
from textblob import TextBlob
from unidecode import unidecode
import dash
from dash.dependencies import Output, Event, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
import pandas as pd

Consumer_Key = 'HxenUwwhFIcVBsbRNKvb1fekK' 
Consumer_Secret = 'hfFCvCOMcKCfJJ0n3emVWTDemkIr6rFMo2DhhR4FtcrLsYXFcN' 
Access_Token = '973076672231587840-Dh6SZrWFo0HcSAC82nNdXieL8ZKwF3R'
Access_Token_Secret = 'pVaaWWUYZPrmOatlgAmnQTb26o1WXaQKHBJsOTZzZ94ax'

topic=input()

class listener(StreamListener):
	def on_data(self, data):
		try:
			print('try')
			data = json.loads (data)
			tweet = unidecode(data['text'])
			analysis = TextBlob(tweet)
			sentiment = analysis.sentiment.polarity
			if sentiment != 0:
				time_ms = data['timestamp_ms']
			# 	user = data['user']
			# 	profile_url =  user['profile_image_url']
				print(time_ms, tweet,sentiment)
				saveThis = str(time_ms) +','+ str(tweet) +','+ str(sentiment)
				saveFile = open('tweets.csv', 'a')
				saveFile.write(saveThis+'\n')
				saveFile.close()
				df = pd.read_csv ('tweets.csv')
				print(df.head())
		except KeyError as e:
			print (str(e))

		return (True)

	def on_error(self, status):
	    print (status)


while True:
	try:
		auth = OAuthHandler (Consumer_Key,Consumer_Secret)
		auth.set_access_token (Access_Token,Access_Token_Secret)
		twitterStream = Stream(auth, listener())
		twitterStream.filter(track=[topic])
	except Exception as e:
		print(str(e))
		time.sleep(5)