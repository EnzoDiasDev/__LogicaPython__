"""  
Elaborar  um  algoritmo  que  solicite  e  armazene  em  um  vetor,  as  idades  de  7 
pessoas. Posteriormente, apresente a Média das Idades.
"""

idades = []

for _ in range(1, 8):
    idades.append(int(input(f"Digite a idade da {_}º pessoa: ")))

print(f"A média das idades é: {sum(idades) / len(idades)}")
# O USO DA VARIÁVEL _ É APENAS PARA VALORES DESCARTÁVEIS

"""  
# ALTERNATIVA LEVEMENTE MELHORADA

idades = []

for i in range(1, 8):
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))
    idades.append(idade)

media = sum(idades) / len(idades)
print(f"A média das idades é: {media:.2f}")

#---------------------
# USANDO STATISTICS

from statistics import mean

idades = [int(input(f"Idade da {i}ª pessoa: ")) for i in range(1, 8)]
print(f"Média das idades: {mean(idades):.2f}")
"""

