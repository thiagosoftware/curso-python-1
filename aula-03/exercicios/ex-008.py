# 8 - Desenvolva um programa em Python que determine se uma pessoa é considerada idosa, maior de idade ou menor de idade com base na idade inserida.

idade = int(input("Digite a idade da pessoa:\n"))

if idade < 0:
    print('Idade inválida')
elif idade <= 11:
    print('Criança')
elif idade <= 17:
    print('Adolescente')
elif idade >= 18 and idade < 60:
    print('Maior de idade')
elif idade >= 60:
    print('Idoso')
else:
    print('Idade inválida')