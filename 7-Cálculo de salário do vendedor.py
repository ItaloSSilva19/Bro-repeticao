# 7 # Cálculo de salário do vendedor

print('\nCálculo de salário.')

# def var
nome = input('\nVendedor: ')
sal_fix = float(input('Salário fixo: '))
vendas = float(input('Total de vendas: '))

# cálculos - comissão e salário total
comissao = 0.15 * vendas
sal_tot = sal_fix + comissao

# resultado
print('\nNome vendedor:',nome)
print('Salário fixo:',sal_fix)
print('Salário total:',sal_tot)
