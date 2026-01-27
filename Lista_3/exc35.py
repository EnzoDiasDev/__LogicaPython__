"""  
Solicite uma frase (mínimo 8 caracteres) e apresente se a mesma é ou não um palíndromo. Obs. Deve haver 
ao menos um espaço na frase.
"""

while True:
    frase = input("Digite uma frase (mínimo de 8 caracteres e 1 espaço): ")

    if len(frase) >= 8 and " " in frase:
        break
    else:
        print("Valor inválido.")
    
inversa = frase[::-1]

if frase == inversa:
    print(f"{frase} é um palíndromo.")
else:
    print(f"{frase} não é um palíndromo.")

"""  
# OUTRA OPÇÃO

while True:
    frase = input("Digite uma frase (mínimo 8 caracteres e 1 espaço): ").strip()

    if len(frase) >= 8 and " " in frase:
        break
    else:
        print("Valor inválido.")

# Remove espaços e padroniza
frase_formatada = frase.replace(" ", "").lower()
inversa = frase_formatada[::-1]

if frase_formatada == inversa:
    print(f'"{frase}" é um palíndromo.')
else:
    print(f'"{frase}" não é um palíndromo.')
"""