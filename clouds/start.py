#!/usr/bin/python

import os,commands,socket,time,sys

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s_ip=""
s_port=9999
s.bind((s_ip,s_port))

cdata=s.recvfrom(100)
cdata1=s.recvfrom(100)
if cdata[0]=='test' and cdata1[0]=='123' :
	s.sendto("ok", cdata[1])

