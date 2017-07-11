#!/usr/bin/python
import os, socket, threading
from connection import Connection

PLAYERFILESDIR = "/home/vanja/Projekti/InitialMUD/res/players/"
PASSWORDSDIR = "/home/vanja/Projekti/InitialMUD/res/passwords/"
HOST = ''
PORT = 23

class Master(object):

	def ifPlayerExists(self, name):
		"""check if the given player name exists in the player
		files dir"""
		exists = False
		plist = os.listdir(PLAYERFILESDIR)
		for p in plist:
			if p == name:
				exists = True
				break
		return exists

	def isPasswordOk(self, name, passw):
		"""check if the password and username pair matches"""
		pf = open(PASSWORDSDIR + name)
		fpassw = pf.readline()
		if fpassw == passw:
			return True
		else:
			return False


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)

master = Master()

while True:
	Connection(s.accept(), master).run()
