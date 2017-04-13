import json
from websocket import create_connection
import threading

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