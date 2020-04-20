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

#     filename = msg2.split(",")[0]
#     print(filename)
    

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
