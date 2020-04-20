try:
    from Tkinter import Entry, Frame, Label, StringVar, Listbox, Button, filedialog
    from Tkconstants import *

except ImportError:
    from tkinter import Entry, Frame, Label, StringVar, Listbox, Button, filedialog
    from tkinter.constants import *
    
import os 
import datetime





class SearchBox(Frame):

    def __init__(self, master, entry_font=None, entry_background="white", entry_highlightthickness=1, button_ipadx=40, button_background="grey", button_foreground="white", button_font=None, opacity=0.8, placeholder=None, placeholder_font=None, placeholder_color="grey", spacing=3):
        Frame.__init__(self, master)


        
        #browse button
        
        #-------------------------
        self.label = Label(self, text = "File Name")
        self.label.pack(side= LEFT,fill=BOTH, ipady=1, padx=(0,spacing))
        self.entry = Entry(self, width=50, background=entry_background, highlightcolor=button_background, highlightthickness=entry_highlightthickness)
        self.entry.pack(side=LEFT, fill=BOTH, ipady=1, padx=(0,spacing))

        self._button_background = button_background
        self.button_label = Label(self, text="Search", background=button_background, foreground=button_foreground, font=button_font)
        if entry_font:
            self.button_label.configure(font=button_font)
            
        self.button_label.pack(side=LEFT, fill=Y, ipadx=button_ipadx)
        self.entry.bind("<Return>", self._on_execute_command)
        self.button_label.bind("<ButtonRelease-1>", self._on_execute_command)

    #browse a file function
    
    #---------------------------

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
        print(self.get_text())






class Results(Frame):

     def __init__(self, master):
        Frame.__init__(self, master)
        DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", 
        "Friday", "Saturday", "Sunday"] 
        
        self.list = Listbox(self, width = 50, background = "white")  
        self.list.insert(0, *DAYS) 
        self.print_btn = Button(self, text="Download", 
                                   command=self.print_selection) 
        
 
        self.list.pack() 
        self.print_btn.pack(fill=BOTH)   

     def print_selection(self): 
        selection = self.list.curselection() 
        print([self.list.get(i) for i in selection]) 

        
class UploadFile(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, text = "Browse Files (up to 5)")
        self.label.pack(side= LEFT,fill=BOTH, ipady=1, padx=(0,3))
        self.browse_button = Button(self, text="Browse a file", command=self.browse)
        self.browse_button.pack(fill=BOTH)

    def browse(self):

        browsedFile=filedialog.askopenfile(initialdir="/",title="select file", filetypes=(("text files", ".txt"),("all files","*.*")))
        print(browsedFile.name)
        path = browsedFile.name
        
        modTimesinceEpoc = os.path.getmtime(path)
        modificationTime = datetime.datetime.fromtimestamp(modTimesinceEpoc).strftime('%Y-%m-%d')
        file_size = os.path.getsize(path)
        all_file = path.split("/")
        file_name = all_file[-1]
        file_type = file_name.split(".")[-1]
        print(modificationTime)
        print(file_size)
        print(file_name)
        print(file_type)
        return [file_name, file_type, file_size, modificationTime]

  
        
if __name__ == "__main__":
    try:
        from Tkinter import Tk
        from tkMessageBox import showinfo
    except ImportError:
        from tkinter import Tk
        from tkinter.messagebox import showinfo

    def command(text):
        showinfo("search command", "searching:%s"%text)

    root = Tk()

    root.geometry("600x600")
    root.title("File sharing")
    UploadFile(root).pack(pady=10, padx=10)
    SearchBox(root, placeholder="Type and press enter", entry_highlightthickness=0).pack(pady=10, padx=10)
    Results(root).pack(pady=10, padx=10)
    
    root.mainloop()