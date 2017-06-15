#!/usr/bin/python
import os,commands,socket,time,sys

x="""
Press 1 to get firefox  
Press 2 to get vlc 
Press 3 to get calculator 
Press 4 to get office 
Press 5 to get screenshot 
Press 6 to get webcam 
Press 7 to get gedit
Press 8 to get imageviewer
"""
print x
ch=raw_input("Enter your choice : ")

if ch=="1" :
	print "Wait few seconds"
	time.sleep(2)
	execfile('firefox.py')
elif ch=="2" :
	print "Wait few seconds"
        time.sleep(2)
        execfile('vlc.py')
elif ch=="3" :
	print "Wait few seconds"
        time.sleep(2)
        execfile('calculator.py')
elif ch=="4" :
	print "Wait few seconds"
        time.sleep(2)
        execfile('office.py')
elif ch=="5" :
	print "Wait few seconds"
        time.sleep(2)
        execfile('screenshot.py')
elif ch=="6" :
	print "Wait few seconds"
        time.sleep(2)
        execfile('webcam.py')
elif ch=="7" :
	print "Wait few seconds"
        time.sleep(2)
        execfile('gedit.py')
elif ch=="8" :
	print "Wait few seconds"
        time.sleep(2)
        execfile('imageviewer.py')
else :
	print "Wrong choice.."

