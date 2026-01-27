"""  
Solicite um número inteiro entre 100 e 10000 e exiba apenas os dois primeiros dígitos
"""

while True:
    string = input("Digite um número entre 100 e 10000: ")

    if string.isdigit() and int(string) >= 100 and int(string) <= 10000:
        break
    else:
        print("Resposta inválida.")

print(f"Os primeiros 3 digitos do seu número são: {string[:3]}")