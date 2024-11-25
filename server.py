import socket

# Create a scoket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port
host = '127.0.0.1' # localhost
port = 12345

# Bind the socket to the address
server_socket.bind((host,port))
 
# Start listening for incoming connections 
server_socket.listen(5)

print(f'Server listening on {host}: {port} ...')

# Accept a connection a nd get the client socket
client_socket, client_address = server_socket.accept()
print(f'Connection established with {client_address}')

# Receive data form the client
data = client_socket.recv(1024).decode('utf-8')
print(f'Received: {data}')

# Echo the received data back to the client