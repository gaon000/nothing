from socket import *

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5050
SIZE = 1024
SERVER_ADDR = (SERVER_IP, SERVER_PORT)

client_socket = socket(AF_INET, SOCK_STREAM) #create socket, AF_INET = IPv4, SOCK_STREAM = tcp
client_socket.connect(SERVER_ADDR) #connect to server
client_socket.send('hello'.encode())#send message
client_socket.close()
