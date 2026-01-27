"""  
Solicite uma frase e substitua todas as letras 'a' por @.
"""

string = input("Digite alguma coisa: ").strip()
print(f"NOVA PALAVRA: {string.replace('a', '@')}")

"""
Só existiu um erro:

ANTES:
print(f"NOVA PALAVRA: {string.replace("a", "@")}")

A f-string foi aberta com ", e foi usado " dentro dela, o que geraria um possível conflito.
"""