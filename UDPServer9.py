from socket import *
 
serverIP = "127.0.0.1"
serverPort = 25006

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverIP,serverPort))

print "The server is ready"

location = "C:\Users\Pavilion 15\Downloads" 
Name = location + '\\' + "lab9.txt" 

File = open(Name,'w') 

while True :
    message, clientAddress = serverSocket.recvfrom(2048) 
    if message == "EOF":
        break
    File.write(message)
    
print "File transfer complete on server side"
File.close()
serverSocket.close()