import socket

# Define IP address and ports
BUFFERSIZE = 1024
serverPort = 7500
clientPort = 7501
ipAddress = "localhost"
NumPlayers = 0
MaxPlayers = 10

# Asks for number of players and stores it as an int
NumPlayers = input("How many players on each team? ")
NumPlayers = int(NumPlayers)

# Stores each player's eqid
RedTeam = [0,0,0,0,0,0,0,0,0,0]
for i in range (0, NumPlayers):
    RedTeam[i] = input("Equipment code for RED team member " + str(i+1) + ": ")

GreenTeam = [0,0,0,0,0,0,0,0,0,0]
for i in range (0, NumPlayers):
    GreenTeam[i] = input("Equipment code for GREEN team member " + str(i+1) + ": ")


# Message to be sent back from the server to the client
ServertoClientmsg = str.encode('Hello, New Client ')

# Create UDP server socket for RECEIVING
ServerReceives = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Create UDP client socket for SENDING
ServerSends = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the local address and port
ServerReceives.bind((ipAddress, serverPort))

print('Waiting on start code... ')

shortcut = '0'
while shortcut != '202':
    shortcut, clientaddress = ServerReceives.recvfrom(BUFFERSIZE)
    shortcut = shortcut.decode('utf-8')
    print ('')
    print (shortcut)


GameState = True

while GameState:
    ServertoClientmsg = ''
    
    # if red player tags, green player
    # msg = '11'
    
    # if green player tags, red player
    # msg = '33'

    # if green player tags red's base 
    # msg = '55'

    # if red player tags green's base 
    # msg = '77'

    print("Sending to client: " + ServertoClientmsg)
    ServerSends.sendto(str.encode(ServertoClientmsg), (ipAddress, clientPort))
    
    shortcut, clientaddress = ServerReceives.recvfrom(BUFFERSIZE)
    shortcut = shortcut.decode('utf-8')
    print ("From the Client: ")
    print (shortcut)
    
    #increments player on team
    i = i + 1
	
    if shortcut == '221':
        ServerSends.close()
        ServerReceives.close()
        GameState = False

print("The game is over. ")
