entrada_segundos=int(input("Por favor, entre com o número de segundos que deseja converter: "))

dia=entrada_segundos//86400
restante_segundos=entrada_segundos%86400
hora=restante_segundos//3600
restante_segundos=restante_segundos%3600
minuto=restante_segundos//60
restante_segundos=restante_segundos%60
segundo=restante_segundos
#imprimir os valores
print(dia," dias, ",hora," horas, ",minuto," minutos e ",segundo," segundos.")