#!/usr/bin/python

import socket, sys, threading
from tcptools import *



class Connection(threading.Thread):

	PORT = 55900

	def __init__(self, (socket,adress), master):
		threading.Thread.__init__(self)
		self.socket = socket;
		self.adress = adress;
		self.master = master;
		
		self.lock = threading.Lock()

		print "connection initialized\n"


	def authenticate(self):
		while True:
			sentname = prompt(self.socket, "Welcome to InitialMUD! Username:")
			uname = sentname[:-2]
			print sentname
			self.lock.acquire()

			playerExists = self.master.ifPlayerExists(uname)
			self.lock.release()
			print "player exists: " + str(playerExists)
			if playerExists:
				passw = prompt(self.socket, "Password:\n")
				self.lock.acquire()
				if master.isPasswordOk(uname, passw):
					self.socket.send("Welcome, " + uname + "\n")
			 	else:
			 		self.socket.send("Incorrect password")
			 		self.socket.close()
			 	self.lock.release()
			else:
				self.socket.send("This username doesn't exist\n")
				self.socket.close()


	def run(self):


		self.authenticate()
		while True:
			c = prompt(self.socket, "napisi nesto \n")
     		self.socket.send(c);
     		
     		