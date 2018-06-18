#! /usr/bin/python3

import cgi
import cgitb
# import subprocess as sb
import mysql.connector as pysql

cgitb.enable()

#header information
print ("Content-type:text/html")
print ("")

web_data = cgi.FieldStorage()
email =  web_data.getvalue('email')
password =  web_data.getvalue('password')

conn = pysql.connect(user='root',password='m487',database='hadoop',host='localhost')


if ( conn.is_connected() ):
	cur = conn.cursor()
		
	query =  ("SELECT * FROM signup "
                 "WHERE email='{}' and password='{}';".format(email,password) )
	try:
		cur.execute (query)
		fetch = cur.fetchall()

		if ( len(fetch)>0 ):
			print("<meta http-equiv='refresh' content='0;http://127.0.0.1/hadoop/version.html'>")
		else:
			print("<meta http-equiv='refresh' content='0;http://127.0.0.1/hadoop/invalid.html'>")
 
	except:
		conn.rollback()
		print("oops..!!")		
