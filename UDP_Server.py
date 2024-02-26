import socket
import keyboard

# Define local IP address and port  
LOCAL_IP = "192.168.1.100"  # Change to what is needed for both these<<
LOCAL_PORT = 7501
BUFFERSIZE = 2400

# Message to be sent back from the server to the client
MsgFromServer = str.encode("Hello New Client.")

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the local address and port
sock.bind((LOCAL_IP, LOCAL_PORT))
print("UDP system is online.")

# Receive player information and add them to the player list
# Initialize an empty dictionary to store player information
Player_List = []
PlayerSelection = True
while PlayerSelection:
    # Will end player/equipment code sync and satrt the game by pressing f3
    key = keyboard.read_key()
    if key != "f3":
        data = sock.recvfrom(1024)
        playername = data[0]
        addr = data[1]
        Player_List.append(playername)
        # Send a message to indicate player initialization is complete        
        sock.sendto(str.encode("Player initialization complete"), addr)
        print("Player List:", Player_List)  # Debugging: Print updated player list
        continue
    if key == "f3":
        PlayerSelection = False
        print("Lock and Load")
        break
        
    

GameState = True
# Continuously receive messages from clients and send response
while GameState:
    # Will end the server prematurely by pressing q
    
    key = keyboard.read_key()
    if key != "q":
        # Buffer size is 1024 bytes. This will empty the buffer continually.
        addressPair = sock.recvfrom(1024)
        eqipmentID = addressPair[0]
        address = addressPair[1]

        clientMsg = "EqID:{}".format(eqipmentID)
        clientIP = "Client IP:{}".format(address)
        print(clientMsg)
        print(clientIP)

        # The reply to the client
        sock.sendto(MsgFromServer, addr)
    else:
        GameState = False
        print("Shutting Server Down...")
        sock.close()
        break
    
