from socket import *
import time


serverIP ='127.0.0.1'
serverPort =12000


clientSocket =socket(AF_INET,SOCK_STREAM)
message = raw_input("Input lowercase sentence:")


ticks1 = time.clock()
localtime1 = time.asctime( time.localtime(time.time()) )
print "Local current time when packet send :", localtime1


clientSocket.connect((serverIP,serverPort))
clientSocket.send(message)


modifiedMessage= clientSocket.recv(1024)


localtime2 = time.asctime( time.localtime(time.time()) )
print "Local current time when packet recieved:", localtime2
ticks2 = time.clock()


print modifiedMessage
print "Round Trip Time (RTT) of TCP is ", ticks2-ticks1     


clientSocket.close()                