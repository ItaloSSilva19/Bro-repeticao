# ESTRUTURA CONDICIONAL
# 5 #
# Reajustar o salário do funcionário
# 50% até 350 reais; 30% se acima.

# variável
sal = float(input('Salário: '))

if sal <= 350:
    sal = sal + sal*50/100
else:
    sal = sal + sal*30/100
print('Salário reajustado é: ',sal)
