entrada=int(input("Digite o valor de n: "))

if entrada==0:
	print(1)
else:
	cont=1
	fat=1
	while(cont<=entrada):
		fat=fat*cont
		cont=cont+1
	print(fat)