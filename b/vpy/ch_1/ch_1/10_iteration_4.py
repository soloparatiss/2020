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
        if 'Error conexion' in banner:
                return
        elif 'FreeFloat Ftp Server (Version 1.00)' in banner:
                print '[+] FreeFloat FTP Server is vulnerable'
        elif '3Com 3CDaemon FTP Server Version 2.0' in banner:
                print '[+] 3CDaemon FTP Server is vulnerable'
        elif 'Ability Server 2.34' in banner:
                print '[+] Ability FTP Server is vulnerable'
        elif 'Sami FTP Server 2.0.2' in banner:
                print '[+] Sami FTP Server is vulnerable'
        else:
                print '[-] FTP Server is not vulnerable'
        return

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
		ip = '192.168.95.'+str(x)
		for port in portList:
			banner = retBanner(ip,port)
			if banner:
				print '[+] '+ip+':'+str(port)+" -> "+banner
				checkVulns(banner)


if __name__ == '__main__':
	main()
