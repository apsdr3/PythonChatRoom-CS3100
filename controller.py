import model as Model
import view as View
import threading
from view import ChatRoom
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

		username = Model.consoleInput("Username: ")[1]
		#password = consoleInput("Password: ")[1]
		Model.login(ws, username)

		C = ChatRoom()
		C.display_message("Hello World! Welcome to the chatroom!", "CHATROOM")

		# TODO: Login authentication
		'''
		try:
			response = recvQueue.get_nowait()
			if response['action'] == 'loginFailure':
				Model.printToConsole(response)
		except queue.Empty:
			# Nothing received from server
		'''

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