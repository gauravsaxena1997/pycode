#!/usr/bin/python3.4

import socket
import threading as t

ip_addr = "127.0.0.1"
port_no = 8888

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind( (ip_addr,port_no) )

def send():
	while True:
		msg = input("Enter your message: ")
		encoded_msg = msg.encode()
		s.sendto(encoded_msg, (ip_addr,9999) )
		

		data = s.recvfrom(100)
		print ("Data is: ",data[0].decode())


# def receive():
# 	while True:
		

t._start_new_thread ( send , () )
# t._start_new_thread ( receive , () )

while True:
	pass
