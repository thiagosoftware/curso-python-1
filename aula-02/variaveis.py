# Constantes: Valores que não devem ser alterados durante a execução do programa.
# Em Python, convenciona-se usar letras maiúsculas para indicar que esses valores são imutáveis.
NOME = "Thiago"  # Nome fixo, que não deve ser alterado.
NOME_COMPLETO = "Thiago Rodrigues"  # Nome completo fixo, também imutável.

# Solicita ao usuário que digite seu nome e armazena na variável 'nome'.
nome = input("Digite seu nome: \n")  

# Exibe uma mensagem com o nome digitado pelo usuário.
print(f"Olá, {nome}!")  

# Variáveis numéricas: valores que podem ser modificados durante a execução do programa.
inteiro = 30  
real = 1.74   

# Soma: Realiza a soma de um número inteiro e um número de ponto flutuante.
soma = inteiro + real 

# Exibe o resultado da soma com 2 casas decimais.
print(f"A soma de {inteiro} e {real} é {soma:.2f}.")  # A formatação '.2f' exibe 2 casas decimais.

# Subtração: Realiza a subtração entre um número inteiro e um número de ponto flutuante.
subtracao = inteiro - real  # 

print(f"A subtração de {inteiro} e {real} é {subtracao:.2f}.")

# + soma
# - subtração
# * multiplicação
# / divisão
# % 