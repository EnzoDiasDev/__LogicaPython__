"""  
Solicite um nome completo e apresente apenas o último sobrenome.
"""

nome = input("Digite o nome: ").strip().split()
sobrenome = nome[len(nome) - 1]

print(f"Seu último sobrenome é: {sobrenome}")

"""
FORMA MELHORADA

sobrenome = input("Digite o nome: ").strip().split()[-1]
print(f"Seu último sobrenome é: {sobrenome}")

FORMA MAIS CURTA

print(input("Digite o nome: ").strip().split()[-1])
"""