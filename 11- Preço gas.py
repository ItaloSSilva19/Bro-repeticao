'''11-A distribuidora de combustíveis Ave Maria irá aumentar o combustível em função da quantidade comprada anualmente por seus
clientes. Os postos que consomem em média até 50.000 litros de combustível mês, t erão aumento de 20%. Os postos que consomem
acima desta média, 12% de aumento. A distribuidora irá fornecer o nome do posto e seu consumo anual. Calcule e escreva qual será o
preço do litro de combustível para o posto, considerando-se que hoje a distribuidora cobra R$2,13 por litro.'''

#posto consome <= 50000 l/m +20%; acima, +12%
# fornecer: nome e consumo anual do posto.
# print preço do litro.
# distribuidora cobra antes do aumento 2,13 por litro

#def var
nome_pst = input('Digite o nome do posto: ')
cons = float(input('Digite o consumo anual(em litro): '))/12
preco_gas = float(2.13)

#Calculo preço
if cons >0 and cons <= 50000:
    preco_gas = preco_gas + preco_gas *12/100
else:
    preco_gas = preco_gas + preco_gas*20/100
print('Posto: ',nome_pst,'\nPreço da Gasolina: ',preco_gas)    
