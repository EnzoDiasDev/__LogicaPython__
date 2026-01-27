"""  
Solicite duas strings e informe se são iguais ignorando maiúsculas/minúsculas.
"""

string1 = input("Digite alguma coisa: ").strip().title()
string2 = input("Digite outra coisa: ").strip().title()

if string1 == string2:
    print("Ambas as palavras/frase são iguais!!!")
else:
    print("As duas palavras/frase são diferentes!!!")

"""
O método .title() modifica a frase, ou seja, não está só comparando, está modificando.
   
VERSÃO MELHORADA

string1 = input("Digite algo: ").strip().casefold()
string2 = input("Digite outra coisa: ").strip().casefold()

if string1 == string2:
    print("As duas palavras/frases são iguais!")
else:
    print("As duas palavras/frases são diferentes!")
"""