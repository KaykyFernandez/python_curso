"""
introdução às funções (def) em python
funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retorna um valor especifico.
por padrão, funções Python retornan None (nada)"""

def imprimir(a, b, c):
    print(a, b, c)
   

imprimir(1,2,3)
imprimir(4,5,6)


def saudacao(nome):
    print(f'Olá {nome}!')

saudacao('Kayky Fernandez')
saudacao('Flavia Bulla')
