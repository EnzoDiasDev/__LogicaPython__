""" 
Solicite uma string e exiba apenas as vogais, uma por linha.
"""

string = input("Digite uma palavra: ")
letras = "aeioAEIOU"

for i in string:
    if i in letras:
        print(i)