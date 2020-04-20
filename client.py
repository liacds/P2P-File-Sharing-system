# made by Aliya Almas and Akzhan Suranshy
from socket import *
from gui import SearchBox
from gui import UploadFile
serverName='localhost'
serverPort = 9998
# ip=199.11.11.11
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
message = b"HELLO\r\n"
clientSocket.send(message)

receivedMessage = clientSocket.recv(1024)
encoding = 'utf-8'
rmsg=receivedMessage[0:].decode('ASCII')
print(rmsg)
print("\nStarting the share of files...\n ")

if (rmsg == "HI\r\n"):
    message = "%s",UploadFile.toClient()
    printf(message)
    messageb = b"%s",UploadFile.toClient()
    clientSocket.send(messageb)

