"""  
Solicite um texto e remova todos os caracteres numéricos.
"""

texto = input("Digite alguma coisa: ").strip()
numeros = "1234567890"
novoTexto = ""

for caractere in texto:
    if caractere not in numeros:
        novoTexto += caractere

print(novoTexto)

"""  
# VERSÃO MELHORADA

texto = input("Digite algo: ").strip()
novo_texto = ""

for caractere in texto:
    if not caractere.isdigit():
        novo_texto += caractere

print(novo_texto)
"""