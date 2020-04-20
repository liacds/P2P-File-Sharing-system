# made by Aliya Almas and Akzhan Suranshy
from _thread import *
from socket import *

def peerThread(connectionSocket):
     message = connectionSocket.recv(1024)

     encoding = 'utf-8'
     msg=message[0:].decode('ASCII')
     print(msg)

     if (msg=="HELLO\r\n"):
        response=b"HI\r\n"
        connectionSocket.send(response)

        print("What files would you like to share?\n")
     else:
        print("или здеся")
        connectionSocket.close()


     message2 = connectionSocket.recv(1024)
     encoding = 'utf-8'
     msg2=message2[0:].decode(encoding)

     print(msg2)
     filename = msg2.split(",")
     filename = filename[0].split('<')[1]
     print(filename)

     files[filename] = msg2
     #files[filename] = msg2
     #print(files)
     # filename = msg2.split(",")
     # print(filename)

     connectionSocket.close()




serverPort = 9998
serverHostname = gethostname()
serverIp = gethostbyname(serverHostname)

# files = {}

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
# serverSocket.connect((serverIp,serverPort))
serverSocket.listen(1)
print ('The server is ready to receive:')


while True:
    connectionSocket1, addr = serverSocket.accept()
    start_new_thread(peerThread ,(connectionSocket1,))
serverSocket.close()

