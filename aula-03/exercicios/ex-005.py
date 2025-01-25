# 5 - Desenvolva um programa em Python que leia o texto e informe se a palavra é o texto "Abobora".

texto = input("Digite um texto: \n")
abobora = "abobora"

texto = texto.lower()

if texto == abobora:
    print('O texto digitado é abobora')
else: 
    print('O texto digitado NÃO é abobora')