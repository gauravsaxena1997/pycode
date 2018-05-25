#! /usr/bin/python3.4
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL Certificate Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen('http://www.cricbuzz.com/', context=ctx).read()

soup = BeautifulSoup ( html, 'html.parser' )

#Retrieve all anchor tags
a = soup.find_all ( 'a', class_= 'cb-font-12' )

for live_matches in a:
	live = live_matches.find( 'div', class_= 'cb-hmscg-bwl-txt' )
	if live is not None:
		final_live = live_matches

#print (final_live)

#Bating Details
bat = final_live.find( 'div', class_= 'cb-hmscg-bat-txt' )
team = bat.find( 'div', class_= 'cb-ovr-flo' )
bat_team = str(team.text)
score = bat.find( 'div', attrs = { 'style': "display:inline-block; width:140px" } )
live_score = str(score.text)

#Bowling Details
bwl = final_live.find( 'div', class_= 'cb-hmscg-bwl-txt' )
team = bwl.find( 'div', class_= 'cb-ovr-flo' )
bwl_team = str(team.text)
score1 = bwl.find( 'div', attrs = { 'style': "display:inline-block; width:140px" } )
live_score1 = str(score1.text)

#Print Details of live matches
print ('\n')
# print ( "Go to website: " + final_live['href'] )
print ( '    *---[ cricbuzz live score ]---*')
print ( '/----------------------------------' )
print ( "Title: " + final_live['title'] )
status = final_live.find( 'div', class_= 'cb-text-live' )
print ( "Status: " + status.text )
print ( "Bating Team: " + bat_team + '\t' +"Score: " + live_score )
print ( "Bowling Team: " + bwl_team + '\t' +"Score: " + live_score1 )
print ( '----------------------------------/' )