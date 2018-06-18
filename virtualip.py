import socket
import subprocess

ip_range = '192.168.122.1/24'
ip = subprocess.getoutput('nmap -sn -n ' + ip_range)
print (ip)
addresses = list()
all_ip = list()

for line in fhand:
#	print(line)
	line = line.strip()
	if line.startswith("Nmap scan report for"):
		addresses.append(line)		

for ip in addresses:
	ip_number = ip.split()
	final = ip_number[-1]
	all_ip.append(final)

print(all_ip)

subprocess.getoutput('rm -f iptest.txt')
