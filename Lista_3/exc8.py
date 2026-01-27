""" 
Solicite uma string (mínimo 4 caracteres) e exiba, para cada caractere, seu valor ASCII.
"""

while True:
    string = input("Digite uma palavra com no mínimo 4 caracteres: ")

    if len(string) >= 4:
        break
    else:
        print("Tente novamente.\n")

print(" LETRA | ASCII")
print("---------------")

for i in string:
    print(f"   {i}   :  {ord(i)}")