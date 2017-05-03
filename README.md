# PythonChatRoom-CS3100
Python Client Side Application that works side by side with another group's Server Application: https://github.com/megalodan/cs3100-s2-java/

Server Communication handling can be seen through: http://cs3100-s2.herokuapp.com/

Python Applicatin needs to install packages: (pip install . .)
websocket-client
pillow

websocket-client allows us to connect to the server through websockets
pillow allows us to use images for the GUI

GUI is made through tkinter

Mutli-threading is used in order to send/recieve messages in real time

Functionalities:
- 5 chat rooms : handled by the client as the server does not handle multiple chat rooms (this is done by message identification depending on specific chat room)
- emotes : type !help for all the emotes
- userlist : left side bar outputs the list of all available users within the server, NOT in a specific chat room
