import sys, socket

def portscan():
	ip = input("Informe o HOST alvo:")
	porta = int(input("Informe a porta alvo:"))
	print("Varrendo HOST:",ip)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.setdefaulttimeout(0.5)
	if (sock.connect_ex((ip,porta)) == 0):
		print("[+] Porta aberta:",porta)
		sock.close()