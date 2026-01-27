"""  
Gere uma sequência aleatória contendo: 4 vogais minúsculas, 2 vogais maiúsculas, 3 consoantes 
maiúsculas e 3 números.
"""

import random 

senha = ""
vogais = "aeiouAEIOU"

for i in range(4):
    while True:
        num = random.randint(97, 122)

        if chr(num) in vogais:
            senha += chr(num)
            break

for i in range(2):
    while True:
        num = random.randint(65, 90)

        if chr(num) in vogais:
            senha += chr(num)
            break

for i in range(3):
    while True:
        num = random.randint(65, 90)

        if chr(num) not in vogais:
            senha += chr(num)
            break

for i in range(3):
    senha += str(random.randint(0, 9))

print(senha)

"""  
import random

vogais_min = "aeiou"
vogais_mai = "AEIOU"
consoantes_mai = "BCDFGHJKLMNPQRSTVWXYZ"
numeros = "0123456789"

senha = []

# 4 vogais minúsculas
senha += random.choices(vogais_min, k=4)

# 2 vogais maiúsculas
senha += random.choices(vogais_mai, k=2)

# 3 consoantes maiúsculas
senha += random.choices(consoantes_mai, k=3)

# 3 números
senha += random.choices(numeros, k=3)
"""