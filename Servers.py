import socket
import threading
from queue import Queue

# Creating an object to set servers up easier
class CreateServer(threading.Thread):
	def __init__(self, hostname, port, motd):
		threading.Thread.__init__(self)
		self.hostname = hostname
		self.port = port
		self.motd = motd

	# Makes the sever
	def getServer(self):
		self.sock = socket.socket()
		self.sock_info = (self.hostname, self.port)
		
		self.sock.bind(self.sock_info)
		self.sock.listen(5)

		while True:
			print("Waiting for Connection...")

			self.client, self.address = self.sock.accept()

			print('Connection from {0}'.format(self.address))

			self.client.send(f"{self.motd}".encode('utf-8'))

			self.client.close()

			break



# IP to host these servers on
localhost = socket.gethostname()

# Not what I would like to do to make the servers run concurrently but I will work on this and update it
def FTPserverfun():
	FTPserver = CreateServer(localhost, 21, "This is the FTP Server")
	FTPserver.getServer()

def SSHserverfun():
	SSHserver = CreateServer(localhost, 22, "This is the SSH Server")
	SSHserver.getServer()

def HTTPserverfun():
	HTTPserver = CreateServer(localhost, 80, "This is the HTTP Server")
	HTTPserver.getServer()

def HTTPSserverfun():
	HTTPSserver = CreateServer(localhost, 443, "This is the HTTPS Server")
	HTTPSserver.getServer()

# Used to create the threads 
def threader():

	thread1 = threading.Thread(target = FTPserverfun)
	thread2 = threading.Thread(target = SSHserverfun)
	thread3 = threading.Thread(target = HTTPserverfun)
	thread4 = threading.Thread(target = HTTPSserverfun)
	
	thread1.start()
	thread2.start()
	thread3.start()
	thread4.start()


threader()
