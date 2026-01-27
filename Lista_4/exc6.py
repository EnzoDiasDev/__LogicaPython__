"""  
Faça  um  algoritmo  que  Leia  um  vetor  (V1)  de  10  elementos  numéricos  e 
preencha um outro (V2) contendo em cada célula, o dobro de V1. Em seguida, 
preencha um terceiro vetor (V3) contendo em cada célula a metade de V1
"""

v1 = [int(input(f"Digite o valor da {i + 1}º posição: ")) for i in range(10)]
v2 = [x * 2 for x in v1]
v3 = [x / 2 for x in v1]

print(f"V1 = {v1}")
print(f"V2 = {v2}")
print(f"V3 = {v3}")

# Se for necessário apenas valores inteiros para o V3, utilize:
# v3 = [valor // 2 for valor in v1]

"""  
v1, v2, v3 = [], [], []

for i in range(10):
    valor = int(input(f"Digite o valor da {i + 1}ª posição: "))
    v1.append(valor)
    v2.append(valor * 2)
    v3.append(valor / 2)
"""