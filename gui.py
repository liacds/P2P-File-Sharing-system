try:
    from Tkinter import Entry, Frame, Label, StringVar, Listbox, Button, filedialog
    from Tkconstants import *

except ImportError:
    from tkinter import Entry, Frame, Label, StringVar, Listbox, Button, filedialog
    from tkinter.constants import *
    
import os 
import datetime
from socket import *


class SearchBox(Frame):

    def __init__(self, master, clientSocket, serverPort, entry_font=None, entry_background="white", entry_highlightthickness=1, button_ipadx=40, button_background="grey", button_foreground="white", button_font=None, opacity=0.8, placeholder=None, placeholder_font=None, placeholder_color="grey", spacing=3):
        Frame.__init__(self, master)
        
        self.clientSocket = clientSocket
        self.label = Label(self, text = "File Name")
        self.label.pack(side= LEFT,fill=BOTH, ipady=1, padx=(0,spacing))
        self.entry = Entry(self, width=50, background=entry_background, highlightcolor=button_background, highlightthickness=entry_highlightthickness)
        self.entry.pack(side=LEFT, fill=BOTH, ipady=1, padx=(0,spacing))
        self.serverPort = serverPort
        self._button_background = button_background
        self.button_label = Label(self, text="Search", background=button_background, foreground=button_foreground, font=button_font)
        if entry_font:
            self.button_label.configure(font=button_font)
            
        self.button_label.pack(side=LEFT, fill=Y, ipadx=button_ipadx)
        self.entry.bind("<Return>", self._on_execute_command)
        self.button_label.bind("<ButtonRelease-1>", self._on_execute_command)


    def get_text(self):
        entry = self.entry
        if hasattr(entry, "placeholder_state"):
            if entry.placeholder_state.contains_placeholder:
                return ""
            else:
                return entry.get()
        else:
            return entry.get()

        

    def _on_execute_command(self, event):
        print("nothing yet")
        #print(self.get_text())
        message="SEARCH: "+self.get_text()
        print(message)
        self.clientSocket.send(message.encode())

        #wait for found or not found
        receivedMessage =self.clientSocket.recv(1024)
        encoding = 'utf-8'
        rmsg=receivedMessage[0:].decode(encoding)
        print(rmsg)

        if (rmsg=="FOUND\r\n"):
        #how many values for same key there are
            numOfValuesInBytes=self.clientSocket.recv(1024)
            encoding = 'utf-8'
            numOfValuesInStr=numOfValuesInBytes[0:].decode(encoding)
            numOfValues=int(numOfValuesInStr.split("<")[0])
        #loop through values and choose the one the client want to connect to and open new socket with a peer
            files=[]
            for i in range(numOfValues):
                receivedMessage=self.clientSocket.recv(1024)
                encoding = 'utf-8'
                rfiles=receivedMessage[0:].decode(encoding)
                files.append(rfiles)
                print(rfiles)
            print(files)

            Results(self.master, self.clientSocket, self.serverPort, files).pack(pady=10, padx=10)
        if (rmsg=="NOT FOUND\r\n"):
            msg="BYE\r\n"
            self.clientSocket.send(msg.encode())
            Label(self, text = "No Files found").pack()






class Results(Frame):

     def __init__(self, master, clientSocket, serverPort, files):
        Frame.__init__(self, master)
        DAYS = files 
        
        self.list = Listbox(self, width = 50, background = "white")  
        self.list.insert(0, *DAYS) 
        self.print_btn = Button(self, text="Download", 
                                   command=self.print_selection) 
        
 
        self.list.pack() 
        self.print_btn.pack(fill=BOTH)   

     def print_selection(self): 
        selection = self.list.curselection() 
        #print([self.list.get(i) for i in selection]) 

        
class UploadFile(Frame):
    def __init__(self, master, clientSocket, serverPort):
        Frame.__init__(self, master)
        self.label = Label(self, text = "Browse Files (up to 5)")
        self.label.pack(side= LEFT,fill=BOTH, ipady=1, padx=(0,3))
        self.browse_button = Button(self, text="Browse a file", command=self.browse)
        self.browse_button.pack(fill=BOTH)
        self.clientSocket = clientSocket
        self.serverPort = serverPort

    def browse(self):

        browsedFile=filedialog.askopenfile(initialdir="/",title="select file", filetypes=(("text files", ".txt"),("all files","*.*")))
        path = browsedFile.name
        
        modTimesinceEpoc = os.path.getmtime(path)
        modificationTime = datetime.datetime.fromtimestamp(modTimesinceEpoc).strftime('%Y-%m-%d')
        file_size = os.path.getsize(path)
        all_file = path.split("/")
        file_name = all_file[-1]
        file_type = file_name.split(".")[-1] 
        hostname = gethostname()
        ip_address = gethostbyname(hostname)
        file_name= file_name.split(".")[0]
        message = "<" + file_name+"," +file_type + "," + str(file_size) + "," + modificationTime + "," +str(ip_address) + "," + str(self.serverPort) + ">" 
        print(message + " lalallalallala")
        
        SearchBox(self.master, self.clientSocket, self.serverPort, placeholder="Type and press enter", entry_highlightthickness=0).pack(pady=10, padx=10)
        

        self.clientSocket.send(message.encode())
        

    

    
        
# if __name__ == "__main__":
#     try:
#         from Tkinter import Tk
#         from tkMessageBox import showinfo
#     except ImportError:
#             from tkinter import Tk
#             from tkinter.messagebox import showinfo

#     root = Tk()

#     root.geometry("600x600")
#     root.title("File sharing")
#     upload = UploadFile(root)
#     upload.pack(pady=10, padx=10)
#     file_info = upload.browse()
#     SearchBox(root, placeholder="Type and press enter", entry_highlightthickness=0).pack(pady=10, padx=10)
#     Results(root).pack(pady=10, padx=10)
    
#     root.mainloop()