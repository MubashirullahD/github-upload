from socket import *
import time

serverIP ='10.3.93.50'
serverPort =25000


clientSocket =socket(AF_INET,SOCK_DGRAM)
message = raw_input("Input lowercase sentence:")


start = time.clock()
localtime1 = time.asctime( time.localtime(time.time()) )
print "Local current time when packet send :", localtime1


clientSocket.sendto(message,(serverIP,serverPort))
modifiedMessage, serveraddress= clientSocket.recvfrom(2048)


localtime2 = time.asctime( time.localtime(time.time()) )
print "Local current time when packet recieved:", localtime2
stop = time.clock()


print modifiedMessage
print "Round Trip Time (RTT) of UDP is: ", stop - start   

clientSocket.close()