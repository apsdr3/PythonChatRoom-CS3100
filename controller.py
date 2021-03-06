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
	C.display_message("Welcome to ChatRoom #" + str(C.chatRoomNumber) + "!", "CHATROOM")

	baseMessage = "ENTERED THE CHATROOM"
	message = Model.appendMessage(baseMessage, chr(ord('0') + C.chatRoomNumber))
	jsonData = Model.pythonToJson('message', 'text', message)
	Model.send(ws, jsonData)

	# Main loop
	while C.close == 0:

		C.update()
		time.sleep(0.01)

		#Used for getting the current selection of chatrooms
		if (C.updater):
			selectedChatRoom = C.chatRoomList.get(0, "end").index(
				C.chatRoomList.get(ANCHOR)) + 1

		if (C.chatRoomNumber != selectedChatRoom):
			#Print exit
			baseMessage = "LEFT THE CHATROOM"
			message = Model.appendMessage(baseMessage, chr(ord('0') + C.chatRoomNumber))
			jsonData = Model.pythonToJson('message', 'text', message)
			Model.send(ws, jsonData)

			C.chatRoomNumber = selectedChatRoom
			C.textbox.config(state=NORMAL)
			C.textbox.delete(1.0, END)
			C.textbox.config(state=DISABLED)
			C.display_message("Welcome to ChatRoom #" + str(C.chatRoomNumber) + "!", "CHATROOM")
			
			baseMessage = "ENTERED THE CHATROOM"
			message = Model.appendMessage(baseMessage, chr(ord('0') + C.chatRoomNumber))
			jsonData = Model.pythonToJson('message', 'text', message)
			Model.send(ws, jsonData)

		if C.TB:

			# prepend chat room number to sent messages
			message = Model.appendMessage(C.T, chr(ord('0') + C.chatRoomNumber))
			jsonData = Model.pythonToJson('message', 'text', message)
			Model.send(ws, jsonData)
			C.TB = 0

		#receiving messages
		try:
			data = recvQueue.get_nowait()		
			#View.printToConsole(data);
			# User messages
			if data['action'] == 'userMessage':
				message = data['text']
				# Only display messages for your chat room
				if message[0] == chr(ord('0') + C.chatRoomNumber):
					message = Model.fixMessageString(message)
					if (C.isEmote(message)):
						C.createEmote(message)
					elif(message == "!help"):
						helpmsg = "Current emotes are: "
						for i in range(0, len(C.emoteStrings)):
							helpmsg = helpmsg + C.emoteStrings[i]
							if (i != len(C.emoteStrings)-1):
								helpmsg = helpmsg + ", "
						C.display_message(helpmsg, 'SERVER')
					else:
						C.display_message(message, data['user'])
			elif data['action'] == 'serverMessage':
				C.display_message(data['text'], 'SERVER')
			elif data['action'] == 'getUserList':
				# {"action":"getUserList", "users":[{"name":"Tom","id":0}]}
				userlist = []
				for user in data['users']:
					userlist.append(user)
				C.updateUsers(userlist)
			elif data['action'] == 'newUser' or data['action'] == 'removeUser':
				Model.send(ws, Model.getUsers())

		except queue.Empty:
			pass


	Model.closeConnection(ws)