# 4 - Desenvolva um programa em Python que leia o texto e informe se a palavra é um palíndromo.

texto = input("Digite um texto: \n")
texto = texto.lower() # Deixa o texto em letra minusculas - upper() -> maiusculas
inverso = texto [::-1] #inverte o texto

print(texto)
print(inverso)

if texto == inverso:
    print('O texto digitado é um palíndromo')
else: 
    print("O texto digitado não é um palíndromo.")