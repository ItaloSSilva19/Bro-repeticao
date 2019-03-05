'''09 - Desenvolver um algoritmo que determine imposto de renda cobrado de um funcionário pelo governo. Seu programa deverá ler o
número de dependentes, o salário do funcionário e o ((imposto normal pago)-????). O imposto bruto é de 20% do salário do funcionário se o
funcionário ganha mais de 12 salários mínimos; o imposto bruto é de 8% do salário do funcionário se o funcionário ganha mais de 5
salários mínimos; e quem ganha 5 salários mínimos ou menos não é cobrado o imposto de renda. Sabe-se que o governo cobra 4% de
taxa adicional sobre o imposto bruto. Determine o imposto líquido a ser pago pelo funcionário subtraindo R$ 300,00 para cada
dependente do mesmo, no imposto bruto. O programa calculará e imprimirá o imposto a ser pago ou devolvido, que é a diferença entre
o imposto normal descontado e o imposto líquido. Se a diferença for negativa mostrar a mensagem “imposto `a pagar”, caso contrário
“imposto a receber”. Considere o salário mínimo como uma constante no seu programa.'''

################################################################# ESTRUTURAS CONDICIONAIS #######################################################################
# Ler: nº dependentes; sal fun; imposto normal pago(imp_brt + tx).
# Imposto bruto: 20% sal fun if sal fun> 12 sal min; 8% if sal fun if sal fun> 5 sal min; 0% sal fun if sal fun =< 5 sal min
#taxa: 4% sal bruto
#imp liq: sal_brt -(n_dep*300)
#calcular o imposto
#Imprimir o imposto a ser pago ou devolvido
# diferença negativa= imposto a pagar
# contrário: imposto a receber
# sal_min é uma constante.

print('Considere o salário mínimo como R$1000,00 reais')

#variáveis
dep = int(input('Dependentes do funcionário: ')) 
sal_fun = float(input('Salário do funcionário: ')) 

#cálculo imposto bruto
if sal_fun > 12*1000:
    imp_brt = sal_fun*20/100
elif sal_fun > 5*1000:
    imp_brt = sal_fun*8/100 
else:
    imp_brt = 0

#taxa e imposto efetivamente pago
tx = imp_brt*4/100 
imp_pg = imp_brt + tx

#imposto líquido
imp_lqd = imp_brt - (dep*300)

#imposto a ser pago ou devolvido

if imp_lqd < 0:
    print('\nO imposto de', abs(imp_lqd), 'deve ser pago!')
else:
    print('\nO imposto de', imp_lqd, 'deve ser devolvido!')
    

