"""  
Solicite ao usuário dois vetores de 7 números e em seguida calcule a soma dos 
vetores, elemento a elemento (de mesmo índice), armazenando em um terceiro 
vetor de índice equivalente.
"""

vetor1 = []
vetor2 = []
vetor3 = [] # Vetor de soma

for i in range(14): 
    while True:
        try:
            if i <= 6:
                numero = int(input(f"Digite um número para ser adicionado na {i + 1}º do primeiro vetor: "))
            else:
                numero = int(input(f"Digite um número para ser adicionado na {i - 6}º do segundo vetor: "))       
            
            if not str(numero).isdigit():
                print("Digite apenas números.")
            else:
                if i <= 6:
                    vetor1.append(numero)
                else:
                    vetor2.append(numero)  
                break      
        except ValueError:
            print("Digite apenas números.")

for i in range(len(vetor1)):
    vetor3.append(vetor1[i] + vetor2[i])

print(f"Vetor de soma: {vetor3}")

"""  
# VERSÃO MELHORADA

vetor1 = []
vetor2 = []
vetor3 = []

for i in range(14):
    while True:
        try:
            if i < 7:
                numero = int(input(f"Digite o {i + 1}º número do primeiro vetor: "))
                vetor1.append(numero)
            else:
                numero = int(input(f"Digite o {i - 6}º número do segundo vetor: "))
                vetor2.append(numero)
            break
        except ValueError:
            print("Digite apenas números inteiros.")

for i in range(len(vetor1)):
    vetor3.append(vetor1[i] + vetor2[i])

print(f"Vetor 1: {vetor1}")
print(f"Vetor 2: {vetor2}")
print(f"Vetor soma: {vetor3}")

# OU

vetor1 = []
vetor2 = []

for i in range(7):
    while True:
        try:
            vetor1.append(int(input(f"Digite o {i + 1}º número do primeiro vetor: ")))
            break
        except ValueError:
            print("Digite apenas números inteiros.")

for i in range(7):
    while True:
        try:
            vetor2.append(int(input(f"Digite o {i + 1}º número do segundo vetor: ")))
            break
        except ValueError:
            print("Digite apenas números inteiros.")

vetor3 = [v1 + v2 for v1, v2 in zip(vetor1, vetor2)]

print(f"Vetor soma: {vetor3}")
"""