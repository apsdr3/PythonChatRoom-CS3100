from model import Model
from model import Listen
import view as View
from view import ChatRoom

if __name__ == '__main__':
        model = Model()
        
        C = ChatRoom()
        C.display_message("Hello World! Welcome to the chatroom!", "CHATROOM")
        ws = model.createConnection() #creates connection
	
        model.login() #login specs
	
        listener = Listen(ws)
        listener.start()

        run = True
        while run: #have to write false function
                C.update()
                if C.TB:
                    C.display_message(C.T, C.U)
                    C.TB = 0
                run = model.sendMessage(listener) #sends message
                jsonData = model.receiveMessage() #receives message sent to server
                #print(jsonData)

        model.closeConnection(listener)
