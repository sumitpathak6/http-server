import socket 
import time

server_host = "0.0.0.0"
server_port = 8080  
#AF_INET -> INTERNET PROTOCOL(IPv4) ADDRESSES
#SOCK_STREAM -> TCP CONENCTION TYPE OF THE SOCKET
#SOCK_DGRAM -> UDP CONNECTION TYPE OF THE SOCKET {IN FORM OF DATAGRAMS}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#BELOW LINE ALLOWS THE SERVER ADDRESS TO REUSE THE LOCAL ADDRESS AFTER THE SOCKET IS CLOSED

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#BINDING THE SOCKET TO AN IP ADDRESS AND A PORT
server_socket.bind((server_host, server_port))

#PUTTING THE SOCKET TO LISTEN TO ANY INCOMING REQUEST

#5 -> MAX NUMBER OF ESTABLISHED CONNECTIONS WHICH CAN WAIT IN THE QUEUE
server_socket.listen(5)

print("Listening on port {server_port}...")

#ACCEPT THE FIRST REQUEST FROM THE QUEUE OF REQUESTS

while True:
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(1500).decode()
    print(request)

  