#!/usr/bin/python

def receive(sock):
	"""receive and return message from socket"""
	buf = []
	while True:
		data = sock.recv(256)
		if not data:
			break
		buf.append(data)
	return ''.join (buf)

def prompt(sock, mesg):
	"""send a prompt to socket"""
	sock.send(mesg)
	return receive(sock)