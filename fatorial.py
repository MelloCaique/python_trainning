def fatorial(x):
	fat=1
	while x>1:
		fat=fat*x
		x=x-1
	return fat

def teste_fatorial():
	if fatorial(1) == 1:
		print("Funcina para 1")
	else:
		print("Não funciona para 1")
	if fatorial(2) == 2:
		print("Funcina para 2")
	else:
		print("Não funciona para 2")
	if fatorial(0) == 1:
		print("Funcina para 0")
	else:
		print("Não funciona para 0")

teste_fatorial()

n=int(input("Digite um número(n): "))
k=int(input("Digite um número(k): "))

bino=(fatorial(n)/(fatorial(k)*fatorial(n-k)))

print(bino)
