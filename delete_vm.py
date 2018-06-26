#! /usr/bin/python3.4

import os

for i in range(1,4):
	os.system('virsh destroy node'+str(i))
	os.system('virsh undefine node'+str(i)+' --remove-all-storage')
	os.system('rm /var/lib/libvirt/images/node'+str(i)+'.qcow2 ')
