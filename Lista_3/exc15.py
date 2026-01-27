""" 
Solicite uma palavra e informe se ela é ou não um palíndromo (ex.: "ANA", “REVIVER”):
"""

string = input("Digite uma palavra: ")
stringInversa = string[::-1]

if string == stringInversa:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")