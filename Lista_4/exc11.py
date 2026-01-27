"""  
Solicite  os  dados  de  10  pessoas  e  armazene-as  em  vetores:  Nome,  idade  e 
sexo.  Posteriormente,  apresente  o  nome  da  pessoa  mais  jovem  e  a  média  de 
idade dos homens.
"""

nomes = []
idades = []
sexos = []
idadesHomens = []

nomeMaisNovo = ""
idadeMaisNovo = 999

for i in range(10):
    nomes.append(input(f"Digite o nome da {i + 1}º pessoa: ").strip().title())
    idades.append(int(input(f"Digite a idade de {nomes[i]}: ")))

    if idades[i] < idadeMaisNovo:
        nomeMaisNovo = nomes[i]
        idadeMaisNovo = idades[i]

    while True:
        sexo = input(f"Qual o sexo de {nomes[i]} (M/F): ").strip().lower()

        if sexo == "m" or sexo == "f":
            sexos.append(sexo)

            if sexo == "m":
                idadesHomens.append(idades[i])
            break
        else:
            print("Valor inválido.")

mediaIdadeHomens = sum(idadesHomens) / len(idadesHomens)
# LEMBRAR QUE SE NÃO TIVER NENHUM HOMEM O VALOR DA MÉDIA DEVE SER ZERO

print(f"\nNome da pessoa mais jovem: {nomeMaisNovo}")
print(f"Média das idades dos homens: {mediaIdadeHomens:.2f}")

"""  
# VERSÃO LEVEMENTE REFINADA

nomes = []
idades = []
sexos = []
idades_homens = []

nome_mais_novo = ""
idade_mais_novo = float("inf")

for i in range(10):
    nome = input(f"Digite o nome da {i + 1}ª pessoa: ").strip().title()
    idade = int(input(f"Digite a idade de {nome}: "))

    nomes.append(nome)
    idades.append(idade)

    if idade < idade_mais_novo:
        nome_mais_novo = nome
        idade_mais_novo = idade

    while True:
        sexo = input(f"Sexo de {nome} (M/F): ").strip().lower()

        if sexo in ("m", "f"):
            sexos.append(sexo)

            if sexo == "m":
                idades_homens.append(idade)
            break
        else:
            print("Valor inválido.")

if idades_homens:
    media_homens = sum(idades_homens) / len(idades_homens)
else:
    media_homens = 0

print(f"\nNome da pessoa mais jovem: {nome_mais_novo}")
print(f"Média das idades dos homens: {media_homens:.2f}")
"""