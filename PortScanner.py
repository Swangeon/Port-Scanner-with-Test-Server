'''
Author: Sean Brady
Project Name: Port Scanner
'''

import socket
import threading
from queue import Queue

# Setting the host that you want to scan
host = socket.gethostname()

# Port Scanner function itself
def port_scanner(port):

	# Setting up the socket object for connecting
	sock = socket.socket() 

	try:
		
		# Making a seperate variable for a host and port because I feel it looks better than sock.connect((host, port)) 
		socket_info = (host, port) 

		# Trying to connect to the host and port
		sock.connect(socket_info)

		print(f"[OPEN] Port {port} is Open")
		
		# Close the connection
		sock.close() 

	except socket.error as e:
		# print(f"Port {port} is closed")
		pass

# This will help pull a process/worker from the queue and process it
def threader():
	while True:
		worker = queue.get()

		#print(worker)

		port_scanner(worker)

		queue.task_done()

# Create a FIFO queue
queue = Queue()

# How many max threads do we allow for 
for maxthread in range(50):
	thread = threading.Thread(target=threader)

	# Will create a daemon for the thread
	thread.daemon = True

	# Begins the thread
	thread.start()

# Assigning ports to different threads and queues 
for worker in range(1, 65535):

	queue.put(worker)
	#print(queue.qsize())
	#print(queue.get())

# Wait for the current queues and threads to stop
queue.join()

input("Press [ENTER] to quit...")
