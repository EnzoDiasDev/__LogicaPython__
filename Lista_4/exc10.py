"""  
Gere  randomicamente  um  vetor  contendo  15  elementos  do  tipo  inteiro  (não 
repetidos), solicite um valor ao usuário e efetue uma busca sequencial do valor 
no vetor. Caso encontre, apresente o índice ao qual o valor foi encontrado, caso 
contrário, apresente a mensagem “Valor não localizado”.
"""
"""
import random

vetor = random.sample(range(0, 101), 15)
pesquisa = int(input("Digite um número para saber se ele está no vetor: "))

for i, pesquisa in enumerate(vetor):
    if pesquisa not in vetor:
        print("Valor não localizado.")
    else:
        print(f"O número {pesquisa} está na {i}º posição do vetor.")

# ERRO
"""

import random

vetor = random.sample(range(0, 101), 15)
busca = int(input("Digite um número para saber se ele está no vetor: "))

encontrado = False

for i, valor in enumerate(vetor):
    if valor == busca:
        print(f"O número {busca} está na {i}ª posição do vetor.")
        encontrado = True
        break

if not encontrado:
    print("Valor não localizado.")

print("Vetor:", vetor)

"""  
# FORMA MAIS FÁCIL

import random

vetor = random.sample(range(0, 101), 15)
busca = int(input("Digite um número para saber se ele está no vetor: "))

if busca in vetor:
    print(f"O número {busca} está na posição {vetor.index(busca)}")
else:
    print("Valor não localizado.")
"""