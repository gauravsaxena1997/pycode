#! /usr/bin/python3

import cgi
import cgitb
import subprocess as sb
# import mysql.connector as pysql

cgitb.enable()

#header information
print ("Content-type:text/html") 
print ("") 

web_data = cgi.FieldStorage()
dn =  web_data.getvalue('no')


for i in range( 1, int(dn)+1 ):
	print ('Creating data node '+ str(i) + '....!!')
	print ('</br>')
	#creating virtual machine
	create_vm = 'sudo qemu-img create -f qcow2 -b /var/lib/libvirt/images/rhvmdnd.qcow2 /var/lib/libvirt/images/gurvdn'+str(i)+'.qcow2'
	print ( sb.getoutput ( create_vm ) )
	print ('</br>')

	running virtual machine
	print ('Installing virtual machine...')
	run_vm = 'sudo virt-install --ram 512 --vcpu 1 --disk path=/var/lib/libvirt/images/gurvdn'+str(i)+'.qcow2 --import --name datanode'+str(i)+' --noautoconsole'
	print ( sb.getoutput ( run_vm ) )

