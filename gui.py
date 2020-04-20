try:
    from Tkinter import Entry, Frame, Label, StringVar, ttk, filedialog
    from Tkconstants import *
except ImportError:
    from tkinter import Entry, Frame, Label, StringVar, ttk, filedialog
    from tkinter.constants import *






class SearchBox(Frame):
    def __init__(self, master, entry_width=30, entry_font=None, entry_background="white", entry_highlightthickness=1, button_ipadx=10, button_background="grey", button_foreground="white", button_font=None, opacity=0.8, placeholder=None, placeholder_font=None, placeholder_color="grey", spacing=3):
        Frame.__init__(self, master)
        
#browse button
        
        self.browse_button = Button(self, text="Browse a file",
                                    command=self.browse)
        self.browse_button.pack(fill=BOTH)
                                    
#-------------------------
        
        self.entry = Entry(self, width=entry_width, background=entry_background, highlightcolor=button_background, highlightthickness=entry_highlightthickness)
        self.entry.pack(side=LEFT, fill=BOTH, ipady=1, padx=(0,spacing))
        self._button_background = button_background

        self.button_label = Label(self, text="Search", background=button_background, foreground=button_foreground, font=button_font)
        if entry_font:
            self.button_label.configure(font=button_font)

        self.button_label.pack(side=LEFT, fill=Y, ipadx=button_ipadx)
        self.entry.bind("<Return>", self._on_execute_command)
        self.button_label.bind("<ButtonRelease-1>", self._on_execute_command)



#browse a file function
    def browse(self):
        browsedFile=filedialog.askopenfile(initialdir="/",title="select file", filetypes=(("text files", ".txt"),("all files","*.*")))
        print(browsedFile)
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



        
if __name__ == "__main__":
    try:
        from Tkinter import Tk
        from Tkinter import *
        from tkMessageBox import showinfo
    except ImportError:
        from tkinter import Tk
        from tkinter import *
        from tkinter.messagebox import showinfo

    def command(text):
        showinfo("search command", "searching:%s"%text)


    root = Tk()

    root.geometry("300x300")
    root.title("File sharing")
    SearchBox(root, placeholder="Type and press enter", entry_highlightthickness=0).pack(pady=10, padx=10)


    root.mainloop()
