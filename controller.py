from model import Model
import view as View

if __name__ == '__main__':
	model = Model()

	View.welcomeMessage()	#welcomes user
	model.createConnection() #creates connection
	model.login() #login specs
	while(True):
		model.sendMessage() #sends message
