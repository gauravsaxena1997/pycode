#! /usr/bin/python3.4
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL Certificate Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen('http://www.cricbuzz.com/cricket-match/live-scores/', context=ctx).read()

soup = BeautifulSoup ( html, 'html.parser' )

live_matches = list()
complete_matches = list()
#Retrieve all anchor tags
all_matches = soup.find_all ( 'div', class_= 'cb-scr-wll-chvrn' )
for details in all_matches:
	live = details.find( 'div', class_= 'cb-text-live' )
	if live is not None:
		live_matches.append (details)
	else:
		complete_matches.append (details)

print ('\Live Matches:')
print ( live_matches)

# print ('\nComplete Matches:\n')
# print ( complete_matches )

for score in live_matches:
	x = score.find ( 'div', class_= 'cb-lv-scrs-col text-black' )
	score_details =  x.text.strip().split()
	print (score_details)


	live_status = score.find ( 'div', class_= 'cb-text-live' )
	print ( live_status.text )









# <div class="cb-scr-wll-chvrn"> <div class="cb-lv-scrs-col text-black"><span class="text-bold">PAK</span> 350/8 (110.0 Ovs) <span class="cb-series-sch-dot">&nbsp;•&nbsp;</span> <span class="text-bold">ENG</span> 184</div> <div class="cb-lv-scrs-col cb-text-live">Day 2: Stumps - Pakistan lead by 166 runs</div> </div>
#Bating Details
# bat = final_live.find( 'div', class_= 'cb-hmscg-bat-txt' )
# team = bat.find( 'div', class_= 'cb-ovr-flo' )
# bat_team = str(team.text)
# score = bat.find( 'div', attrs = { 'style': "display:inline-block; width:140px" } )
# live_score = str(score.text)

# #Bowling Details
# bwl = final_live.find( 'div', class_= 'cb-hmscg-bwl-txt' )
# team = bwl.find( 'div', class_= 'cb-ovr-flo' )
# bwl_team = str(team.text)
# score1 = bwl.find( 'div', attrs = { 'style': "display:inline-block; width:140px" } )
# live_score1 = str(score1.text)

# #Print Details of live matches
# print ('\n')
# # print ( "Go to website: " + final_live['href'] )
# print ( '    *---[ cricbuzz live score ]---*')
# print ( '/----------------------------------' )
# print ( "Title: " + final_live['title'] )
# status = final_live.find( 'div', class_= 'cb-text-live' )
# print ( "Status: " + status.text )
# print ( "Bating Team: " + bat_team + '\t' +"Score: " + live_score )
# print ( "Bowling Team: " + bwl_team + '\t' +"Score: " + live_score1 )
# print ( '----------------------------------/' )