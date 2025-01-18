#1 - A loja Davi Model's necessita de um sistema que leia a quantidade de dias e leia o total vendido nesses dias,
# na sequência faça a quantidade de vendas por dia e informe o valor final.

faturamento_total = float(input('Digite o faturamento da loja: \n'))
dias = float(input('Digite a quantidade de dias que o valor esse valor foi faturado: \n'))
faturamento_dia = faturamento_total / dias

print(f"O faturaramento de Davi  Models, dividido pelos últimos 50 dias foi de R${faturamento_dia}")