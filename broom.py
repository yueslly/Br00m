import sys, socket

ip = "192.168.5.1"

print("BR00M -- PortScanner by Yueslly Lisboa")

print("Varrendo HOST:",ip)

for porta in range(1,1025):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.setdefaulttimeout(0.5)
	if (sock.connect_ex((ip,porta)) == 0):
		print("[+] Porta aberta:",porta)
		sock.close()