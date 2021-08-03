from socket import *

serverName = 'server ip'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_STREAM)

clientSocket.connect((serverName,serverPort))
sentence = input("Please enter the sentence: ")

clientSocket.send(sentence.encode())
modified_sentence, addr = clientSocket.recv(1024)
print(modified_sentence.decode())

clientSocket.close()