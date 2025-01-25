# Desenvolva um sistema que leia de 1 a 12, onde cada número representa o mês de janiero a dezembro e retorne quantos dias tem o mês.

print('Olá, esse programa tem por objetivo auxiliar você a descobrir quantos dias tem cada mês do ano.')
print('Cada número de 1 a 12 representa um mês, na ordem cronológica do calendário.')

mes = int(input('Digite o número do mês: '))

while (mes >= 13):
    print('O número digitado não representa um mês válido. Vamos tentar novamente.')
    mes = int(input('Digite o número do mês: '))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print('31 dias')
elif mes == 2:
    print('28 ou 29 dias')
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print('30 dias')