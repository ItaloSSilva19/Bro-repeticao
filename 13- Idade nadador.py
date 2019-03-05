'''13 - Fazer um algoritmo que receba a idade e o nome de um nadador e imprima o seu nome, a sua idade e a categoria do mesmo, de
acordo com as regras a seguir:

Categoria Idade
Infantil A 5 à 7 anos
Infantil B 8 à 10 anos
Juvenil A 11 à 13 anos
Juvenil B 14 à 17 anos
Sênior À partir de 18 anos'''

#receber: idade e nome do nadador
#Imprimir: nome; idade; categoria

# definição das variáveis
nome_nadador = input('Digite o nome do nadador: ')
idade_nadador = int(input('Digite a idade do nadador: '))

#Constituir as categorias
if idade_nadador < 5:
    print('Não pode participar da natação!')
    categoria = 'NENHUMA'
elif idade_nadador >= 5 and idade_nadador <= 7:
    categoria = 'Infantil A'
elif idade_nadador >=8 and idade_nadador <= 10:
    categoria = 'Infantil B'
elif idade_nadador >=11 and idade_nadador <= 13:
    categoria = 'Juvenil A'
elif idade_nadador >=14 and idade_nadador <=17:
    categoria = 'Juvenil B'
else:
    categoria = 'Sênior'

#output
print('Nome: ',nome_nadador,'\nIdade:',idade_nadador,'\nCategoria',categoria)
