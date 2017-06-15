#!/usr/bin/python
import os,commands,socket,time,sys,getpass
s_ip="192.168.122.79"
os.system('sshpass -p "123" ssh -X test@'+s_ip+' libreoffice')
time.sleep(2)

execfile('saas.py')

