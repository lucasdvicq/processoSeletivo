"""
Processo seletivo Demander

Conversor de número romano para número real
12/11/2023
"""

def romano_para_inteiro(s):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    resultado = 0

    for indice, atual in enumerate(s): # 'S' parâmetro usado para para receber uma string que representa um número em algarismo romano
        if indice > 0 and valores[atual] > valores[s[indice - 1]]:
            resultado += valores[atual] - 2 * valores[s[indice - 1]]
        else:
            resultado += valores[atual]

    return resultado

# Troque o valor entre os '' para receber um novo resultado
numero_romano = 'V'
numero_inteiro = romano_para_inteiro(numero_romano)
print(f'{numero_romano} em número inteiro é: {numero_inteiro}')

