from model import Model
from model import Listen
import view as View

if __name__ == '__main__':
	model = Model()
	
	#View.welcomeMessage()	#welcomes user
	ws = model.createConnection() #creates connection
	
	model.login() #login specs
	
	listener = Listen(ws)
	listener.start()

	run = True
	while run: #have to write false function
		run = model.sendMessage(listener) #sends message
		#jsonData = model.receiveMessage() #receives message sent to server
		#print(jsonData)

	model.closeConnection(listener)