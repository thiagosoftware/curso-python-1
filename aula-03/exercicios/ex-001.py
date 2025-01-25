# 1 - Desenvolva um programa em Python que leia a nota de um aluno e determine se ele foi aprovado ou reprovado, considerando a nota mínima de aprovação como 7.

nota = int(input('Digite a nota do aluno: \n'))

if nota >= 7:
    print(f'O aluno está aprovado.')
else:
    print(f'O aluno não atingiu a média, portanto está reprovado.')