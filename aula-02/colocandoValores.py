# Desenvolva um sistema que calcule um aumento de 15% em um salário de R$750,00

nome_colaborador = input("Digite o nome do colaborador: \n")

salario_base = float(input("Informe o salário do colaborador: \n"))
aumento = 15 / 100 * salario_base
salario_novo = salario_base + aumento

print(f'O novo salário do colaborador {nome_colaborador} é de R${salario_novo:.2f}')