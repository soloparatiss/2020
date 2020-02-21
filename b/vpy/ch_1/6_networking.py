import socket
socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("192.168.10.1",21))
ans = s.recv(1024)
print ans
