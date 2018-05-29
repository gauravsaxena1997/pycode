#! /usr/bin/python3

import cgi
import subprocess as sb

#header information
print ("Content-type:text/html")
print ("")

web_data = cgi.FieldStorage()
out =  web_data.getvalue('x')
result = sb.getoutput(out)
print  ('<h4>')
print  ('<pre>')
print (result)
print  ('</pre>')                                                        #data of x variable in web_data is stored)
print  ('</h4>')
