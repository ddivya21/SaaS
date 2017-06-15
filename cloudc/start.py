#!/usr/bin/python
import os,commands,socket,time,sys,getpass

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s_ip="192.168.122.79"
s_port=9999

print "Enter authentication details :"
s_user=raw_input("Enter user name : ")
s_password=getpass.getpass()

s.sendto(s_user,(s_ip,s_port))
s.sendto(s_password,(s_ip,s_port))

sdata=s.recvfrom(2)
if sdata[0]=="ok" :
	print "Authentication Successful !!"
	print "Services Loading..."
	time.sleep(3)
	execfile('saas.py')
else:
	print "Check user and password.."
