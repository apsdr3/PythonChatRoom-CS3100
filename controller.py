import model as Model
import view as View
import threading
from view import ChatRoom
from view import Login
import queue

def listen(ws, q):
	try:
		while True:
			data = Model.recv(ws)
			if 'action' in data:
				q.put(data)
				#View.printToConsole(data)
	except ValueError:
		pass


if __name__ == '__main__':

	ws = Model.createConnection()

	recvQueue = queue.Queue()

	listener = threading.Thread(target=listen, args=(ws,recvQueue,))
	listener.setDaemon(True)

	listener.start()

	L = Login()

	LoginWindow = True
	# set validLog to true if valid username & pass, otherwise false
	validLog = True
	#Main Login Loop
	while LoginWindow:
		L.update()
		#TODO Login Authentication
		'''
		try:
			response = recvQueue.get_nowait()
			if response['action'] == 'loginFailure':
				Model.printToConsole(response)
				validLog = False
		except queue.Empty:
			# Nothing received from server
		'''
		if (L.login and not validLog):
			L.password.configure(text="Password: (Does not match)", fg="red")
			L.login = 0

		if validLog and L.login:
			L.login = 0
			LoginWindow = False
			Model.login(ws, L.u)
			L.destroy()

	C = ChatRoom()
	C.display_message("Hello World! Welcome to the chatroom!", "CHATROOM")


	# Main loop
	# TODO: Make this loop an event loop
	while True:
		# Read user input
		#run, buff = Model.consoleInput() # Implement event polling so that this line no longer blocks

		C.update()

		if C.TB:
			jsonData = Model.pythonToJson('message', 'text', C.T)
			Model.send(ws, jsonData)
			C.TB = 0

		# Exit loop if exit command was sent
		#if not run:
		#	break

		# Send data to View
		try:
			data = recvQueue.get_nowait()
			if data['action'] == 'userMessage':
				C.display_message(data['text'], data['user'])
		except queue.Empty:
			pass


	Model.closeConnection(ws)