"""  
Construir  algoritmo  que  Leia  um  vetor  de  10  elementos  e  posteriormente 
apresente a soma dos mesmos.
"""

numeros = []

for _ in range(10):
    numeros.append(int(input(f"Digite o {_ + 1}º número: ")))

print(f"SOMA DE TODOS OS NÚMEROS É: {sum(numeros)}")