"""  
Solicite um número inteiro e converta-o em string, depois apresente seus dígitos ao contrário.
"""

numero = int(input("Digite um número: "))
numeroString = str(numero)
numeroString = numeroString[::-1]

print(numeroString)

"""  
# VERSÃO LEVEMENTE MELHORADA

numero = int(input("Digite um número: "))
numeroString = str(numero)[::-1]

print(numeroString)
"""