from socket import *

serverName = 'hostname'
serverPort = 12000

clientsocket = socket(AF_INET, SOCK_DGRAM)
message = input("please enter the message to send")

clientsocket.sendto(message.encode(), (serverName,serverPort))
modifiedMessage, serverAddress = clientsocket.recvfrom(2048)

print(modifiedMessage.decode())
clientsocket.close()
