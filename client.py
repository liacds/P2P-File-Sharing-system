# made by Aliya Almas and Akzhan Suranshy
from socket import *
from gui import SearchBox
from gui import UploadFile
from gui import Results

def open_gui(clientSocket):
    try:
        from Tkinter import Tk
        from tkMessageBox import showinfo
    except ImportError:
            from tkinter import Tk
            from tkinter.messagebox import showinfo

    root = Tk()

    #SearchBox(root, placeholder="Type and press enter", entry_highlightthickness=0).pack(pady=10, padx=10)
    root.geometry("600x600")
    root.title("File sharing")
    upload = UploadFile(root, clientSocket, serverPort)
    upload.pack(pady=10, padx=10)

    
    #Results(root).pack(pady=10, padx=10)
    #file_info = upload.browse()
    # вот здесь короче будет 
    #  message = "<" + file_info + ">"
    # clientSocket.send(message)

    hostname = gethostname()
    ip_address = gethostbyname(hostname)
    print(ip_address)
    #message ="<"+file_info[0] + "," + file_info[1] +"," + str(file_info[2]) + "," + file_info[3] + "," +str(ip_address) +","+ str(serverPort)+ ">"

    #print(message)
    #print("\n")
    #clientSocket.send(message.encode())

    root.mainloop()


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
    open_gui(clientSocket)
else:
    print("здеся")
    close(clientSocket)



#ДАУНЛОУД 
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
while True:
    connectionSocket1, addr = serverSocket.accept()
    receivedMessage = connectionSocket1.recv(1024)
    encoding = 'utf-8'
    message = receivedMessage[0:].decode(encoding)
    if("DOWNLOAD" in message):
        message = message.split("DOWNLOAD:")[1]
        filename = message.split(",")[0]
        f = open(filename,'rb')
        l = f.read(1024)
        while (l):
            clientSocket.send(l)
            print('Sent ',repr(l))
            l = f.read(1024)
            f.close()





