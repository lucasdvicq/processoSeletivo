"""
Função que pode ser usada para validar se o número romano é valido ou não.
"""

def e_num_romano(s):
    caracteres_validos = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
    return all(caracteres in caracteres_validos for caracteres in s)

numero_romano_invalido = 'XM'
if e_num_romano(numero_romano_invalido):
    print(f'{numero_romano_invalido} é um número romano válido.')
else:
    print(f'{numero_romano_invalido} é um número romano inválido.')