"""  
Solicite  um  vetor  contendo  5  nomes  e  armazene  em  um  segundo  vetor  a 
quantidade de caracteres de cada elemento do primeiro vetor.
"""

nomes = []
quantidadeCaracteres = []

for i in range(5):
    while True:
        nome = input(f"Digite o nome da {i + 1}º pessoa: ").strip().title()

        if not nome.isalpha():
            # if not nome.replace(" ", "").isalpha():
            # Dessa forma o algoritmo aceita nomes compostos
            print("Valor inválido.")
        else:
            nomes.append(nome)
            quantidadeCaracteres.append(len(nome))
            break

print("\n")
for nome, letras in zip(nomes, quantidadeCaracteres):
    print(f"NOME: {nome}, QUANTIDADE DE CARACTERES: {letras}")
    # TOMAR CUIDADO COM OS NOMES DAS VARIÁVEIS (ANTES FOI UTILIZANDO "nomes" PARA A VARIÁVEL DE 
    # DENTRO E DE FORA DO ZIP)
    