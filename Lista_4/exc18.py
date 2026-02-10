"""
Construa  um  algoritmo  que  solicite  10  nomes  e  os  armazene  em  um  vetor,  e 
posteriormente apresente o Maior nome, bem como sua respectiva posição no 
vetor.
"""

nomes = []
maiorNome = ""

for i in range(10):
    while True:
        nome = input(f"Digite o {i + 1}º nome: ").strip().title()

        if nome.replace(" ", "").isalpha():
            nomes.append(nome)
            
            if len(nome) > len(maiorNome):
                maiorNome = nome
            break
        else:
            print("Digite apenas letras.")
        
print(f"\n-- MAIOR NOME -- \n{maiorNome}")
print("-" * 16)
print(f"Posição no vetor: {nomes.index(maiorNome) + 1}")