# coding: utf-8
#from socket import includes the python library
from socket import *
serverPort = 9999
#serverSocket creates UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "The server is ready to receive"

while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
	x, clientAddress = serverSocket.recvfrom(2048)
	if x == 1:
        	message, clientAddress = serverSocket.recvfrom(2048)
        	modifiedMessage = message.lower()
        	serverSocket.sendto(modifiedMessage, clientAddress)
	elif x == 2:
			message, clientAddress = serverSocket.recvfrom(2048)
			modifiedMessage = message.upper()
			serverSocket.sendto(modifiedMessage, clientAddress)
	elif x == 3:
			message, clientAddress = serverSocket.recvfrom(2048)
			modifiedMessage = message.join(reversed(string))
			serverSocket.sendto(modifiedMessage, clientAddress)
