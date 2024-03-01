import socket
import keyboard
import time

# This is the code for the clients (NOT SERVER) which starts by taking a targetted IP address and port
# An input is also taken for the Player's ID or tag. This is later sent through UDP to the server to identify which player the information is coming from.
# In set up this is just the player calibration. During game this will be used to send when the player is "hit" and who "hit" them 

ClienttoServermsg = 'New Player is Ready'
ClienttoServermsg = str.encode(ClienttoServermsg)
serverPort = 7500
ipAddress = 'localhost'
BUFFERSIZE = 1024

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

selectionLock = True
# Locks Player until the game is ready to begin
while selectionLock:
    if keyboard.is_pressed('f5'):
        time.sleep(5)
        ClienttoServermsg = str.encode('202')
        clientSock.sendto(ClienttoServermsg, (ipAddress, serverPort))
        selectionLock = False
while True:
    if clientSock.recvfrom(BUFFERSIZE) == True:

            ServertoClientmsg = clientSock.recvfrom(BUFFERSIZE)
            ServertoClientmsg = ServertoClientmsg[0].decode('utf-8')
            print(ServertoClientmsg)
