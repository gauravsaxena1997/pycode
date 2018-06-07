#! /usr/bin/python3

import subprocess as sb

all_files = sb.getoutput ('hadoop fs -ls / | cut -d "/" -f2 | grep -vi Found')

directories = all_files.split()

for files in directories:
	print ('cleaning /'+files+' ...')
	sb.getoutput ('hadoop fs -rmr /'+files)

print ('%---Whole cluster clear---%')
