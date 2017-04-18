from model import Model
from model import Listen
import view as View

if __name__ == '__main__':
	model = Model()

	View.welcomeMessage()	#welcomes user
	model.createConnection() #creates connection
	model.login() #login specs
	while(True):
		model.sendMessage() #sends message
		jsonData = model.receiveMessage() #receives message sent to server
		print(jsonData)