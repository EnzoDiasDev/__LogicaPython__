"""  
Solicite uma frase e exiba o caractere de maior valor ASCII.
"""

string = input("Digitee uma frase: ")
maiorASCII = 0
letraMaiorASCII = ""

for i in string:
    if ord(i) > maiorASCII:
        maiorASCII = ord(i)
        letraMaiorASCII = i

print(f"MAIOR ASCII: {maiorASCII}, {letraMaiorASCII}")