""" 
Apresente o valor ASCII de todas as letras (maiúsculas e minúsculas) e todos os números.
"""

print("--- TABELA ASCII ---\n")

tabela = {
    "LetrasMaiusculas" : {},
    "LetrasMinusculas" : {},
    "Numeros" : {}
}

for i in range(65, 91):
    tabela["LetrasMaiusculas"][chr(i)] = i

for i in range(97, 123):
    tabela["LetrasMinusculas"][chr(i)] = i

for i in range(48, 58):
    tabela["Numeros"][chr(i)] = i

print("LETRAS MAIUSCULAS:")
for key, value in tabela["LetrasMaiusculas"].items():
    print(f"{key:^10} : {value:^10}")

print("\nLETRAS MINUSCULAS:")
for key, value in tabela["LetrasMinusculas"].items():
    print(f"{key:^10} : {value:^10}")

print("\nNUMEROS:")
for key, value in tabela["Numeros"].items():
    print(f"{key:^10} : {value:^10}")