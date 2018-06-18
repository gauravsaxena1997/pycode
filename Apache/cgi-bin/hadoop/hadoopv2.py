#! /usr/bin/python3

import cgi
import cgitb
import subprocess as sb
import time
import sys

cgitb.enable()

#header information
print ("Content-type:text/html")
print ("")

web_data = cgi.FieldStorage()
nodes =  web_data.getvalue('nodes')
ram =  web_data.getvalue('ram')
cpu =  web_data.getvalue('cpu')
service_type =  web_data.getvalue('service_type')

for i in range( 1, int(nodes)+1 ):
	#creating virtual machine
	create_vm = 'sudo qemu-img create -f qcow2 -b /var/lib/libvirt/images/cluster.qcow2 /var/lib/libvirt/images/node'+str(i)+'.qcow2'
	print ( sb.getoutput ( create_vm ) )

	# running virtual machine
	run_vm = 'sudo virt-install --ram ' +ram+ ' --vcpu '+cpu+' --disk path=/var/lib/libvirt/images/node'+str(i)+'.qcow2 --import --name node'+str(i)+' --noautoconsole'
	print ( sb.getoutput ( run_vm ) )
	# sys.stdout.write('something something something')
	# sys.stdout.flush()


time.sleep(5)
print('hbck')
# sys.stdout.write('sdvsd vvar er ')
# sys.stdout.flush()

time.sleep(2)
sys.stdout.write('sdvsd vvar er ')
sys.stdout.flush()


# ip = sb.getoutput(" nmap -n -sn 192.168.122.1/24 -oG - | awk '/Up$/{print $2}' ")
# ip_list = ip.split()
# print (ip_list)






# if (nodes == '2' and service_type == 'nm' ):
	
	