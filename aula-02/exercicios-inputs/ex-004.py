# 4 - Desenvolva um programa em Python que calcule um aumento de 15% para um salário de informado pelo usuário.

salario_base = float(input("Informe o salário do colaborador: \n"))
aumento = 15 / 100 * salario_base
salario_novo = salario_base + aumento

print(f'O novo salário do colaborador é de R${salario_novo:.2f}')