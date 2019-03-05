# ESTRUTURAS CONDICIONAIS
# 2 #
# LER: CÓDIGO DO ALUNO E SUAS 3 NOTAS;
#CALCULAR: MÉDIA PONDERADA -> MAIOR NOTA = PESO 4, AS DEMAIS = 3;
#EXIBIR: cod aluno; 3 notas; média; APROVADO -> >5 ou REPROVADO.
# A QUESTÃO NÃO DEIXA CLARO O QUE FAZER NO CASO DE NOTAS IGUAIS, POR ISSO,
#ESSA QUESTÃO NÃO FOI LEVADA EM CONSIDERAÇÃO. AGUARDO INSTRUÇÕES FUTURAS.

# Variáveis
aluno = input('Código do aluno: ')
n_1 = float(input('Nota 1: '))
n_2 = float(input('Nota 2: '))
n_3 = float(input('Nota 3: '))

# Classificação da nota em grau e peso  
n_1 = a = float(input('Nota 1: '))
n_2 = b = float(input('Nota 2: '))

if a > b:
  aux = b
  b = a
  a = aux

n_3 = c =float(input('Nota 3: '))
if b > c:
  aux = c
  c = b
  b = aux


#Cálculo da média

med = (n_1 + n_2 + n_3)/10

# APRO OR REPRO
print(aluno)
print ('nota 1: ',n_1,'\nnota 2: ',n_2,'\nnotta 3: ',n_3)
print (med)

if med >= 5:
    print('APROVADO')
else:
    print('REPROVADO')
    

