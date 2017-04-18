import tkinter as tk
import time
from tkinter import *

class ChatRoom(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.minsize(825, 825)

        #UPPER CONTAINER
        self.uframe = tk.Frame(self, bg="#C0C0C0", relief=SUNKEN, borderwidth=2)
        self.uframe.place(x=25, y=25, width=775, height=100)
        
        self.entry1 = tk.Entry(self.uframe, bd=3)
        self.entry1.place(x=10, y=50)

        self.label1 = tk.Label(self.uframe, text="User Name : ", bg="#C0C0C0")
        self.label1.place(x=10, y=25)
        
        self.button1 = tk.Button(self.uframe, text="Enter", command=self.buttonpress1)
        self.button1.place(x=150, y=50)
        
        #LEFT CONTAINER
        self.lframe = tk.Frame(self, bg="#C0C0C0", relief=SUNKEN, borderwidth=2)
        self.lframe.place(x=25, y=150, width=150, height=650)

        #MIDDLE CONTAINER
        self.mframe = tk.Frame(self, bg="#C0C0C0", relief=SUNKEN, borderwidth=2)
        self.mframe.place(x=200, y=150, width=600, height=525)

        self.textbox = tk.Text(self.mframe)
        self.textbox.place(x=0, y=0, width=577, height=520)
        self.textbox.config(state=DISABLED)

        self.scroll = tk.Scrollbar(self.mframe)
        self.scroll.pack(side=RIGHT, fill=Y)

        self.textbox.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.textbox.yview)
        
        #BOTTOM CONTAINER
        self.bframe = tk.Frame(self, bg="#C0C0C0", relief=SUNKEN, borderwidth=2)
        self.bframe.place(x=200, y=700, width=600, height=100)
        
        self.entry2 = tk.Entry(self.bframe, bd=3, width=85)
        self.entry2.place(x=20, y=20)

        self.button2 = tk.Button(self.bframe, text="Send", command=self.buttonpress2)
        self.button2.place(x=550, y=20)

        #VARIABLES
        self.T = ""
        self.U = ""
        self.TB = 0
        self.UB = 0
        
        self.update()
             
    def display_message(self,S,U):
        now = time.strftime("%H:%M:%S" , time.gmtime())
        M = now + " " + U + " : " + S + "\n"
        self.textbox.config(state=NORMAL)
        self.textbox.insert(END, M)
        self.textbox.config(state=DISABLED)
        self.update()
        #Recieve S and U from controller to display message

    def buttonpress1(self):
        self.U = self.entry1.get()
        self.UB = 1
        self.entry1.delete(0, END)
        
    def buttonpress2(self):
        self.T = self.entry2.get()
        self.TB = 1
        self.entry2.delete(0, END)

        

        
    
