#! /usr/bin/python3

import subprocess as sb
import time

ip = sb.getoutput(" nmap -n -sn 192.168.122.1/24 -oG - | awk '/Up$/{print $2}' ")
print (ip)
