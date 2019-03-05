# 5 # calcular a média ponderada do aluno
print('\nCalcule a média ponderada.')

# definir nome do aluno
aluno = input('\nNome do aluno: ')

# definir notas
p_1 = float(input('Nota da 1ª prova:')) #peso 1
p_2 = float(input('Nota da 2ª prova:')) #peso 2
p_3 = float(input('Nota da 3ª prova:')) #peso 3

# calcular nota
nota = ((p_1*1)+(p_2*2)+(p_3*3))/6

#imprimir nome e nota
print('\nAluno: ', aluno)
print('Média ponderada: ', nota)
