'''16 - A cidade de Perdiz das Cruzes possui um único posto telefônico. Por este posto são feitas todas as ligações interurbanos da
cidade. O valor a ser pago é calculado de acordo com as seguintes regras a seguir:
• Taxa de R$2,00 pela ligação mais R$ 1,00 para os 3 primeiros minutos;
• Acima do três primeiros minutos as regras são de R$ 2,15 para cada intervalo de 5 minutos e R$ 0,85 para cada
minuto abaixo disto.
A telefonista irá fornecer o nome do usuário e o tempo da ligação em minutos. O algoritmo deverá calcular o valor a ser pago e
escrever o nome do usuário e o valor da conta.'''

#variáveis: nome do usuário e o tempo de ligação(min).
# regras de preço:
#                   2,00 + 1,00 até os 3 primeiros minutos;
#                   Após isso: 2,15 para cada 5 minutos e 0,85 para cada minuto < 5
# se o tempo é até 3 minutos: 2+ (tempo)
# se o tempo é de maior que 3 e divisível por 5: 2,15* (tempo/5)
# se o tempo é maior que 3 e não é divisível por 5: (int(tempo/5)*2,15) + ((tempo%5)*0,85)

#definir variáveis
nome_usuario = input('Digite o nome do usuário: ')
minutos = int(input('Digite o tempo de ligação em minutos: '))#foi desconsiderado float como opção pois a questão não trata do preço da fração do minuto.

#Cálculo do preço
if minutos > 0 and minutos <= 3:
    valor_conta = 2 + minutos
elif minutos > 3:
    if minutos%5 == 0:
        valor_conta = 2.15 * (minutos / 5)
    elif minutos%5 != 0:
        valor_conta = 2.15 * (minutos /5) + (minutos%5)* 0.85
else:
    print('Tempo inválido')

#impressão dos resultados.
print('Usuário: ',nome_usuario)
print('Valor da conta: ',valor_conta)
