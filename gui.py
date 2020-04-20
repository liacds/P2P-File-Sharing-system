from tkinter import *

rootWindow = Tk()

rootWindow.geometry("300x300")
rootWindow.title("Hello World")

topFrame = Frame(rootWindow)
topFrame.pack(side=TOP)
bottomFrame = Frame(rootWindow)
bottomFrame.pack(side=BOTTOM)

rootWindow.mainloop()