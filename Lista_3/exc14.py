"""  
Solicite uma string sem espaços e valide a informação, pedindo novamente se houver espaço.
"""

while True:
    string = input("Digite uma frase sem espacos: ")

    if " " not in string:
        print("Tudo certo.")
        break
    else:
        print("Tente novamente burro.")