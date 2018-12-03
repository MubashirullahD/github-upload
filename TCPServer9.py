from socket import *
import time

serverPort = 25010

serverSocket = socket(AF_INET,SOCK_STREAM) 

serverSocket.bind(('',serverPort)) 
serverSocket.listen(1)

print "The server is ready"

location = "C:\Users\Pavilion 15\Downloads" 
Name = location + '\\' + "small.mp4" 

File = open(Name,'wb') 

print "The server is ready to receive"
while 1:
    connectionSocket, addr = serverSocket.accept() 
    data = connectionSocket.recv(1024)
    time.sleep(0.1)
    if data == "EOF":
        break
    File.write(data)
    connectionSocket.close()

connectionSocket.close()
File.close()
serverSocket.close()
