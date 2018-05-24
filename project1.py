#! /usr/bin/python3.4

import time
import subprocess
import socket
import webbrowser as wb
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import whois
import json


menu = '''
1.) Search data in web browser in seperate tabs
2.) Search images in web browser in seperate tabs
3.) Search URLs of first webpage
4.) Current date & time
5.) Open default web browser
6.) All network IP
7.) Check owner & email and contact (if available) 
'''
print (menu)
# data_list = []
# def search():
# 	input_data = raw_input("Enter the data: ")
# 	data_list = input_data.strip().split()
# 	print data_list
# 	return data_list

ch = input("Enter your choice: ")
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








