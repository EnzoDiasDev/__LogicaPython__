"""  
Construa um algoritmo que solicite um vetor de 6 elementos inteiros maiores ou 
iguais a zero (V1) e em seguida preencha mais dois vetores (V2 e V3) onde V2 
armazenará os elementos ímpares de V1 e V3 os elementos pares também de V1.
"""
"""
v1 = []
v2 = []
v3 = []

for i in range(6):
    while True:
        numero = int(input(f"Digite o valor do {i + 1}º elemento: ")) 

        if numero >= 0:
            v1.append(numero)
            break
        else:
            print("Valor inválido.")

for numero in v1:
    if numero % 2 == 0:
        v3.append(numero)
    else:
        v2.append(numero)
"""

# VERSÃO MELHORADA

v1 = []
v2 = []
v3 = []  

for i in range(6):
    while True:
        try:
            numero = int(input(f"Digite o valor do {i + 1}º elemento: "))

            if numero >= 0:
                v1.append(numero)
                break
            else:
                print("Digite um número maior ou igual a zero.")

        except ValueError:
            print("Digite um número inteiro.")

for numero in v1:
    if numero % 2 == 0:
        v3.append(numero)
    else:
        v2.append(numero)   

print(f"\nV1: {v1}")
print(f"V2 (ímpares): {v2}")
print(f"V3 (pares): {v3}")
