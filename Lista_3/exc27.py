"""  
Solicite um nome completo e apresente apenas o último sobrenome.
"""

sobrenome = input("Digite seu nome inteiro: ").strip().split()
print(f"Seu último sobrenome é: {sobrenome[-1]}")

"""  
# VERSÃO MAIS ENXUTA

print(input("Digite seu nome: ").strip().split()[-1])
"""