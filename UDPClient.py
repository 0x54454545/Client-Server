# coding: utf-8
from socket import *
serverName = 'LocalHost'
serverPort = 9999
clientSocket = socket(AF_INET, SOCK_DGRAM)
while 1:
	message = raw_input('Write a sentence:')
	clientSocket.sendto(message,(serverName, serverPort))
	x = raw_input ('Press 1 to print out sentence in lower case, 2 for upper case, 3 for reverse:')
	clientSocket.sendto(x,(serverName,serverPort))
	if x == 1:
			modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
			print modifiedMessage
	elif x == 2:
			modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
			print modifiedMessage	
	elif x == 3:
			modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
			print modifiedMessage	
clientSocket.close()