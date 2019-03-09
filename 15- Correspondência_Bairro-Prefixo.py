'''15 - Fazer um algoritmo que leia os dados de um usuário de telefonia de uma empresa de telecomunicações: bairro e número completo
do telefone e verifique se o número do telefone (Exemplo:32121212) está correto, ou seja, se o prefixo (4 primeiros dígitos) é
correspondente ao bairro especificado. Sabendo-se que os prefixos existem nos bairros conforme a tabela a seguir:

    |Bairro          |Prefixos
    |Oeste           |3223, 3225, 3212,
    |Centro          |3223, 3224, 3212,
    |Sul             |3241, 3242, 3243, 3281
    |Bueno           |3251, 3285
    |Campinas        |3233, 3291'''

#variáveis: bairro; número completo do telefone
# verificar se o número de telefone corresponde ao bairro informado

#definir listas dos prefixos dos bairros:
oeste = [3223, 3225, 3212]
centro = [3223, 3224, 3212]
sul = [3241, 3242, 3243, 3281]
bueno = [3251, 3285]
campinas = [3233, 3291]


# definir variáveis:
telefone = int(input('Digite o número de telefone: '))
bairro = input('Digite o nome do bairro: ')

# converter telefone em string e separar prefixo
telefone = str(telefone)
prefixo = ('{0:.4}'.format(telefone))
prefixo = int(prefixo)

# verificar se bairro informado corresponde ao bairro predefinido:
if bairro == 'Oeste':
    bairro = oeste
elif bairro == 'Centro':
    bairro = centro
elif bairro == 'Sul':
    bairro = sul
elif bairro == 'Bueno':
    bairro = bueno
elif bairro == 'Campinas':
    bairro = campinas
else:
    print('Esse bairro',bairro,' não está incluído em nossa área de cobertura.' )
    exit()

# verificar se o prefixo informado corresponde ao bairro informado

if prefixo in bairro:
    print('O prefixo informado corresponde ao bairro especificado!')
else:
    print('O prefixo informado não corresponde ao bairro especificado!')



