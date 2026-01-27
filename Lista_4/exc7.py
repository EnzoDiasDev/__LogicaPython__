"""  
Solicite  ao  usuário  5  números  inteiros,  guarde-os  em  um  vetor  e  em  seguida 
apresente-os  ao  usuário.  Finalmente,  apresente  também  quantos  elementos 
são negativos.
"""

negativos = 0
vetor = [int(input(f"Digite o {i + 1}º número inteiro: ")) for i in range(5)]

for nums in vetor:
    if nums < 0:
        negativos += 1

print(f"Lista dos números: {vetor}")
print(f"Números negativos: {negativos}")

"""  
# FORMA MAIS PYTHONICA

vetor = [int(input(f"Digite o {i + 1}º número inteiro: ")) for i in range(5)]
negativos = sum(1 for n in vetor if n < 0)

print("Lista dos números:", vetor)
print("Quantidade de negativos:", negativos)
"""