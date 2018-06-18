#! /usr/bin/python3

import tweepy
from textblob import TextBlob
import cgi
import cgitb
import sys
import time
cgitb.enable()	

#header information
print ("Content-type:text/html")
print ("")

web_data = cgi.FieldStorage()
topic =  web_data.getvalue('topic')
print (topic)

Consumer_Key = 'HxenUwwhFIcVBsbRNKvb1fekK' 
Consumer_Secret = 'hfFCvCOMcKCfJJ0n3emVWTDemkIr6rFMo2DhhR4FtcrLsYXFcN' 
Access_Token = '973076672231587840-Dh6SZrWFo0HcSAC82nNdXieL8ZKwF3R'
Access_Token_Secret = 'pVaaWWUYZPrmOatlgAmnQTb26o1WXaQKHBJsOTZzZ94ax'

auth = tweepy.OAuthHandler (Consumer_Key,Consumer_Secret)
auth.set_access_token (Access_Token,Access_Token_Secret)
connect = tweepy.API(auth)

get_data = connect.search(topic,count=10)
for i in get_data:
	print (i.text)
	# sys.stdout.write(i.text)
	# sys.stdout.flush()
	# time.sleep(2)
	# print ('</br>')
