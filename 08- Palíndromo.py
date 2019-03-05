# ESTRUTURAS CONDICIONAIS
# 8 #08 - dígitos palíndromos são aqueles que escritos da direita para esquerda ou da esquerda para direita tem o mesmo valor. Exemplo
#929, 44, 97379. Fazer um algoritmo que dado um dígito de 5 dígitos; calcule e escreva se este é ou não palíndromo.
# 1 = 5
# 2 = 4
# 3 tanto faz

#var
n1 = int(input('1º dígito: '))
n2 = int(input('2º dígito: '))
n3 = int(input('3º dígito: '))
n4 = int(input('4º dígito: '))
n5 = int(input('5º dígito: '))

if n1 == n5 and n2 == n4:
    print('Este algarismo é palíndromo')
else:
    print('Este algarismo não é palíndromo')


