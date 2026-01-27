"""  
Construir um algoritmo que Leia um vetor de 15 elementos, iniciando a partir do 
último elemento (15º).
"""

vetor = []

for i in range(16):
    valor = int(input(f"Digite o valor do índice {i}: "))
    vetor.append(valor)

print("\nVALORES DO ÚLTIMO PARA O PRIMEIRO:")
for e in vetor[::-1]:
    print(e)