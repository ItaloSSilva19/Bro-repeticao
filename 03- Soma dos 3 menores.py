# ESTRUTURAS CONDICIONAIS #
# 3 #
# 4 números distintos -> determinar e somar os 3 menores
# imprimir resultado

#variáveis
n1 = float(input('Número 1: '))
n2 = float(input('Número 2: '))
n3 = float(input('Número 3: '))
n4 = float(input('Número 4: '))

# n1 tem que ser maior que n2 e o resto
# n2 tem que ser maior que n3 e n4
# n3 tem que ser maior que n4
# n4 é o menor

if n1 > n2:
    aux = n2
    n1 = n2
    n2 = aux
    
if n2 > n3:
    aux = n3
    n2 = n3
    n3 = aux
    
if n3 > n4:
    aux = n3
    n3 = n4
    n4 = aux

res = (n1 + n2 + n3)
print('A soma dos três menores é: ',res)
