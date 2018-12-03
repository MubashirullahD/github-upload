from socket import *

serverIP = "127.0.0.1"
serverPort = 25006

clientSocket = socket(AF_INET, SOCK_DGRAM)


fileName = "C:\Python27\README.txt"
BUFFER_SIZE = 1024


ebook = open(fileName, 'r')
chunk = ebook.read(BUFFER_SIZE)

while chunk != "" :
    clientSocket.sendto(chunk,(serverIP,serverPort))
    chunk = ebook.read(1024)


clientSocket.sendto("EOF",(serverIP,serverPort))
ebook.close()

print "File transfer complete from the client side."
clientSocket.close()