from socket import *
from select import *
HOST = ''
PORT = 8080
BUFSIZE = 1024
ADDR = (HOST, PORT)

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(ADDR)R)
print('bind')

serverSocket.listen(100)

