"""  
Gere  randomicamente  um  vetor  contendo  20  elementos  do  tipo  inteiro  (não 
repetidos) e apresente ao usuário.
"""

"""
import random

vetor = []
vetor = [random.randint(0, 100) for i in range(20) if i not in vetor]
print(f"VETOR: {vetor}")

# DEU RUIM
"""

#FORMA MAIS PYTHONICA

import random

vetor = random.sample(range(0, 101), 20)
# random.sample = escolhe elementos sem repetição
print("VETOR:", vetor)

"""  
# FORMA CORRETA E SIMPLES
import random

vetor = []

while len(vetor) < 20:
    numero = random.randint(0, 100)
    if numero not in vetor:
        vetor.append(numero)

print("VETOR:", vetor)
"""
