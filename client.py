# made by Aliya Almas and Akzhan Suranshy
from socket import *
from gui import SearchBox
from gui import UploadFile
from gui import Results
from threading import Thread

def open_gui(clientSocket,main_client_socket_port,main_client_socket_ip,main_client_socket):
    try:
        from Tkinter import Tk
        from tkMessageBox import showinfo
    except ImportError:
            from tkinter import Tk
            from tkinter.messagebox import showinfo

    root = Tk()

    root.geometry("600x600")
    root.title("File sharing")
    upload = UploadFile(root, clientSocket, serverPort, main_client_socket_port, main_client_socket_ip)
    upload.pack(pady=10, padx=10)

     # start_new_thread(peerClientThread ,(clientSocket,))
    thread = Thread(target = peerClientThread, args = (clientSocket,main_client_socket_port,main_client_socket_ip,main_client_socket ))
    thread.start()
#     root.after_idle(peerClientThread(clientSocket,main_client_socket_port,main_client_socket_ip,main_client_socket))
#     root.after_idle(thread.join())
#     thread.join()

    root.mainloop()

def peerClientThread(clientSocket,main_client_socket_port,main_client_socket_ip,main_client_socket):
    print("Client is in thread")

    while main_client_socket:
        conn, addr = main_client_socket.accept()
        message = conn.recv(1024)
        encoding = 'utf-8'
        rmsg=message[0:].decode(encoding)
        if("DOWNLOAD" in rmsg):

            print("sending the file ")
            message = rmsg.split("DOWNLOAD: ")[1]
            filename = message.split(",")[0]
            filetype=message.split(",")[1]
            file=filename+"."+filetype
            f = open(file,'rb')
            l = f.read(1024)
            while (l):
                conn.send(l)
                print('Sent ',repr(l))
                l = f.read(1024)
                f.close()

#             m="SENDING"
#             conn.send(m.encode())
#             checkMessage =conn.recv(1024)
#             encoding = 'utf-8'
#             cmsg=checkMessage[0:].decode(encoding)
#             print(cmsg)
#             if ("WAITING" == cmsg):
#                 message = rmsg.split("DOWNLOAD: ")[1]
#                 filename = message.split(",")[0]
#                 filetype=message.split(",")[1]
#                 file=filename+"."+filetype
#                 f = open(filename,'rb')
#                 l = f.read(1024)
#                 while (l):
#                     conn.send(l)
#                     print('Sent ',repr(l))
#                     l = f.read(1024)
#                     f.close()

        else:
            print("здеся download ne rabotaet ")





#client as a listener
main_client_socket = socket(AF_INET, SOCK_STREAM)
main_client_socket.bind(('127.0.0.1', 0))
main_client_socket.listen(1)
main_client_socket_port = main_client_socket.getsockname()[1]
main_client_socket_ip = main_client_socket.getsockname()[0]
print(main_client_socket_port)
print(main_client_socket_ip)


serverName='localhost'
serverPort = 9999

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
print("Client is ready to send")
message = b"HELLO\r\n"
clientSocket.send(message)

receivedMessage = clientSocket.recv(1024)
encoding = 'utf-8'
rmsg=receivedMessage[0:].decode('ASCII')
print(rmsg)


if (rmsg == "HI\r\n"):
    open_gui(clientSocket,main_client_socket_port,main_client_socket_ip, main_client_socket)
else:
    print("здеся")
    close(clientSocket)


