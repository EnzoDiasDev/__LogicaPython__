"""  
Solicite uma string e exiba a quantidade de vogais que ela possui.
"""

string = input("Digite alguma coisa: ")
vogais = "aeiouAEIOU"
count = 0

for i in string:
    if i in vogais:
        count += 1

print(f"Quantidade de vogais: {count}")

