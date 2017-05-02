import tkinter as tk
from tkinter import ttk
import time
from tkinter import *
from PIL import Image, ImageTk

class ChatRoom(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.minsize(825, 825)
        self.title("Chat Room - Client 2")
        self.configure(bg="#36393E")

        #UPPER CONTAINER
        self.uframe = tk.Frame(self, bg="#C0C0C0", relief=SUNKEN, borderwidth=2)
        self.uframe.place(x=25, y=25, width=775, height=100)

        image = Image.open("something2.jpg")
        photo = ImageTk.PhotoImage(image)

        imageHolder = Label(self.uframe, image = photo)
        imageHolder.image = photo
        imageHolder.pack()

        #LEFT CONTAINER
        self.lframe = tk.Frame(self, bg="#C0C0C0", relief=SUNKEN, borderwidth=2)
        self.lframe.place(x=25, y=150, width=150, height=650)

        userRoomLabel = tk.Label(self.lframe, text=" Users:", font = "Sans/Serif 12 bold", bg = "#C0C0C0", justify = "center")
        userRoomLabel.pack(side = TOP)

        self.userRoomList = Listbox(self.lframe, borderwidth = 0, highlightthickness = 0,
                                    justify = 'center', bg = "#C0C0C0")
        self.userRoomList.place(x = 15, y = 25, height = 300)
        #self.userRoomList.config(state="enabled", disabledforeground="Black")

        self.userSet = False

        chatListLabel = tk.Label(self.lframe, text="ChatRooms: ", font = "Sans/Serif 12 bold", bg = "#C0C0C0")
        chatListLabel.place(x = 25, y = 350)

        #Listbox for listing the chatrooms
        self.chatRoomList = Listbox(self.lframe, borderwidth = 0, highlightthickness = 0,
                                    justify = 'center', bg = "#C0C0C0")
        self.chatRoomList.place(x = 15, y = 375)
        self.chatRoomList.insert(1, "ChatRoom #1")
        self.chatRoomList.insert(2, "ChatRoom #2")
        self.chatRoomList.insert(3, "ChatRoom #3")
        self.chatRoomList.insert(4, "ChatRoom #4")
        self.chatRoomList.insert(5, "ChatRoom #5")

        self.chatRoomList.bind('<Button-1>', self.updateVar)
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
        self.entry2.focus_force()

        #VARIABLES
        self.T = ""
        self.U = ""
        self.TB = 0
        self.UB = 0
        self.chatRoomNumber = 1
        self.updater = False
        self.close = 0

        def on_closing():
            self.close = 1
            time.sleep(0.1)

        self.protocol("WM_DELETE_WINDOW", on_closing)
        
        self.update()
             
    def display_message(self,S,U):
        now = time.strftime("%H:%M:%S" , time.localtime())
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

    def updateVar(self, event):
        self.updater = True



    #self.userRoomList.insert(1, "UserExample1")#0
    #self.userRoomList.insert(2, "UserExample2")#1
    #self.userRoomList.insert(3, "UserExample3")#2
    #userSet = True
    #self.userRoomList.delete(2, 3)#based on index, ends on next index
    #To delete all: self.userRoomList.delete(0, END) or C.userRoomList.delete(0,END) if on other file

    def userListScroll(self):
        if self.userSet: #Throws an error when there is no user
            #print (self.userRoomList.get(0, "end").index(self.userRoomList.get(END)) + 1)
            #To have scrollbar show up at more than 19 users
            if ((self.userRoomList.get(0, "end").index(self.userRoomList.get(END)) + 1) >= 20):
                self.scrollU = tk.Scrollbar(self.userRoomList)
                self.scrollU.place(x = 103, height = 300)
                self.userRoomList.config(yscrollcommand=self.scrollU.set)
                self.scrollU.config(command=self.userRoomList.yview)

    def updateUsers(self, users):
        self.userRoomList.delete(0, END)
        if len(users) > 0:
            self.userSet = True
        else:
            self.userSet = False

        for i in range(len(users)):
            self.userRoomList.insert(i, users[i]['name'])
        #self.userListScroll()
        self.update()

"""
Login Window
"""
class Login(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        bgColor = "#36393E"
        def setColor(event):
            if (self.focus_get() == userInput):
                line.configure(bg="white")
            if (self.focus_get() == passInput):
                line2.configure(bg="white")

        def resetColor(event):
            if (self.focus_get() != userInput):
                line.configure(bg="black")
            if (self.focus_get() != passInput):
                line2.configure(bg="black")

        def setLine(event):
            line3.configure(bg="white")

        def resetLine(event):
            line3.configure(bg=bgColor)

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
                self.password.configure(text="Password:", fg="white")
            else:
                welcome.configure(text="Please Log In")
                submit.configure(text="Login", padx=150)
                needAcc.configure(text="Need an account?")
                register.configure(text="Register")
                line3.configure(width=46)
                self.password.configure(text="Password:", fg="white")

        def on_click():
            self.login = 1
            self.u = userInput.get()
            self.p = passInput.get()

        def enterBtnLogIn(event):
            self.login = 1
            self.u = userInput.get()
            self.p = passInput.get()

        def on_closing():
            self.close = 1
            time.sleep(0.1)
        self.close = 0
        self.protocol("WM_DELETE_WINDOW", on_closing)

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

        #Background Color
        self.configure(bg = bgColor)


        # Welcome Label
        welcome = tk.Label(self, text="Please Log In", font="Sans/Serif 15 bold", fg="White", bg = bgColor)
        welcome.place(x=130, y=20)

        # Username Label
        username = tk.Label(self, text="Username:", font="Sans/Serif 9", bg = bgColor, fg="White")
        username.place(x=30, y=70)

        # Password Label
        self.password = tk.Label(self, text="Password:", font="Sans/Serif 9", bg = bgColor, fg="White")
        self.password.place(x=30, y=153)

        # NeedanAccount Label
        needAcc = tk.Label(self, text="Need an account?", font="Sans/Serif 9", bg = bgColor, fg="White")
        needAcc.place(x=30, y=380)

        # Register/Button
        register = tk.Label(self, text="Register", font="Sans/Serif 9", bg = bgColor, fg="White")
        register.place(x=135, y=380)

        register.bind("<Enter>", setLine)
        register.bind("<Leave>", resetLine)
        register.bind("<Button-1>", Register_toggle)

        # Entries
        userInput = tk.Entry(self, bg=bgColor, borderwidth=0, width=58, fg="White")
        passInput = tk.Entry(self, show="*", bg=bgColor, borderwidth=0, width=58, fg="White")

        userInput.focus_set()
        userInput.place(x=35, y=113)
        passInput.place(x=35, y=198)

        # Lines
        canvas_width = 344
        canvas_height = 1
        # line = under username, line2 = under password, line3 = under register

        line = tk.Canvas(self, width=canvas_width, height=canvas_height, highlightthickness = 0, bg = "white")
        line2 = tk.Canvas(self, width=canvas_width, height=canvas_height, highlightthickness = 0, bg = "black")
        line3 = tk.Canvas(self, width=46, height=1, bg="black", highlightthickness = 0)

        line.place(x=30, y=135)
        line2.place(x=30, y=220)
        line3.place(x=138, y=397)
        line3.configure(bg="#2E282D")

        userInput.bind("<FocusIn>", setColor)
        userInput.bind("<FocusOut>", resetColor)
        passInput.bind("<FocusIn>", setColor)
        passInput.bind("<FocusOut>", resetColor)
        # passInput.bind("<Return>", enterBtnLogIn)
        self.bind("<Return>", enterBtnLogIn)

        #Submit Button
        submit = tk.Button(self, text='Login', padx=150, bg="#e62727", activebackground="#B31E1E",
                           activeforeground="white", fg="white", font="Sans/serif 12 bold", pady=15,
                           command=on_click)
        submit.bind("<Enter>", setSubmitColor)
        submit.bind("<Leave>", resetSubmitColor)

        submit.place(x=30, y=320)


"""
ChatRoom Selection Window
"""
class Select(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        bgColor = "#36393E"
        def on_closing():
            self.close = 1
            time.sleep(0.1)
        self.close = 0
        self.protocol("WM_DELETE_WINDOW", on_closing)

        def goChat():
            if (selection.get() == "ChatRoom 1"):
                self.initialRoom = 1
            elif (selection.get() == "ChatRoom 2"):
                self.initialRoom = 2
            elif (selection.get() == "ChatRoom 3"):
                self.initialRoom = 3
            elif (selection.get() == "ChatRoom 4"):
                self.initialRoom = 4
            elif (selection.get() == "ChatRoom 5"):
                self.initialRoom = 5

        def enterPress(event):
            if (selection.get() == "ChatRoom 1"):
                self.initialRoom = 1
            elif (selection.get() == "ChatRoom 2"):
                self.initialRoom = 2
            elif (selection.get() == "ChatRoom 3"):
                self.initialRoom = 3
            elif (selection.get() == "ChatRoom 4"):
                self.initialRoom = 4
            elif (selection.get() == "ChatRoom 5"):
                self.initialRoom = 5

        self.title("Chat Room Selection Screen")
        self.initialRoom = 0
        #self.focus_force()
        w = 300  # width for the Tk self
        h = 150  # height for the Tk self

        # get screen width and height
        ws = self.winfo_screenwidth()  # width of the screen
        hs = self.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk self window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.configure(bg = bgColor)
        # labels
        chooseLabel = tk.Label(self, text="Please select a chatroom: ", font="Sans/Serif 12", fg = "white", bg = bgColor)
        chooseLabel.pack(pady=10)

        # combobox
        selection = ttk.Combobox(self, state="readonly", takefocus = True)
        selection.pack(pady=10)
        selection['values'] = ('ChatRoom 1', 'ChatRoom 2', 'ChatRoom 3', 'ChatRoom 4', 'ChatRoom 5')
        selection.current(0)
        selection.focus_force()

        # button
        submit = tk.Button(self, text='Start Chatting', bg = "#e62727", activebackground = "#B31E1E",
        activeforeground = "white", fg = "white", font = "Sans/serif 12 bold", padx=45, pady=10, command=goChat)
        submit.pack()

        self.bind("<Return>", enterPress)


#Debug function for printing to console
def printToConsole(data):
    print(data)