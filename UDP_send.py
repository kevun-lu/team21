import socket


# This is the code for the clients (NOT SERVER) which starts by taking a targetted IP address and port
# An input is also taken for the Player's ID or tag. This is later sent through UDP to the server to identify which player the information is coming from.
# In set up this is just the player calibration. During game this will be used to send when the player is "hit" and who "hit" them 
  

#IP and Port can be changed as needed.
SERVER_IP = "localhost"
SERVER_PORT = 8080
Player_ID = "Joe_Schmoe"
BUFFERSIZE = 1024


# print ("message:", Player_ID)

# if ("Player is hit")
#     {}

# if ("Player hits enemy")
#     {}

# Probably best if all the information is then connected into only one message to be sent/received.
MsgFrClient = "Player: " + Player_ID

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.sendto(bytes(MsgFrClient, "utf-8"), (SERVER_IP, SERVER_PORT))

MessageFrServer = sock.recvfrom(BUFFERSIZE)
msg = "S2C: " + format(MessageFrServer[0])

print (msg)