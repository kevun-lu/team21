import socket


# Define local IP address and port  
LOCAL_IP = "localhost"
LOCAL_PORT = 8080

# Message to be sent back from the server to the client
MsgFrServer = str.encode("Message received.")

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the local address and port
sock.bind((LOCAL_IP, LOCAL_PORT))
print("UDP system is online.")

print("How many total players in the game?")
Player_Count = int(input())
# Initialize an empty dictionary to store player information
Player_List = {}

# Receive player information and add them to the player list
while (Player_Count > 0):
    data = sock.recvfrom(1024)
    playername = data[0]
    addr = data[1]
    Player_List[playername] = addr
    Player_Count = Player_Count-1
# Send a message to indicate player initialization is complete
sock.sendto(str.encode("Player initialization complete"), addr)
print(Player_List)

# Continuously receive messages from clients and send response
while True: 
    # Buffer size is 1024 bytes. This will empty the buffer continually.
    data = sock.recvfrom(1024)
    PlayerName = data[0]
    addr = data[1]
    print ("C2S:", PlayerName)
    print ("Client's IP: ", data[1])
    sock.sendto(MsgFrServer, addr)