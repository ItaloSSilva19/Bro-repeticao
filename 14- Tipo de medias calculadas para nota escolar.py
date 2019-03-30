'''14 - Um usuário deseja um algoritmo onde ele possa escolher o tipo de média que deseja calcular a partir de 3 notas. Faça um
algoritmo que leia as notas, sua opção escolhida e calcule a média.

(1) aritmética;                             (4) geométrica
(2) ponderada (3,3,4);                      (5) quadrática.
(3) harmônica'''

# média aritmética: razão entre a soma dos elementos(a;b;c;) pela quantidade de elementos(n). Ex.: (a + b + c)/n;
# média ponderada: razão entre o produto da soma dos elementos e respectivos pesos pela soma dos pesos. Ex.: (xa + yb + zc)/n;
# média harmônica: razão entre a quantidade de elementos pela soma do inverso dos elementos. Ex.: n/((1/a)+(1/b)+(1/c));
# média geométrica: multiplica todos os elementos dentro da raiz de índice da quantidade de elementos. Ex.: (abc)**(1/n);
# média quadrática: razão entre a soma dos quadrado dos elementos pela quantidade de elementos dentro da raiz quadrada. Ex.: math.sqrt(((a**2)+(b**2)+(c**2))/n)

###################################################################################################################################################################

#variáveis:
nota_1 = float(input('Digite a 1ª nota: '))
nota_2 = float(input('Digite a 2ª nota: '))
nota_3 = float(input('Digite a última nota: '))
escolha_media = input('Qual tipo de média? [Aritmética; Ponderada; Harmônica; Geométrica; Quadrática]: ')

# cálculo da média escolhida:
if escolha_media == 'Aritmética':
    media_aritmetica = (nota_1 + nota_2 + nota_3)/ 3 # cálculo da média aritmética;
    print('A média aritmética das notas é: ', media_aritmetica)
elif escolha_media == 'Ponderada':
    media_ponderada = (3*nota_1 + 3*nota_2 + 4*nota_3)/10 # cálculo da média ponderada;
    print('A média ponderada das notas é: ', media_ponderada)
elif escolha_media == 'Harmônica':
    media_harmonica = 3/((1/nota_1)+(1/nota_2)+(1/nota_3)) # cálculo da média harmônica;
    print('A média harmônica das notas é: ', media_harmonica)
elif escolha_media == 'Geométrica':
    media_geometrica = (nota_1*nota_2*nota_3)**(1/3) # cálculo da média geométrica;
    print('A média geométrica das notas é: ', media_geometrica)
elif escolha_media == 'Quadrática':
    media_quadratica = (((nota_1**2)+(nota_2**2)+(nota_3**2))/3)**(1/2) # cálculo da média quadrática;
    print('A média quadrática das notas é: ', media_quadratica)
else:
    print('Tipo de média desconhecido! \nNão é possível realizar o cálculo!')
    
    





