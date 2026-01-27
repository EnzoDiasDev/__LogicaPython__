"""  
Construa  um  algoritmo  que  armazene  os  seguintes  dados  de  40  pessoas: 
Nome  do  aluno,  nota1,  nota2,  nota  sub,  média  e  situação  (“Aprovado”  ou 
“Reprovado”)  com  base  a  média  mínima  6,0 para aprovação. No final, 
apresente todas as informações.
"""

alunos = []

for i in range(2):
    print(f"\nAluno {i + 1}")

    nome = input("Nome: ").strip().title()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota_sub = float(input("Nota Sub: "))

    media = (nota1 + nota2 + nota_sub) / 3

    situacao = "Aprovado" if media >= 6 else "Reprovado"

    aluno = {
        "Nome": nome,
        "Nota1": nota1,
        "Nota2": nota2,
        "Sub": nota_sub,
        "Media": round(media, 2),
        "Situacao": situacao
    }

    alunos.append(aluno)

# Exibição final
print("\n--- RESULTADO FINAL ---")

for aluno in alunos:
    print(
        f'{aluno["Nome"]} | '
        f'N1: {aluno["Nota1"]} | '
        f'N2: {aluno["Nota2"]} | '
        f'Sub: {aluno["Sub"]} | '
        f'Média: {aluno["Media"]} | '
        f'{aluno["Situacao"]}'
    )