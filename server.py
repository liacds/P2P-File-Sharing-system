# made by Aliya Almas and Akzhan Suranshy
from socket import *
serverPort = 9998
# ip=198.11.11.11
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive:')

while True:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024)
    
    #    print (message,'::',message.split()[0],':',message.split()[1])
#    filename = message.split()[1]
#    print (filename,'||',filename[1:])
#    encoding = 'utf-8'
#    lastchar3=filename[-3:].decode('ASCII')
#    lastchar4=filename[-4:].decode('ASCII')

    if (message=="HELLO\r\n"):
        response="HI"
        connectionSocket.send(response)


    filename = message.split()[0]
    print (filename,'||',filename[1:])
    encoding = 'utf-8'
    lastchar3=filename[0:].decode('ASCII')
    print(lastchar3)


#     try:
#         f=open(filename[1:], "r+b")
#         f.close()
#
#     except IOError:
#         print("You are not sharing files, sorry BYE!!!\n")
#         connectionSocket.send("HTTP/1.1 404 Not Found  \r\n\r\n 404 Not Found".encode())
#         connectionSocket.close()
#         break

#     firstPart=message.split()[0]
#     if(firstPart=="SEARCH"):
        



#    if (lastchar3=="jpg" or lastchar4=="jpeg"):
#
#        try:
#            f=open(filename[1:], "r+b")
#            data = f.read()
#            f.close()
#            HTTP_RESPONSE = b'\r\n'.join([
#                              b"HTTP/1.1 200 OK",
#                              b"Connection: close",
#                              b"Content-Type: image/jpg",
#                              bytes("Content-Length: %s" % len(data),'utf-8'),
#                              b'', data
#                              ] )
#            print(HTTP_RESPONSE)
#            connectionSocket.sendall(HTTP_RESPONSE)
#            break
#
#
#
#        except IOError:
#            print("404 Not Found")
#            connectionSocket.send("HTTP/1.1 404 Not Found  \r\n\r\n 404 Not Found".encode())
#            break
#    else:
#        try:
#            f = open(filename[1:])
#            outputdata = f.read()
#            f.close()
#            print (outputdata)
#            HTTP_RESPONSE = b'\r\n'.join([
#                                          b"HTTP/1.1 200 OK",
#                                          b"Connection: close",
#                                          b"Content-Type: text/txt/html",
#                                          bytes("Content-Length: %s" % len(outputdata),'utf-8'),
#                                          b'', str.encode(outputdata)
#                                          ] )
#            print(HTTP_RESPONSE)
#            connectionSocket.send("HTTP/1.1 200 OK  \r\n\r\n 200 OK\n".encode())
#            connectionSocket.send(str.encode(outputdata))
#            connectionSocket.close()
#            break
#
#        except IOError:
#            print("404 Not Found")
#            connectionSocket.send("HTTP/1.1 404 Not Found  \r\n\r\n 404 Not Found".encode())
#            break
