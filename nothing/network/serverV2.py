from socket import *
#from select import *
HOST = ''
PORT = 5050
BUFSIZE = 1024
ADDR = (HOST, PORT)

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(ADDR)
serverSocket.listen()

while 1:
	clientSocket, clientAddr = serverSocket.accept()
	msg = clientSocket.recv(BUFSIZE)
	print("message : %s"%msg)
	clientSocket.close()


