#!/usr/bin/python3.4
import subprocess as sb 


vm_list = sb.getoutput ('virsh list | grep -vi Id | grep -vi - | cut -d " " -f7')

vm = vm_list.split()

for i in vm:
	print (i)