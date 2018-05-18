#! /usr/bin/python2

import socket
ip_addr = "192.168.43.89"
port_no = 7777

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
 
msg = raw_input("Enter your messege: ")


s.sendto(msg, (ip_addr,port_no) )
print s.recvfrom(100)

