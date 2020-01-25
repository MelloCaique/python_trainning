entrada=int(input("Digite o valor de n: "))

cont_impar=0
num=1

while cont_impar<entrada:

	if num%2!=0:
		print(num)
		cont_impar=cont_impar+1
		num=num+1
	else:
		num=num+1



