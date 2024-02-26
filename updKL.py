import socket 

localIP = '127.0.0.1'
sendPort = 7500
receivePort = 7501
bufferSize = 1024

class Udp:

    def __init_(self) -> None:
        self.__sendPort = sendPort
        self.sendSocket = sendSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sendSocket.bind((localIP,sendPort))
        self.__receivePort = receivePort
        self.__receiveSocket = sendPort = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def sendData(self, data, port):
        sendSocket = socket.socket(socket.AF_INTET, socket.SOCK_DGRAM)
        sendSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sendSocket.sendto(data.encode(), ("<broadcast>", port))
        print("Data: ")
        print("Searching for equipment ID: ", self.sentId)

        sendSocket.close()

    def sendEquipmentId(self, equipmentId):
        self.__receiveSocket.sendto(str(equipmentId).encode(), (localIP, self.__sendPort))
        print(f"Showing equipment id: {equipmentId}.....")

    def receiveEquipmentId(self):
        received = ''
        while str(received) != '202':
            received, address = self.boardcast_socket.recvfrom(bufferSize)
            print(f"Received equipment: {received.decode()}")
    
    def receiveData(self, port):
        receiveSocket = socket.socket(socket.AF_INTET, socket.SOCK_DGRAM)
        receiveSocket.bind(('', port))
        receiveSocket.settimeout(10)
        try:
            data, _ = receiveSocket.recvfrom(1024)
        except socket.timeout:
            data = None
        finally:
            receiveSocket.close()
        return data.decode() if data else None

    def sentId(self):
        self.sendData(str(self.playerId), self.__sendPort)