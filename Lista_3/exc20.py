""" 
Solicite um nome completo e apresente apenas a primeira palavra.
"""

nomeInteiro = input("Digite o seu nome: ")
nome = nomeInteiro.split(" ", -1)[0]

print(f"Seu primeiro nome é: {nome}")

# MÉTODO MAIS SIMPLES
# print(input("Digite o nome: ").strip().split()[0])

"""  
VERSÃO MELHORADA DO CÓDIGO

nome_completo = input("Digite o seu nome: ").strip()
primeiro_nome = nome_completo.split()[0]

print(f"Seu primeiro nome é: {primeiro_nome}")


OU PODE SER TAMBÉM


nome = input("Digite o seu nome: ").strip()
primeiro_nome = nome.partition(" ")[0]

print(f"Seu primeiro nome é: {primeiro_nome}")
"""