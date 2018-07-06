import pyrebase
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json, time, sqlite3
from textblob import TextBlob
from unidecode import unidecode

Consumer_Key = 'HxenUwwhFIcVBsbRNKvb1fekK' 
Consumer_Secret = 'hfFCvCOMcKCfJJ0n3emVWTDemkIr6rFMo2DhhR4FtcrLsYXFcN' 
Access_Token = '973076672231587840-Dh6SZrWFo0HcSAC82nNdXieL8ZKwF3R'
Access_Token_Secret = 'pVaaWWUYZPrmOatlgAmnQTb26o1WXaQKHBJsOTZzZ94ax'

config = {
    'apiKey': "AIzaSyCsFZXDyAcAiSPPFmox32R4vBx2GMdVBSE",
    'authDomain': "twitter-sentiment-33b5f.firebaseapp.com",
    'databaseURL': "https://twitter-sentiment-33b5f.firebaseio.com",
    'projectId': "twitter-sentiment-33b5f",
    'storageBucket': "twitter-sentiment-33b5f.appspot.com",
    'messagingSenderId': "1081160536869"
}

firebase = pyrebase.initialize_app (config)
auth1 = firebase.auth ()
database = firebase.database()
storage=firebase.storage()

class listener(StreamListener):

	def on_data(self, data):
		try:
			data = json.loads (data)
			time_ms = data['timestamp_ms']
			tweet = unidecode(data['text'])
			# user = data['user']
			# profile_url =  user['profile_image_url']
			analysis = TextBlob(tweet)
			sentiment = analysis.sentiment.polarity
			data =  str(time_ms) + "/split/" + str(tweet) + "/split/" + str(sentiment)
			print (data)
			data = {
				'data' : data
			}

			database.child('Tweets').set(data)

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
		twitterStream.filter(track=["a","e","o","i","u"])
	except Exception as e:
		print(str(e))
		time.sleep(5)

	
firebase_data = database.child('Tweets').shallow().get().val()
lis = firebase_data.split('/split/')
print (lis)
