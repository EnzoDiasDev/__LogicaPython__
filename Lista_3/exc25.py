"""  
Solicite uma frase e apresente a primeira letra de cada palavra em maiúsculo
"""

frase = input("Digite uma frase: \n").strip().split()

for i in frase:
    print(i[0].upper())

"""  
# VERSÃO MELHORADA

frase = input("Digite uma frase: ").strip().split()
print("".join(p[0].upper() for p in frase))

# Se for preciso um espaço entre as iniciais, troque os "" do inicio do print para " "
""" 
