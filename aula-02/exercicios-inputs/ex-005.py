# 5 - Dado que a fórmula para conversão de Fahrenheit para Celsius é C = 5/9 * (F – 32),  
# faça a leitura do valor em  graus Fahrenheit e na sequência, faça a conversão para exibi-lo em Celsius.

f = float(input('Digite o grau em F°: \n'))
c = 5/9 * (f - 32)

print(f"{f}f° é exatamente {c:.0f}c° ")
