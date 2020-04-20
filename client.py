# made by Aliya Almas and Akzhan Suranshy
from socket import *
serverName="servername"
serverPort = 9999
ip=199.11.11.11
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
message = "HELLO\r\n"
clientSocket.send(message)

receivedMessage = clientSocket.recv(1024)
if (receivedMessage == "HI\r\n"){
    message = ""
    clientSocket.send(message)
}
