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
out =  web_data.getvalue('x')

conn = pysql.connect(user='root',password='m487',host='localhost')

def db():
	if ( conn.is_connected() ):
		print ('Database connected successfully...')
		cur = conn.cursor()

		cur.execute ("""create database if not exists pytest""")

		cur.execute ("use pytest")

		cur.execute ("""create table if not exists onecol (  
						value INT(5) NOT NULL PRIMARY KEY  )""")

		value = ("INSERT INTO onecol "
	             "(value) "
	             "VALUES (%s)" % (out) )
		try:
			cur.execute (value)
			conn.commit()

		except:
			print ('</br>')
			print ("Duplicate entry detected...")
			conn.rollback()
	else:
		print ('Something went wrong...')


if __name__ == "__main__":
	db()

# print  ('<h4>')
# print  ('<pre>')
# print (result)
# print  ('</pre>')                                                        #data of x variable in web_data is stored)
# print  ('</h4>')
