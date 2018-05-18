#! /usr/bin/python2

import socket
import time

ip_addr = "192.168.43.89"
port_no = 7777

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind( (ip_addr,port_no) )

while True:
	data = s.recvfrom(100)
	print "Data is: ",data[0]
	print "Client's IP: ",data[1][0]
	rply = raw_input("Enter your reply: ")
	s.sendto(rply, (ip_addr,port_no) )
