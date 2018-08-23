from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json, time, sqlite3
from textblob import TextBlob
from unidecode import unidecode

conn = sqlite3.connect('twitter.db')
c = conn.cursor()

def create_table():
	try:
	    c.execute("CREATE TABLE IF NOT EXISTS sentiment(unix REAL, tweet TEXT, sentiment REAL)")
	    c.execute("CREATE INDEX fast_unix ON sentiment(unix)")
	    c.execute("CREATE INDEX fast_tweet ON sentiment(tweet)")
	    c.execute("CREATE INDEX fast_sentiment ON sentiment(sentiment)")
	    # c.execute("CREATE INDEX fast_url ON sentiment(url)")
	    conn.commit()
	except Exception as e:
		print(str(e))
create_table()

Consumer_Key = 'hqzcXRnqj5AoYr4MvTF9dbeYU' 
Consumer_Secret = 'jlTXxVjt3Nc0tA9fDtkwpIwoFXjXzeF4AQtGEDgni8nCy2mNES' 
Access_Token = '973076672231587840-Dh6SZrWFo0HcSAC82nNdXieL8ZKwF3R'
Access_Token_Secret = 'pVaaWWUYZPrmOatlgAmnQTb26o1WXaQKHBJsOTZzZ94ax'

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
			print(time_ms, tweet, sentiment)
			c.execute("INSERT INTO sentiment (unix, tweet, sentiment) VALUES (?, ?, ?)",
			      (time_ms, tweet, sentiment))
			conn.commit()
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
		twitterStream.filter(track=["modi"])
	except Exception as e:
		print(str(e))
		time.sleep(5)
