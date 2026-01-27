"""  
Solicite uma string com pelo menos 5 caracteres e confirme o tamanho antes de processar.
"""

while True:
    string = input("Digite uma palavra com pelo menos 5 caracteres: ")

    if len(string) >= 5:
        break
    else:
        print("Tente novamente.\n")