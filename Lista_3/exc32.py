"""  
Solicite uma frase e exiba apenas as vogais que aparecem uma única vez.
"""

frase = input("Digite uma frase: ").strip().lower()
vogais = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0
}

for letra in frase:
    if letra in vogais:
        vogais[letra] += 1

print("--- LETRAS ÚNICAS NA FRASE ---")
for key, value in vogais.items():
    if value == 1:
        print(f"Letra {key}")