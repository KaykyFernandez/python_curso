"""
Faça um programa que peça ao usuario para digitar um número inteiro,
informe se este numero é par ou impar. caso o não digite um número inteiro, informe que não é inteiro.
"""

entrada = input('Digite um número: ')

if entrada.isdigit():
     entrada_int = int(entrada)
     par_impar = entrada_int % 2 == 0
     par_impar_texto = 'ímpar'

     if par_impar:
         par_impar_texto = 'par'

     print(f'O número {entrada_int} é {par_impar_texto}')
else:
     print('Você não digitou um número inteiro')

try:
     entrada_int = float(entrada)
     par_impar = entrada_int % 2 == 0
     par_impar_texto = 'ímpar'

     if par_impar:
         par_impar_texto = 'par'

     print(f'O número {entrada_int} é {par_impar_texto}')
except:
     print('Você não digitou um número inteiro')


"""
faça um programa que pergunte a hor ao usuario e, baseando-se no horario
descrito, exiba a saudação apropriada. EX.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')

"""
faça um programa que peça o primeiro nome do usuario. se o nome tiver 4 letras ou menos escreva "seu nome é curto"; se tiver 5 e 6 letras,
escreva "seu nome é normal"; se for maior que 6 escreva "seu nome é muito grande".
"""
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')