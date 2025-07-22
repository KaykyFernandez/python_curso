"""
repetições
while (enquanto)
executa uma ação enquanto uma condição for verdadeira
loop infinito - > quando um código não tem fim
"""
condicao = True

while condicao :
    nome = input('diga seu nome: ')
    print(f'seu nome é {nome}')
    
    if nome == 'sair':
        break

print('acabou')