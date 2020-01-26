a=int(input("digite a altura: "))
l=int(input("digite a largura: "))

for i in range(a):
    for j in range(l):
            if((i==0  or i==(a-1)) or ((j==0)or j==(l-1))):
                print("#", end = "")
            else:
                print(" ", end = "")
    print()