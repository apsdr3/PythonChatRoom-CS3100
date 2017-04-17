import tkinter as tk
import time
from tkinter import *

class ChatRoom(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.uframe = tk.Frame(self)
        self.uframe.place(x=25, y=25, width=775, height=100)
        self.mframe = tk.Frame(self)
        self.mframe.place(x=200, y=150, width=600, height=525)
        self.label1 = tk.Label(self.uframe, text="User Name : ")
        self.label1.place(x=0, y=25)
        self.label2 = tk.Label(self.mframe, text="CHAT")
        self.label2.place(x=10, y=0)
        self.entry1 = tk.Entry(self.uframe, bd=3)
        self.entry1.place(x=0, y=50)
        self.scroll = tk.Scrollbar(self.mframe)
        self.scroll.pack(side = RIGHT, fill=Y)

        self.yval = 25
        
        self.update("Hello World! Welcome to the chatroom!", "CHATROOM")
    
    def update(self,S,U):
        now = time.strftime("%H:%M:%S" , time.gmtime())
        M = now + " " + U + " : " + S + "\n"
        self.message = tk.Message(self.mframe, text=M, relief=RAISED, width=580, anchor=W)
        self.message.place(x=0, y=self.yval, width=580, height=50) 
        self.yval=self.yval+50
    
if __name__== "__main__":
    C = ChatRoom()
    C.mainloop()

