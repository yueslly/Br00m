def ports():
	portas_top10 = [21,22,23,25,53,80,110,139,443,445]
	portas_top20 = [21,22,23,25,53,80,110,135,139,143,443,445,993,995,1723,2222,3306,3389,5900,8080,8291]
	portas_top30 = [21,22,23,25,80,110,135,139,143,443,445,993,995,1723,2222,3306,3389,5900,5060,5666,6001,8000,8008,8080,8291,8443,8888,10000,32768,49152,49154]
	
	print("Selecione uma das listas de portas disponíveis:")
	print("1 - Lista top 10")
	print("2 - Lista top 20")
	print("3 - Lista top 30")
	escolha = input("\n>>>")

	lista = []
	
	if (escolha == "1"):
		lista = portas_top10
		return lista
	elif (escolha == "2"):
		lista = portas_top20
		return lista
	else:
		lista = portas_top30
		return lista