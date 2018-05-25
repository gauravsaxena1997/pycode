#!/usr/bin/python3.4

import socket
import time
import threading as t

ip_addr = "192.168.10.72"
server_port = 9999

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind( (ip_addr,server_port) )

bind = { 'client_ip': "" ,'client_port': 0 }

print (bind)
print (bind['client_ip'])
print (bind['client_port'])


# def mainfunc():
# 	global client_ip
# 	global client_port

def receive():
	while True:
		data = s.recvfrom(100)
		print ("Data is: ",data[0].decode())
		print ("Client's IP: ",data[1][0])
		print ("Client's Port: ",data[1][1])
		bind['client_ip'] = data[1][0]
		#print ( type(client_ip) )
		bind['client_port'] = int(data[1][1])
		#print ( type(client_port) )

print (bind)
print (bind['client_ip'])
print (bind['client_port'])
def send():	
	while True:
		rply = input("Enter your reply: ")
		encoded_msg = rply.encode()
		print (client_ip)
		print (client_port)
		s.sendto(encoded_msg, (client_ip,client_port) )
	

t._start_new_thread ( receive , () )
t._start_new_thread ( send , () )

while True:
	pass

