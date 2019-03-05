# ESTRUTURA CONDICIONAL
# 5 #
# Reajustar o salário do funcionário
# 50% até 350 reais; 30% se acima.

# variável
sal = float(input('Salário: '))

if sal <= 350:
    sal = sal *1.5
else:
    sal = sal * 1.3
print('Salário reajustado é: ',sal)
