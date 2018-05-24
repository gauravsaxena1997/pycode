#!/usr/bin/python3.4

import sys
import time as t

#extracting src and destination file
files=sys.argv[0:3]

print (files[0])
#storing src file
src=files[1]

#storing destination file
dst=files[2]

f1=open(src,"r")
data=f1.read()
f1.close()

f2=open(dst,"w")
f2.write(data)
f2.close()

print ("coping data from"+src+" to "+dst+" ...!!")
