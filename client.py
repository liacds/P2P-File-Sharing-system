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

    root.geometry("600x600")
    root.title("File sharing")
    upload = UploadFile(root)
    upload.pack(pady=10, padx=10)

    SearchBox(root, placeholder="Type and press enter", entry_highlightthickness=0).pack(pady=10, padx=10)
    Results(root).pack(pady=10, padx=10)
    file_info = upload.browse()
    # вот здесь короче будет 
    #  message = "<" + file_info + ">"
    # clientSocket.send(message)

    message ="<"+file_info[0] + "," + file_info[1] +"," + str(file_info[2]) + "," + file_info[3] + ">"
    
    print("this is my file_info ")
    print(message)
    print("\n")
    clientSocket.send(message.encode())
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
    close(clientSocket)





