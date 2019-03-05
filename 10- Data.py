#10 - Desenvolver um algoritmo para receber uma data e consisti-la. Consistir uma data significa verificar se esta é válida.

#var
dia = int(input('Dia: '))
mes = int(input('Mês: '))
mil = int(input('Milênio: '))
sec = int(input('Século: '))
dec = int(input('Década: '))
ano = int(input('Ano: '))


if dia <=0 or dia >31:
    print('Data inválida!')
elif mes <=0 or mes > 12:
    print('Data inválida!')
else:
    print(dia,'/',mes,'/',mil,sec,dec,ano)
