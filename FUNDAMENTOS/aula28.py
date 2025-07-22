"""
exercicio
peça ao usuario para digitar seu nome
peça ao usuario para digitar sua idade 
se o nome e idade forem digitados:
    exiba:
        seu nome é {nome}
        seu nome invertido é {nome_invertido}
        se o nome contém (ou não) espaços
        seu nome tem {n} letras
        a primeira letra do seu nome é {letra}
        a última letra do seu nome é {letra}
se nada for digitado em nome e idade :
    exiba "desculpe, você deixou campos vazios.
"""
nome = input('diga seu nome: ')
idade = input('diga a sua idade: ')
nome_invertido = (nome[::-1])

if nome and idade:
    print(f'seu nome é: {nome}')
    print(f'seu nome invertido é: {nome_invertido}')
    print(f'seu nome tem {len(nome)} letras')
    if ' ' in nome:
        print('seu nome tem espaços')
    else:
        print('seu nome não tem espaços')
    
    print(f'a primeira letra do seu nome é:{nome[0]}')
    print(f' a ultima letra do seu nome é: {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')
    

