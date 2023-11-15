"""
Processo seletivo Demander

Conversor de número real para número romano
12/11/2023
"""

def inteiro_para_romano(numero):
    dicionario_valores = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 
        90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 
        5: 'V', 4: 'IV', 1: 'I'
    }

    numero_romano = ''
    for valor, simbolo in dicionario_valores.items(): # .items usando para percorrer o dicionário
        while numero >= valor:
            numero_romano += simbolo
            numero -= valor

    return numero_romano

# Troque o valor logo após o '=' para receber um novo resultado
numero_inteiro = 5
numero_romano = inteiro_para_romano(numero_inteiro)
print(f'{numero_inteiro} em numeral romano é: {numero_romano}')