# made by Aliya Almas and Akzhan Suranshy
from socket import *
serverPort = 9999
files = {}
# ip=198.11.11.11
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive:')


while True:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024)

    encoding = 'utf-8'
    msg=message[0:].decode('ASCII')
    print(msg)

    if (msg=="HELLO\r\n"):
        response=b"HI\r\n"
        connectionSocket.send(response)

        print("What files would you like to share?\n")
    else:
         connectionSocket.close()
         break

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
    

