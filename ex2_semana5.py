def maior_primo(x):
	#x=int(input("Digite um número:  "))
	if x>2:
		primo=0
		while(primo==0):
			tot=0
			for c in range (1,x+1):
				if x%c==0:
					tot+=1
			if tot==2:
				primo=1
				#print("PRIMO")
				#print(x)
				return x
			else:
				primo=0
				x=x-1
				#print("NÃO PRIMO")
	else:
		print("Numero tem que ser maior que 2")