"""
CPF: 746.824.890-70
colete a soma dos 9 primeiros digitos do CPF
multiplicando cada  um dos valores por ua contagem regressiva começando de 10
EX : 746.824.890-70 (746824890)
    10 9  8  7  6  5  4  3  2 
  * 7  4  6  8  2  4  8  9  0
    70 36 48 56 12 20 32 27 0
    
somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
multiplicando o resultado anterior por 10
301 * 10 = 3010
obter o rsto da divisão da conta anterior por 11
3010 % 11 = 7
se o resultado anterior for maior que 9:
resultado é 0
contrário disso:
"""
cpf = '18673970059'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10
resultado_1 = 0


for digito in nove_digitos:
    resultado_1 += int(digito)  * contador_regressivo_1
    print(resultado_1)
    contador_regressivo_1 -= 1
    

print(f'resultado {resultado_1}')
digito_1 = (resultado_1 * 10) % 11
print(digito_1)
digito_1 = digito_1 if digito_1 >= 9 else 0
print(digito_1)
