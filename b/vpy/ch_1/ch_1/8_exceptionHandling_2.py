import socket
socket.setdefaulttimeout(2)
s = socket.socket()
try:
	s.connect(("192.168.10.1",21))
except Exception, e:
	print "[-] Error = "+str(e)
