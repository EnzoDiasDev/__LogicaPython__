"""  
Solicite uma string com mínimo 5 e máximo 20 caracteres e exiba os 3 últimos caracteres
"""

while True:
    string = input("Digite uma palavra/frase com mínimo 5 e máximo 20 caracteres: ").strip()

    if len(string) >= 5 and len(string) <= 20:
        break
    else:
        print("Tente novamente mamute.")

print(f"Os três últimos caracteres da palavra/frase são: {string[3:]}")