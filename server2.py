#second attempt 


from _thread import *
from socket import *

def peerThread(connectionSocket, addr):
     #print(clientPort)
     message = connectionSocket.recv(1024)
     encoding = 'utf-8'
     msg=message[0:].decode('ASCII')

    
     if (msg=="HELLO\r\n"):
        response=b"HI\r\n"
        connectionSocket.send(response)

        print("What files would you like to share?\n")
     else:
        print("Did not recieve HELLO")
        connectionSocket.close()

     while(True):
        message = connectionSocket.recv(1024)
        encoding = 'utf-8'
        msg=message[0:].decode('ASCII')

    #need to send "BROWSE"
        if (msg =="BROWSE\r\n"):
            print("browse recieved")
            message2 = connectionSocket.recv(1024)
            encoding = 'utf-8'
            msg2=message2[0:].decode(encoding)
            words = msg2.split(",")
            filename = words[0].split('<')[1]
            filename= filename.split(".")[0]
            msg2 = "<" + filename + "," + words[1] + "," + words[2] + "," + words[3] + "," + addr[0] + "," + str(addr[1])+">"
     #print(filename)
            if filename not in files:
                files[filename] = [msg2]
            else:
                files[filename].append(msg2)
    

        if "SEARCH:" in msg:
            
            filename = msg.split("SEARCH: ")[1]
            print("filename: to search for:" + filename)
            if filename:
                if filename in files:
                    response=b"FOUND\r\n"
                    connectionSocket.send(response)
               
                    number = len(files[filename])
                    number = str(number)
                    connectionSocket.send(number.encode())
                
                    for i in files[filename]:
                        response = i.encode()
                    #print(i)
                        connectionSocket.send(response)
                else:
                    response=b"NOT FOUND\r\n"
                    connectionSocket.send(response)

        if msg == "BYE":
            print("Client wants to leave")
            connectionSocket.close()
            break
        if not message:
            print("No Message Recieved")
            break



     connectionSocket.close()




serverPort = 9999
serverHostname = 'localhost'

files = {}

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive:')


while True:
    connectionSocket1, addr = serverSocket.accept()
    start_new_thread(peerThread ,(connectionSocket1,addr))
serverSocket.close()
