"""  
Ler um vetor com 21 elementos numéricos, e apresentar ao usuário os 
elementos em ordem inversa ao da entrada.
"""

"""
vetor = [x + 1 for x in range(21)]
print(vetor[::-1])
"""

import random

vetor = [random.randint(0, 100) for _ in range(21)]
print(f"VETOR ORIGINAL: {vetor}")
print(f"VETOR INVERTIDO: {vetor[::-1]}")
