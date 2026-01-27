"""  
Solicite uma palavra e conte quantas letras 'A' ela possui.
"""

palavra = input("Digite uma palavra: ").strip().lower()
print(f"A quantidade de ocorrências da letra 'A' é: {palavra.count('a')}")

"""  
# VERSÃO LEVEMENTE MELHORADA

palavra = input("Digite uma palavra: ").strip().casefold()
qtd = palavra.count("a")

print(f"A letra 'A' aparece {qtd} vezes.")
"""