"""  
Solicite uma string com no mínimo 8 caracteres e apresente apenas os 5 primeiros caracteres
"""

while True:
    string = input("Digite uma palavra com pelo menos 8 caracteres: ")

    if len(string) >= 8:
        break
    else:
        print("Tente novamente macaco.\n")

print(f"Os primeiros 5 caracteres da sua palavra são {string[:5]}")