""" 
Solicite um número no formato string e verifique se contém apenas dígitos numéricos.
"""

# MINHA RESPOSTA
"""
string = input("Digite um número: ")
nums = "1234567890"
count = 0

for i in string:
    if i not in nums:
        count += 1

if count > 0:
    print("Resposta inválida.")
else:
    print("Tudo certo.")
"""

# RESPOSTA MAIS ADEQUADA

string = input("Digite um número: ")

if string.isdigit():
    print("Tudo certo.")
else:
    print("Resposta inválida.")