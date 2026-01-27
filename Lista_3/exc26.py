"""  
Solicite um nome completo e apresente apenas a primeira palavra.
"""

nome = input("Digite seu nome inteiro:\n").strip().split()
print(f"Seu primeiro nome é: {nome[0]}")

""" 
# VERSÃO MAIS LEGÍVEL

nome = input("Digite seu nome inteiro:\n").strip().split()
print(f"Seu primeiro nome é: {nome[0]}")
"""