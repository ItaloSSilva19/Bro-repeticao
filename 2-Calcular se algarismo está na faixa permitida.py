# 2 # Calcular se algarismo está na faixa permitida.
print('\nCalcular faixa permitida.')

# def var
alg = float(input('\n Digite um valor entre 1 e 9: '))

# condição
if alg >1:
    if alg >9:
        print('O valor está fora da faixa permitida!')
    else:
        print('O valor está dentro da faixa permitida!')
else:
    print('O valor está fora da faixa permitida!')
