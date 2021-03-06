import json
from websocket import create_connection

def recv(ws):
	jsonData = ws.recv()
	pythonData = json.loads(jsonData)
	return pythonData

def send(ws, jsonData):
	ws.send(jsonData)
	return

def createConnection():
	ws = create_connection("ws://cs3100-s2.herokuapp.com/actions")
	return ws

def closeConnection(ws):
	ws.close()
	return

def pythonToJson(action, field, data):
	pythonData = {'action':action, field:data}
	jsonData = json.dumps(pythonData)
	return jsonData

def consoleInput(message = ""):
	run = True
	buff = input(message)
	if buff == '/exit':
		run = False
	return run, buff

def login(ws, username, password = None):
	jsonData = pythonToJson("login", "name", username)
	#if password is not None:
		#create password functionality
	send(ws, jsonData)
	return

#returns string with chat room number identifier	
def appendMessage(message, number):
	message = number + message
	return message

# Deletes first message identifier i.e. first letter in sent string to outout the correct user sent message
def fixMessageString(message):
	message = message[1:]
	return message

def getUsers():
	pythonData = {'action':'getUsers'}
	jsonData = json.dumps(pythonData)
	return jsonData;