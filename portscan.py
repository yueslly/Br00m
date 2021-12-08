import sys, socket

def portscan(porta_alvo):
	ip = input("Informe o HOST alvo:")
	print("Varrendo HOST:",ip)
	for porta in porta_alvo:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(0.5)
		if (sock.connect_ex((ip,porta)) == 0):
			print("[+] Porta aberta:",porta)
			sock.close()