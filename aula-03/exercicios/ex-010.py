# 10 - Desenvolva um programa em Python que leia o dia da semana e informe se é dia útil ou não.

segunda = "segunda"
terca = "terça"
quarta = "quarta"
quinta = "quinta"
sexta = "segunda"
sabado = "sabado"
domingo = "domingo"

dia_desejado = input('Digite o dia da semana:\n')

dia_desejado = dia_desejado.lower()

if dia_desejado == "sabado" or dia_desejado == "domingo":
    print('Final de semana')
elif dia_desejado == "segunda" or dia_desejado == "terca" or dia_desejado == "quarta" or dia_desejado == "quinta" or  dia_desejado == "sexta":
    print('Dia útil')
else:
    print('Dia inválido')