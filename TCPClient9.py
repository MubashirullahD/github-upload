from socket import *
import time

serverIP = "127.0.0.1"
serverPort = 25010

clientSocket = socket(AF_INET, SOCK_STREAM) 

clientSocket.connect((serverIP,serverPort))


fileName = "C:\Users\Pavilion 15\OneDrive\Semester 5\Computer Networking\Lab\python code\small.mp4"
BUFFER_SIZE = 1024

mp3 = open(fileName, 'rb')
chunk = mp3.read(BUFFER_SIZE)

while chunk != "" :
    clientSocket.send(chunk)
    time.sleep(0.1)
    chunk = mp3.read(1024)
 
print "Transfer from client side complete." 
clientSocket.send("EOF")
mp3.close()
clientSocket.close()
