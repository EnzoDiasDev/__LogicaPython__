"""  
Solicite uma string e informe se ela contém a letra 'Z'.
"""

palavra = input("Digite alguma coisa: ").strip().lower()

if "z" in palavra:
    print("A palavra contém a letra Z")
else:
    print("A palavra não tem a letra Z")

"""  
VERSÃO MELHORADA

palavra = input("Digite algo: ").strip().lower()
print("Contém 'Z'" if "z" in palavra else "Não contém 'Z'")
"""