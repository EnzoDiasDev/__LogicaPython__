"""  
Solicite duas strings e informe se são iguais ignorando maiúsculas/minúsculas.
"""

palavra1 = input("Digite a primeira palavra: ").strip().casefold()
palavra2 = input("Digite a segunda palavra: ").strip().casefold()

if palavra1 == palavra2:
    print("As duas palavras são iguais.")
else:
    print("As duas palavras não são iguais.")

"""  
# VERSÃO MAIS ENXUTA

p1 = input("Digite a primeira palavra: ").strip().casefold()
p2 = input("Digite a segunda palavra: ").strip().casefold()

print("São iguais" if p1 == p2 else "São diferentes")
"""