# made by Aliya Almas and Akzhan Suranshy
from socket import *
from gui import SearchBox
from gui import UploadFile
from gui import Results

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
    message = "%s",UploadFile.toClient()
    print(message)
    messageb = b"%s",UploadFile.toClient()
    clientSocket.send(messageb)
    #giu(socket)

def gui():
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
    file_info = upload.browse()
    # вот здесь короче будет 
    #  message = "<" + file_info + ">"
    # clientSocket.send(message)
    SearchBox(root, placeholder="Type and press enter", entry_highlightthickness=0).pack(pady=10, padx=10)
    Results(root).pack(pady=10, padx=10)
    
    root.mainloop()

