""" 
Solicite uma string e exiba-a invertida (ex.: "CASA" → "ASAC").
"""

# MINHA RESPOSTA (DEU ERRO)
"""
string = input("Digite alguma coisa: ")
stringInvertida = ""

for i in range(len(string), -1):
    stringInvertida += i

print(f"Palavra/frase invertida: {stringInvertida}")
"""

# OUTRAS FORMAS
"""  
SLICING

Para inverter uma string usando fatiamento, basta utilizar a sintaxe [::-1], que começa do final 
da string e percorre até o início com um passo negativo de -1
"""

string = input("Digite alguma coisa: ")
stringInvertida = string[::-1]

print(stringInvertida)

# OU
"""  
texto = "Python"
invertido = ""

for caractere in texto:
    invertido = caractere + invertido

print(invertido)  # Saída: nohtyP   
"""

""" 
texto = "Python"
invertido = ""
i = len(texto)

while i > 0:
    invertido += texto[i - 1]
    i -= 1

print(invertido)  # Saída: nohtyP   
"""