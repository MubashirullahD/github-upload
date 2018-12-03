from socket import *

#use the IP address of your neighbor running the server
serverName="127.0.0.1"
serverPort=55001

clientSocket = socket(AF_INET,SOCK_DGRAM)

#use your name here
message="Kaleem Ullah"


clientSocket.sendto(message,(serverName,serverPort)) 

modifiedMessage,serverAddress=clientSocket.recvfrom(2048)


print "received from"
for n in serverAddress:
	print n 
print modifiedMessage

clientSocket.close()


