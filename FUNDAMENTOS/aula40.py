""" Calculadora com while"""

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um desse operadores (+-/*): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print(' Um ou ambos os números não são inválidos!')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('o operador digitado não é válido')
        continue

    if len(operador) > 1:
        print('um operador por vez!')
        continue
    ######
    if operador =='+':
        print(f'{numero_1} + {numero_2} = ',num_1_float + num_2_float)

    elif operador == '-':
        print(f'{numero_1} - {numero_2} = ',num_1_float - num_2_float)

    elif operador == '/':
        print(f'{numero_1} / {numero_2} = ',num_1_float / num_2_float)

    elif operador == '*':
        print(f'{numero_1} * {numero_2} = ',num_1_float * num_2_float)

    sair = input('quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break