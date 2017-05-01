import model as Model
import view as View
import threading
from view import *
import queue
import time
import json

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
	while LoginWindow and L.close == 0:
		L.update()
		time.sleep(0.01)
		
		if (L.login and not validLog):
			L.password.configure(text="Password: (Does not match)", fg="red")
			L.login = 0

		if validLog and L.login:
			L.login = 0
			LoginWindow = False
			Model.login(ws, L.u)
			L.destroy()

	if L.close == 1:
		L.destroy()
		exit(0)


	#TODO: Debating whether to keep this window for chat selection or just placing client in chatroom randomly/default to chatroom 1
	S = Select()
	SelectWindow = True
	while SelectWindow and S.close == 0:
		S.update()
		time.sleep(0.01)
		if (S.initialRoom != 0):
			SelectWindow = False
			initialChatRoom = S.initialRoom
			S.destroy()

	if S.close == 1:
		S.destroy()
		exit(0)

	C = ChatRoom()

	C.chatRoomNumber = initialChatRoom
	selectedChatRoom = S.initialRoom
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

	while C.close == 0:
		# Read user input
		#run, buff = Model.consoleInput() # Implement event polling so that this line no longer blocks

		C.update()
		time.sleep(0.01)

		#Used for getting the current selection of chatrooms
		if (C.updater):
			selectedChatRoom = C.chatRoomList.get(0, "end").index(
				C.chatRoomList.get(ANCHOR)) + 1

		if (C.chatRoomNumber != selectedChatRoom):
			C.chatRoomNumber = selectedChatRoom
			C.textbox.config(state=NORMAL)
			C.textbox.delete(1.0, END)
			C.textbox.config(state=DISABLED)
			C.display_message("Changed to ChatRoom #" + str(C.chatRoomNumber), "CHATROOM")

		#print(C.chatRoomNumber)

		if C.TB:

			# prepend chat room number to sent messages
			message = Model.appendMessage(C.T, chr(ord('0') + C.chatRoomNumber))
			jsonData = Model.pythonToJson('message', 'text', message)
			Model.send(ws, jsonData)
			C.TB = 0

			'''
			if C.chatRoomNumber == 1:
				C.T = Model.appendMessage(C.T, '1')
				jsonData = Model.pythonToJson('message', 'text', C.T)
				Model.send(ws, jsonData)
				C.TB = 0

			# print(C.T)

			# Chat room # 1
			if C.chatRoomNumber == 2:
				C.T = Model.appendMessage(C.T, '2')
				jsonData = Model.pythonToJson('message', 'text', C.T)
				Model.send(ws, jsonData)
				C.TB = 0

			time.sleep(0.5)
			'''

		#receiving messages
		try:
			data = recvQueue.get_nowait()		

			# User messages
			if data['action'] == 'userMessage':
				message = data['text']
				# Only display messages for your chat room
				if message[0] == chr(ord('0') + C.chatRoomNumber):
					message = Model.fixMessageString(message)
					C.display_message(message, data['user'])

			elif data['action'] == 'serverMessage':
				C.display_message(data['text'], 'SERVER')
			#elif data['action'] == 'getUserList':
				#TODO: If not able to print users for a specific chatroom, we could just print the users for
				#TODO  all the chat rooms
		except queue.Empty:
			pass


	Model.closeConnection(ws)