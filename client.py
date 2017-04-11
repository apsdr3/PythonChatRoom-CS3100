import json
from websocket import create_connection

ws = create_connection("ws://cs3100-s2.herokuapp.com/actions")

print("Sending 'Log in info'...")

#JSON to Python
jsonData = '{"action": "login", "name": "Miggy"}'
jsonToPython = json.loads(jsonData)


#Python to JSON
pythonData = {'action':'login', 'name':'Miggy'}
pythonToJson = json.dumps(pythonData)



ws.send(pythonToJson)

print("Receiving...")

jsonData = ws.recv()
jsonToPython = json.loads(jsonData)

print(jsonToPython)

ws.close()