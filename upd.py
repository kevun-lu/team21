import socket 
import time

localIP = '127.0.0.1'
sendPort = 7501
receivePort = 7500
bufferSize = 1024

class Udp:

    def __init__(self, play_action):
        self.play_action = play_action
        self.sendPort = 7500
        self.sendSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.receivePort = 7501
        self.__receiveSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__receiveSocket.bind(('127.0.0.1',7501))

    def sendData(self, data, port):
        sendSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sendSocket.sendto(data.encode(), ("127.0.0.1", port))
        sendSocket.close()


    def sendEquipmentId(self, equipmentId):
        self.__receiveSocket.sendto(str(equipmentId).encode(), (localIP, self.sendPort))

    # def receiveEquipmentId(self):
    #     received = ''
    #     received, address = self.__receiveSocket.recvfrom(bufferSize)
    #     print(f"Received equipment: {received.decode()}")
    #     if ":" in received:
    #         transmittingId, hitId = received.split(":")
    #         print(f"Received data - Transmitting ID: {transmittingId}, Hit ID: {hitId}")
    #         #logic to handle the received IDs as needed
    #         #send to playaction screen
    #         self.play_action.receive_player_action(transmittingId, hitId) #kevin van put right method here

    #     else: 
    #         print("Invalid format received.")
    
    def receiveData(self):
        while True:
            #receiveSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.__receiveSocket.settimeout(5)
            try:
                data, _ = self.__receiveSocket.recvfrom(1024)
                data = data.decode()
                data = data.partition(':')
                self.play_action.receive_player_action(int(data[0]),int(data[2])) 
                self.sendEquipmentId(data[2])
            except socket.timeout:
                data = None
                #self.__receiveSocket.close()
              
            
        

    def sendGameStartCode(self):
        #time.sleep(10) #simulating a 10-second countdown timer
        self.sendData("202", self.sendPort)
        print("Game start code (202) sent.")
        self.receiveData()

    def sendGameEndCode(self):
        for _ in range(3): #Send code 221 three times
            self.sendData("221", self.sendPort)
            print("Game end code (221) sent.")

