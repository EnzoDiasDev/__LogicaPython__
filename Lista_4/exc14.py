"""  
Gere randomicamente um vetor com 15 elementos numéricos entre 5 e 75 (não 
repetidos) e gere um segundo vetor contendo a informação “par” ou “impar” de 
acordo com o valor de cada elemento do primeiro vetor. Finalmente, apresente 
os dois vetores, lado a lado.
"""

import random

numeros = random.sample(range(5, 76), 15)
parOuImpar = []

for i in numeros:
    if i % 2 == 0:
        parOuImpar.append("Par")
    else:
        parOuImpar.append("Ímpar")

for numero, classificacao in zip(numeros, parOuImpar):
    print(f"Número: {numero:<2} | {classificacao}")

"""  
# ALTERNATIVA MAIS ENXUTA

import random

numeros = random.sample(range(5, 76), 15)
par_ou_impar = ["Par" if n % 2 == 0 else "Ímpar" for n in numeros]

for numero, classificacao in zip(numeros, parOuImpar):
    print(f"Número: {numero:<2} | {classificacao}")
"""