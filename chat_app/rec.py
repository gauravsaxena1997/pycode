#!/usr/bin/python3.4

import socket
import time
import threading as t

ip_addr = "127.0.0.1"
server_port = 9999

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind( (ip_addr,server_port) )

def receive():
	while True:
		data = s.recvfrom(100)
		print ("Data is: ",data[0].decode())
		print ("Client's IP: ",data[1][0])
		print ("Client's Port: ",data[1][1])

def send():	
	while True:
		rply = input("Enter your reply: ")
		encoded_msg = rply.encode()
		s.sendto(encoded_msg, ("127.0.0.1",8888) )
	


t._start_new_thread ( receive , () )
t._start_new_thread ( send , () )

while True:
	pass

