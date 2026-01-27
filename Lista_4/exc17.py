"""  
Leia  um  vetor  de  10  elementos  (todos  distintos)  e  em  seguida  encontre  e 
apresente  a  posição  do  elemento  N  (informado  pelo  usuário)  no  vetor.  Caso 
não seja encontrado, informe ao usuário sobre a inexistência do mesmo
"""

import random

vetor = random.sample(range(0, 101), 10)
print(f"VETOR: {vetor}\n")

while True:
    try:
        pesquisa = int(input("Digite um número para a pesquisa no vetor (de 0 a 100): "))

        if pesquisa in range(0, 101):
            break
        else:
            print("Digite um valor entre 0 e 100.")

    except ValueError:
        print("Digite um número inteiro.")

encontrado = False

for i, valor in enumerate(vetor):
    if valor == pesquisa:
        print(f"O número {pesquisa} está na posição {i} do vetor!")
        encontrado = True
        break

if not encontrado:
    print("Valor não encontrado.")

"""  
# FORMA MAIS PYTHONICA

import random

vetor = random.sample(range(0, 101), 10)
print(f"VETOR: {vetor}\n")

while True:
    try:
        pesquisa = int(input("Digite um número para a pesquisa no vetor (de 0 a 100): "))

        if pesquisa in range(0, 101):
            break
        else:
            print("Digite um valor entre 0 e 100.")

    except ValueError:
        print("Digite um número inteiro.")

if pesquina in vetor:
    print(f"O número {pesquisa} está na posição {vetor.index(pesquisa)}")
else:
    print("Valor não encontrado.")
"""