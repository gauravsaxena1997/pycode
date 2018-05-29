#! /usr/bin/python3.4
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import cgi
import cgitb

cgitb.enable()

#header information
print ("Content-type:text/html")
print ("")

web_data = cgi.FieldStorage()
ch =  web_data.getvalue('choice')

if ch == '1':
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
		complete = details.find( 'div', class_= 'cb-text-complete' )
		if live is not None:
			live_matches.append (details)

		if complete is not None:
			complete_matches.append (details)

	# print ('\Live Matches:')
	# print ( live_matches)

	# print ('\nComplete Matches:\n')
	# print ( complete_matches )
def live():
	if ( len(live_matches) > 0):
		for score in live_matches:
			x = score.find ( 'div', class_= 'cb-lv-scrs-col text-black' )
			dotTag = score.find ( 'span', class_= 'cb-series-sch-dot' )
			dot = dotTag.text
			score_details =  x.text.strip().split(dot)

			live_statusTag = score.find ( 'div', class_= 'cb-text-live' )
			live_status = live_statusTag.text

			print ( "//------------------------------------------" )
			print ( "Team1: " + score_details[0] )
			print ( "Team2: " + score_details[1] )
			print ( "Live Status: " + live_status )
			print ( "------------------------------------------//" )

	else:
		print ("No live Matches found....")

def complete():
	for score in complete_matches:
		try:
			exception = score.div.span.text
		except:
			pass
		
		if ( exception is not None ):
			try:
				y = score.find ( 'div', class_= 'cb-lv-scrs-col text-black' )
				dotTag = score.find ( 'span', class_= 'cb-series-sch-dot' )
				dot = dotTag.text
				score_details =  y.text.strip().split(dot)

				complete_statusTag = score.find ( 'div', class_= 'cb-text-complete' )
				complete_status = complete_statusTag.text
				print ( "Team1: " + score_details[0] )
				print ( "Team2: " + score_details[1] )
				print ( "Live Status: " + complete_status )
				print ( "      -------------------" )

			except:
				pass


if __name__ == '__main__':
	live()
	complete()




# <div class="cb-scr-wll-chvrn"> <div class="cb-lv-scrs-col text-black"><span class="text-bold">PAK</span> 350/8 (110.0 Ovs) <span class="cb-series-sch-dot">&nbsp;•&nbsp;</span> <span class="text-bold">ENG</span> 184</div> <div class="cb-lv-scrs-col cb-text-live">Day 2: Stumps - Pakistan lead by 166 runs</div> </div>
