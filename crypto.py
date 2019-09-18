import socket
import subprocess as sp
import pyttsx3
s=socket.socket()
#s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
port= 1234
ip= "192.168.43.254"

s.bind((ip,port))
s.listen()

cl,addr= s.accept()
voice=pyttsx3.init()
voice.setProperty('rate',150)
while True:
	data=cl.recv(1024)
	talk=data.decode()
	voice.say(talk)
	voice.runAndWait()
  #	if talk==0:
  #		break

