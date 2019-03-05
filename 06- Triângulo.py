# ESTRUTURAS CONDICIONAIS
# 6 #
# Três valores: A, B, C.
# Verificar se formam um triângulo.
# se formar: imprimir se é: equilátero, isósceles ou escaleno.

#OBS.: um triângulo não pode ter um dos lados maior do que a soma dos outros 2 lados.

# variáveis

A = float(input('Lado A: '))
B = float(input('Lado B: '))
C = float(input('Lado C: '))

# verificar se é um triângulo e de qual tipo
if A > B+C or B > A+C or C > A+B:
    print('\nNão é um triângulo!')
else:
    if A == B and B == C:
        print('É um triângulo equilátero!')
    elif A == B or A == C or B == C:
        print('É um triângulo isósceles!')
    else:
        print('É um triângulo escaleno!')
