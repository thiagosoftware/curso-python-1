# Desenvolva um programa em Python que identifique números positivos, negativos e nulos

numero = float(input("Digite um número:\n"))

if numero > 0:
    print('Positivo')
elif numero < 0:
    print('Negativo')
else:
    print('Nulo')