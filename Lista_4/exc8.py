"""  
Gere randomicamente um vetor contendo 14 elementos do tipo inteiro e 
apresente ao usuário.
"""

import random

vetor = [random.randint(0, 100) for _ in range(14)]
print(f"VETOR: {vetor}")