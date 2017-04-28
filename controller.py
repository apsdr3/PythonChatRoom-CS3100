import model as Model
import view as View
import threading
from view import *
import queue
import time

def listen(ws, q):
	try:
		while True:
			data = Model.recv(ws)
			if 'action' in data:
				q.put(data)
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
		
		if (L.login and not validLog):
			L.password.configure(text="Password: (Does not match)", fg="red")
			L.login = 0

		if validLog and L.login:
			L.login = 0
			LoginWindow = False
			Model.login(ws, L.u)
			L.destroy()

	#TODO: Debating whether to keep this window for chat selection or just placing client in chatroom randomly/default to chatroom 1
	S = Select()
	SelectWindow = True

	while SelectWindow:
		#TODO: Fix this so when pressing enter it would load the chatroom
		S.update()
		if (S.initialRoom != 0):
			SelectWindow = False
			initialChatRoom = S.initialRoom
			S.destroy()

	C = ChatRoom()

	C.chatRoomNumber = initialChatRoom
	C.chatRoomList.select_set(C.chatRoomNumber-1)
	C.display_message("Hello World! Welcome to the chatroom #" + str(C.chatRoomNumber) + "!", "CHATROOM")
	#testing purposes
#	C.chatRoomNumber = 1
	#testing purposes

	"""
	# CHAT ROOM SWITCH CHECK		
		print("Which Chat room do you want to join? 1-2")
		chatRoomNum = input('')
		C.chatRoomNumber = int(chatRoomNum)
		print(C.chatRoomNumber)
	# CHAT ROOM SWITCH CHECK
	"""

	# Main loop
	# TODO: Make this loop an event loop
	while True:
		# Read user input
		#run, buff = Model.consoleInput() # Implement event polling so that this line no longer blocks

		C.update()

		#Used for getting the current selection of chatrooms
		selectedChatRoom = C.chatRoomList.curselection()[0]+1 #TODO: Find proper way of doing this (throws errors on exit)
		if (C.chatRoomNumber != selectedChatRoom):
			#TODO: Figure out how to clear textbox
			C.chatRoomNumber = selectedChatRoom
			C.display_message("Changed to ChatRoom #" + str(C.chatRoomNumber), "CHATROOM")
		#print(C.chatRoomNumber)


		#sending messages
		if C.TB:
			# Needs to separate chat room
			
			# Chat room # 1
			if C.chatRoomNumber == 1:
				C.T = Model.appendMessage(C.T, '1')
				jsonData = Model.pythonToJson('message', 'text', C.T)
				Model.send(ws, jsonData)
				C.TB = 0

			#print(C.T)

			# Chat room # 1
			if C.chatRoomNumber == 2:
				C.T = Model.appendMessage(C.T, '2')
				jsonData = Model.pythonToJson('message', 'text', C.T)
				Model.send(ws, jsonData)
				C.TB = 0
			
			time.sleep(0.5)

		#receiving messages
		try:
			data = recvQueue.get_nowait()
			#need to only print messages inside your separate chat room
			if C.chatRoomNumber == 1:
				if data['action'] == 'userMessage':
					message = data['text']
					if message[0] == '1':
						message = Model.fixMessageString(message)
						C.display_message(message, data['user'])
				
			if C.chatRoomNumber == 2:
				if data['action'] == 'userMessage':
					message = data['text']
					if message[0] == '2':
						message = Model.fixMessageString(message)
						C.display_message(message, data['user'])
				
		except queue.Empty:
			pass


	Model.closeConnection(ws)