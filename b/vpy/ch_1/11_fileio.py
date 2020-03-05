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

def checkVulns(banner):
	f = open("vuln_banners.txt",'r')
	for line in f.readlines():
		if line.strip('\n') in banner:
			print "[+] Server is vulnerable: "+banner.strip('\n')

def main():
	
	'''
	ftp.cs.brown.edu
	128.148.32.111

	speedtest.tele2.net
	90.130.70.73

	ftp.at.debian.org
	213.129.232.18
	'''

	portList = [21,22,25,80,110,443]

	for x in range(1,255):
		ip = '192.168.65.'+str(x)
		for port in portList:
			banner = retBanner(ip,port)
			if banner:
				print '[+] '+ip+':'+str(port)+" -> "+banner
				checkVulns(banner)


if __name__ == '__main__':
	main()
