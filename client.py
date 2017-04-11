import json
from websocket import create_connection

ws = create_connection("ws://cs3100-s2.herokuapp.com/actions")

print("Username: ")
name = input("")

"""
#JSON to Python
jsonData = '{"action": "login", "name": "Miggy"}'
jsonToPython = json.loads(jsonData)

#Python to JSON
pythonData = {'action':'login', 'name':name}
pythonToJson = json.dumps(pythonData)
"""

#Python to JSON
pythonData = {'action':'login', 'name':name}
pythonToJson = json.dumps(pythonData)

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