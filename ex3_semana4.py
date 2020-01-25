entrada=input("Digite um número inteiro: ")


tamanho=len(entrada)
n=int(entrada)

cont=1
adicionar=0
soma=0

while cont<=tamanho:
	adicionar=n%10
	soma=soma+adicionar
	n=n//10
	cont=cont+1

print(soma)