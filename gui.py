try:
    from Tkinter import Entry, Frame, Label, StringVar, Listbox, Button
    from Tkconstants import *

except ImportError:
    from tkinter import Entry, Frame, Label, StringVar, Listbox, Button
    from tkinter.constants import *
    






class SearchBox(Frame):
    def __init__(self, master, entry_font=None, entry_background="white", entry_highlightthickness=1, button_ipadx=40, button_background="grey", button_foreground="white", button_font=None, opacity=0.8, placeholder=None, placeholder_font=None, placeholder_color="grey", spacing=3):
        Frame.__init__(self, master)
        
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

    root.geometry("500x500")
    root.title("File sharing")

    SearchBox(root, placeholder="Type and press enter", entry_highlightthickness=0).pack(pady=10, padx=10)
    Results(root).pack(pady=10, padx=10)
   
    root.mainloop()