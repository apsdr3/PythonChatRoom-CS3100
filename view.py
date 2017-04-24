import tkinter as tk
import time
from tkinter import *

class ChatRoom(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.minsize(825, 825)
        self.title("Chat Room - Client 2")

        #UPPER CONTAINER
        self.uframe = tk.Frame(self, bg="#C0C0C0", relief=SUNKEN, borderwidth=2)
        self.uframe.place(x=25, y=25, width=775, height=100)
        
        """        
        self.entry1 = tk.Entry(self.uframe, bd=3)
        self.entry1.place(x=10, y=50)

        self.label1 = tk.Label(self.uframe, text="User Name : ", bg="#C0C0C0")
        self.label1.place(x=10, y=25)
        
        self.button1 = tk.Button(self.uframe, text="Enter", command=self.buttonpress1)
        self.button1.place(x=150, y=50)
        """
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

        self.entry2.bind('<Return>', self.buttonpress2)

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
        
    def buttonpress2(self, event = None):
        self.T = self.entry2.get()
        self.TB = 1
        self.entry2.delete(0, END)


"""
Login Window
"""
class Login(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        def setColor(event):
            if (self.focus_get() == userInput):
                line.configure(bg="black")
            if (self.focus_get() == passInput):
                line2.configure(bg="black")

        def resetColor(event):
            if (self.focus_get() != userInput):
                line.configure(bg="grey")
            if (self.focus_get() != passInput):
                line2.configure(bg="grey")

        def setLine(event):
            line3.configure(bg="black")

        def resetLine(event):
            line3.configure(bg="#F0F0F0")

        def setSubmitColor(event):
            submit.configure(bg="#B31E1E")

        def resetSubmitColor(event):
            submit.configure(bg="#e62727")

        def Register_toggle(event):
            # switching to registration
            if (welcome.cget("text") == "Please Log In"):
                welcome.configure(text="Please Register")
                submit.configure(text="Register", padx=140)
                needAcc.configure(text="Have an account?")
                register.configure(text="Log In")
                line3.configure(width=35)
                self.password.configure(text="Password:", fg="black")
            else:
                welcome.configure(text="Please Log In")
                submit.configure(text="Login", padx=150)
                needAcc.configure(text="Need an account?")
                register.configure(text="Register")
                line3.configure(width=46)
                self.password.configure(text="Password:", fg="black")

        def on_click():
            self.login = 1
            self.u = userInput.get()
            self.p = passInput.get()

        #Main Window
        self.title("Login")
        self.login = 0
        self.u = ""
        self.p = ""

        w = 400  # width for the Tk self
        h = 425  # height for the Tk self

        # get screen width and height
        ws = self.winfo_screenwidth()  # width of the screen
        hs = self.winfo_screenheight()  # height of the screen

        #centering the window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Welcome Label
        welcome = tk.Label(self, text="Please Log In", font="Sans/Serif 15 bold")
        welcome.place(x=130, y=20)

        # Username Label
        username = tk.Label(self, text="Username:", font="Sans/Serif 9")
        username.place(x=30, y=70)

        # Password Label
        self.password = tk.Label(self, text="Password:", font="Sans/Serif 9")
        self.password.place(x=30, y=153)

        # NeedanAccount Label
        needAcc = tk.Label(self, text="Need an account?", font="Sans/Serif 9")
        needAcc.place(x=30, y=380)

        # Register/Button
        register = tk.Label(self, text="Register", font="Sans/Serif 9")
        register.place(x=135, y=380)

        register.bind("<Enter>", setLine)
        register.bind("<Leave>", resetLine)
        register.bind("<Button-1>", Register_toggle)

        # Entries
        color = '#F0F0F0'
        userInput = tk.Entry(self, bg=color, borderwidth=0, width=58)
        passInput = tk.Entry(self, show="*", bg=color, borderwidth=0, width=58)

        userInput.place(x=35, y=113)
        passInput.place(x=35, y=198)

        # Lines
        canvas_width = 344
        canvas_height = 2
        # line = under username, line2 = under password, line3 = under register

        line = tk.Canvas(self, width=canvas_width, height=canvas_height, bg="grey")
        line2 = tk.Canvas(self, width=canvas_width, height=canvas_height, bg="grey")
        line3 = tk.Canvas(self, width=46, height=1, bg="black")

        line.place(x=30, y=135)
        line2.place(x=30, y=220)
        line3.place(x=136, y=397)
        line3.configure(bg="#F0F0F0")

        userInput.bind("<FocusIn>", setColor)
        userInput.bind("<FocusOut>", resetColor)
        passInput.bind("<FocusIn>", setColor)
        passInput.bind("<FocusOut>", resetColor)

        #Submit Button
        submit = tk.Button(self, text='Login', padx=150, bg="#e62727", activebackground="#B31E1E",
                           activeforeground="white", fg="white", font="Sans/serif 12 bold", pady=15,
                           command=on_click)
        submit.bind("<Enter>", setSubmitColor)
        submit.bind("<Leave>", resetSubmitColor)

        submit.place(x=30, y=320)


#Temporary function for printing
def printToConsole(data):
    if data['action'] == 'userMessage':
        print("> {}: {}".format(data['user'], data['text']))
    elif data['action'] == 'serverMessage':
        print("> SERVER: {}".format(data['text']))
    elif data['action'] == 'loginFailure':
        print("> LOGIN FAILED: {}".format(data['reason']))
    #else:
        #print(data)