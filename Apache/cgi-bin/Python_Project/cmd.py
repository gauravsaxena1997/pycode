#!/usr/bin/python3.4

import time
import subprocess
import socket
import webbrowser as wb
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import whois
import json
import cgi
import cgitb

cgitb.enable()

#header information
print ("Content-type:text/html")
print ("")

web_data = cgi.FieldStorage()
ch =  web_data.getvalue('choice')


if (ch == '1'):
	input_data = input("Enter the data: ")
	data_list = input_data.strip().split()
	for i in data_list:
		wb.open_new_tab('http://www.google.com/search?q='+i)
		time.sleep(2)

elif (ch == '2'):
	input_data = input("Enter the data: ")
	data_list = input_data.strip().split()
	for i in data_list:
		wb.open_new_tab('http://www.google.com/search?tbm=isch&q='+i)
		time.sleep(2)

elif (ch == '3'):
	#Ignore SSL Certificate Errors
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE

	url = input("Enter the url: ")

	html = urllib.request.urlopen('http://'+url, context=ctx).read()

	soup = BeautifulSoup ( html, 'html.parser' )

	#Retrieve all anchor tags
	tags = soup ( 'a' )
	for tag in tags:
		print ( tag.get( 'href', None ) )

elif (ch == '4'):
	
	time = subprocess.getoutput ('date +%H:%M:%S')
	date = subprocess.getoutput ('date +%d-%m-%Y')
	print ("Current time: "+ date + '\n' + 'Current date: ' + time)

elif (ch == '5'):
	wb.open('http://www.google.com')

elif (ch == '6'):
	ip = socket.gethostbyname('www.google.com')
	print (ip)

elif (ch == '7'):
	url = input ("Enter the URL: ")
	full_url = str (whois.whois( 'http://'+url ))
	#print (whois)
	info = json.loads (full_url)
	emails = info['emails']
	address = info['address']
	domain_name = info['domain_name']
	print ("Emails:" + emails)
	print ("Address: " + address)
	print ("Domain name: " + domain_name)




# result = c.getoutput(out)
# print  '<h4>'
# print  '<pre>'
# print result
# print  '</pre>'                                                              #data of x variable in web_data is stored
# print  '</h4>'

