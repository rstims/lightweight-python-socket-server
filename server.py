import socket, imp, json
while 1:
	# Create and open the port the socket will be listening on
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind(("127.0.0.1", 8008))
	server_socket.listen(5)

	# Inside processing loop we wait for a connection 
	client_socket, address = server_socket.accept()
	
	# Receive buffer
	controlCommand = client_socket.recv(3000)
	
	# Parse JSON into Dict
	args = json.loads(controlCommand)
	
	# Load python file depending on file passed in buffer
	modl = imp.load_source('tmp', args['path'])	
	
	# Find function named main() and pass it args from buffer
	out = modl.main(args['args'])
	
	# Send response back to requester
	client_socket.send(out)		
	
	# Close connection
	client_socket.close()
