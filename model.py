"""
#JSON to Python
jsonData = '{"action": "login", "name": "Miggy"}'
jsonToPython = json.loads(jsonData)

#Python to JSON
pythonData = {'action':'login', 'name':name}
pythonToJson = json.dumps(pythonData)
"""
import json

class Model(object)
	def createConnection()
		ws = create_connection("ws://cs3100-s2.herokuapp.com/actions")
		
	def createUsername()
		print("Username: ")
		name = input("")

	def pythonToJson(action, data)
		#Python to JSON
		pythonData = {'action':action, 'name':data}
		jsonData = json.dumps(pythonData)
		return jsonData

	#need to figure out how to separate json values and store
	def jsonToPython(data)
		data = json.loads(jsonData)

"""
ws.send(pythonToJson)

jsonData = ws.recv()
jsonToPython = json.loads(jsonData)

print("Message: ")
message = input("")

pythonData = {'action':'message', 'text':message}
pythonToJson = json.dumps(pythonData)
ws.send(pythonToJson)

#ws.run_forever()

ws.close()
"""