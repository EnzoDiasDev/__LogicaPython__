"""  
Solicite  um  vetor  contendo  6  nomes  e  apresente  a  média  da  quantidade  de 
caracteres.
"""

nomes = []
qtdCaracteres = []

for i in range(6):
    while True:
        nome = input(f"Digite o nome da {i + 1}º pessoa: ").strip().title()

        if not nome.replace(" ", "").isalpha():
            print("Valor inválido.")
        else:
            nomes.append(nome)
            qtdCaracteres.append(len(nome))
            break

media = sum(qtdCaracteres) / len(qtdCaracteres)
print(f"\nMédia da quantidade de caracteres: {media:.2f}")