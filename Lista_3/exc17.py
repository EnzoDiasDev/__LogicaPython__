"""  
Gere e exiba uma sequência aleatória de caracteres.
"""

import random

string = ""

for i in range(10):
    num = random.choice([
        random.randint(65, 90),
        random.randint(97, 122)
    ])
    string += chr(num)

print(f"Palavra aleatória:\n{string}")