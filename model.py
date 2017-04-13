import json
from websocket import create_connection
import threading

global ws

class Model(object):

	#def __init__(self):


	def createConnection(self):
		global ws
		ws = create_connection("ws://cs3100-s2.herokuapp.com/actions")
		#ws.run_forever()


	def closeConenction(self):
		ws.close()

	def login(self):
		print("Username: ", end = "")
		username = input("")
		print("Password: ", end = "")
		password = input("")
		jsonData = self.pythonToJson("login", "name", username)
		ws.send(jsonData)
		return

	def sendMessage(self):
		global ws
		print("Message: ", end = "")
		message = input("")
		jsonData = self.pythonToJson("message", "text", message)
		ws.send(jsonData)

	def receiveMessage(self):
		global ws
		jsonData = ws.recv()
		return jsonData

	def pythonToJson(self, action, field, data):
		#Python to JSON
		pythonData = {'action':action, field:data}
		jsonData = json.dumps(pythonData)
		return jsonData

	#need to figure out how to separate json values and store
	def jsonToPython(self, data):
		data = json.loads(jsonData)







class Listen(threading.Thread):
	def __init__(self, ws):
		super(Listen, self).__init__()
		self.ws = ws
		self.stopped = False

	def stop(self):
		self.stopped = True

	def run(self):
		while not self.stopped:
			jsonData = self.ws.recv()
			jsonToPython = json.loads(jsonData)
			print("> {}".format(jsonToPython))
		print("EXIT THREAD")

def main():
	ws = create_connection("ws://cs3100-s2.herokuapp.com/actions")

	print("Username: ")
	name = input("")

	#Python to JSON
	pythonData = {'action':'login', 'name':name}
	pythonToJson = json.dumps(pythonData)

	ws.send(pythonToJson)

	jsonData = ws.recv()
	jsonToPython = json.loads(jsonData)

	listener = Listen(ws)
	listener.start()
	running = True

	while running:
		print("Message: ")
		message = input("")

		if message == "exit":
			running = False
			listener.stop()
		else:
			pythonData = {'action':'message', 'text':message}
			pythonToJson = json.dumps(pythonData)
			ws.send(pythonToJson)

	#ws.run_forever()
	listener.join()
	ws.close()

main()