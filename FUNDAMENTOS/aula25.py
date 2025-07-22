"""
interpolação é básica de strings
s - string
d e i = int 
f - float
x e X - hexadecimal (ABCDEF0123456789)
"""


nome = 'kayky'
preco = 1000.958956
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('o hexadecimal de %d é %08X' % (1500, 1500))