import socket

def retBanner(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip,port))
		banner = s.recv(1024)
		return banner
	except Exception, e:
		return 'Error conexion: '+str(e) 

def main():
	
	'''
	ftp.cs.brown.edu
	128.148.32.111

	speedtest.tele2.net
	90.130.70.73
	'''

	ip1 = '128.148.32.111'
	ip2 = '90.130.70.73'
	port = 21
	
	banner1 = retBanner(ip1,port)

	if 'Error conexion' in banner1:
		print ip1+':'+str(port)+' -> '+banner1
	else:
		if banner1:
			print '[+] '+ip1+': '+banner1

	banner2 = retBanner(ip2,port)
	
	if 'Error conexion' in banner2:
		print ip2+':'+str(port)+' -> '+banner2
	else:
		if banner2:
			print '[+] '+ip2+': '+banner2

if __name__ == '__main__':
	main()
