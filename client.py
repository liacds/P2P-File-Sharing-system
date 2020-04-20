# made by Aliya Almas and Akzhan Suranshy
from socket import *
serverName='localhost'
serverPort = 9998
# ip=199.11.11.11
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
message = b"HELLO\r\n"
clientSocket.send(message)

receivedMessage = clientSocket.recv(1024)
encoding = 'utf-8'
lastchar3=receivedMessage[0:].decode('ASCII')
print(lastchar3)

if (receivedMessage == "HI\r\n"):
    message = "SEARCH + %s",gui.get_text()
    printf(message)
    clientSocket.send(message)

