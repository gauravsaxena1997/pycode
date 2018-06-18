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
name =  web_data.getvalue('name')
email =  web_data.getvalue('email')
contact =  int(web_data.getvalue('contact'))
password =  web_data.getvalue('password')

conn = pysql.connect(user='root',password='m487',host='localhost')


if ( conn.is_connected() ):
	print ('Database connected successfully...')
	cur = conn.cursor()

	cur.execute ("""create database if not exists hadoop""")
	cur.execute ("use hadoop")
	cur.execute ("""create table if not exists signup (  
					name CHAR(20) NOT NULL,
					email CHAR(30) NOT NULL PRIMARY KEY,
					contact BIGINT UNSIGNED NOT NULL,
					password CHAR(15) NOT NULL )""")
	
	query = ("INSERT INTO signup "
          "(name, email, contact, password) "
          "VALUES ('%s','%s','%d','%s')" % (name, email, contact, password) )
	
	try:
		cur.execute(query)
		conn.commit()
		print ("<meta http-equiv='refresh' content='0;http://127.0.0.1/hadoop/index.html'>")
	
	except:
		conn.rollback()
		print('</br>')
		print("oops..!!")

else:
	print ('Something went wrong...')
