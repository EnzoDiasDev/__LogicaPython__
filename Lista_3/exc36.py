"""  
Solicite um número inteiro e some-o com sua versão invertida repetidamente até que o resultado seja um 
número capicua (palíndromo numérico). Ao final, apresente o resultado e a quantidade de somas 
realizadas.
"""

numero = input("Digite um número: ").strip()
somas = 0

if numero == numero[::-1]:
    print(f"Capicua: {numero}\nQuantidade de somas: 0")
else:
    while numero != numero[::-1]:
        inverso = numero[::-1]
        numero = str(int(numero) + int(inverso))
        somas += 1

    print(f"Capicua: {numero}\nQuantidade de somas: {somas}")

"""  
# VERSÃO MELHORADA

numero = input("Digite um número: ").strip()
somas = 0

while numero != numero[::-1]:
    inverso = numero[::-1]
    numero = str(int(numero) + int(inverso))
    somas += 1

print(f"Capicua: {numero}")
print(f"Quantidade de somas: {somas}")
"""
