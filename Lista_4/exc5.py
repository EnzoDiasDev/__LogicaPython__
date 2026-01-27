"""  
Construir um algoritmo que Leia um vetor de 8 elementos (V1) e preencha um 
outro (V2) em ordem inversa.
"""
vetor = []
vetorInv = []

for i in range(8):
    vetor.append(int(input(f"Digite o valor da {i + 1}º posição do vetor: ")))

for i in vetor[::-1]:
    vetorInv.append(i)

print(f"VETOR ORIGINAL: {vetor}")
print(f"VETOR INVERTIDO: {vetorInv}")

"""  
# VERSÃO MAIS SIMPLES

vetor = [int(input(f"Digite o {i + 1}º valor: ")) for i in range(8)]
vetor_invertido = vetor[::-1]

print("Vetor original:", vetor)
print("Vetor invertido:", vetor_invertido)
"""