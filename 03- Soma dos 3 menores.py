# ESTRUTURAS CONDICIONAIS #
# 3 #
# 4 números distintos -> determinar e somar os 3 menores
# imprimir resultado

#variáveis
n_1 = float(input('Número 1: '))
n_2 = float(input('Número 2: '))
n_3 = float(input('Número 3: '))
n_4 = float(input('Número 4: '))

#distintos e cálculo dos 3 menores
if n_1 == n_2 or n_1 == n_3 or n_1 == n_4: print('É necessário que os números sejam distintos!')
elif n_2 == n_3 or n_2 == n_4: print('É necessário que os números sejam distintos!')
elif n_3 == n_4:print('É necessário que os números sejam distintos!')
else:
    if n_1 > n_2 and n_1 > n_3 and n_1 > n_4:
        res = n_2 + n_3 + n_4
    elif n_2 > n_1 and n_2 > n_3 and n_2 > n_4:
        res = n_1 + n_3 + n_4
    elif n_3 > n_1 and n_3 > n_2 and n_3 > n_4:
        res = n_1 + n_2 + n_4
    else:
        res = n_1 + n_2 + n_3
print('A soma dos três menores é: ',res)
