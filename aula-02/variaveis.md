# Regras e Exemplos de Variáveis em Python

## 1. Regras para nomes de variáveis em Python

- **Os nomes devem começar com uma letra ou um sublinhado (`_`)**:
  - Exemplo válido: `nome`, `idade`, `_altura`.
  - Exemplo inválido: `1nome` (não pode começar com número).

- **Os nomes podem conter letras, números e o caractere de sublinhado (`_`)**:
  - Exemplo válido: `nome_usuario`, `altura_1`, `a2b3`.
  - Exemplo inválido: `nome@usuario` (não pode conter símbolos especiais como `@`).

- **Não podem ser palavras reservadas do Python**:
  - Python tem palavras-chave que já têm um significado específico na linguagem, como `if`, `for`, `else`, `class`, `while`, etc. Esses nomes não podem ser usados como variáveis.
  - Exemplo inválido: `if = 10`, `for = 5`.

- **Python é sensível a maiúsculas e minúsculas**:
  - Ou seja, `nome` e `Nome` são considerados variáveis diferentes.
  - Exemplo válido: `nome = "João"`, `Nome = "Maria"`.
  - Exemplo inválido: Usar `nome` e `Nome` para a mesma variável, já que são tratadas como diferentes.

## 2. Atribuição de valores às variáveis

- Para **atribuir** um valor a uma variável, usamos o operador de atribuição `=`.
  
  Exemplo:
  ```python
  idade = 25  # Atribuindo o valor 25 à variável 'idade'
  nome = "Ana"  # Atribuindo a string "Ana" à variável 'nome'
  ```

## 3. Tipos de dados em Python
Python é uma linguagem de **tipagem dinâmica**, o que significa que você não precisa especificar o tipo da variável ao declará-la. O Python automaticamente determina o tipo de dado com base no valor atribuído à variável.

### Principais tipos de dados:

- **Inteiros (`int`)**: São números sem casas decimais.
  ```python
  idade = 30  # Exemplo de inteiro
  ```

- **Flutuantes (`float`)**: São números com casas decimais.
  ```python
  altura = 1.75  # Exemplo de flutuante
  ```

- **Strings (`str`)**: São sequências de caracteres, ou seja, texto.
  ```python
  nome = "Carlos"  # Exemplo de string
  ```

- **Booleanos (`bool`)**: São valores lógicos, que podem ser `True` ou `False`.
  ```python
  ativo = True  # Exemplo de booleano
  ```

- **Listas (`list`)**: São coleções ordenadas de itens.
  ```python
  notas = [7.5, 8.0, 9.0]  # Exemplo de lista
  ```

- **Dicionários (`dict`)**: São coleções de pares chave-valor.
  ```python
  pessoa = {"nome": "Lucas", "idade": 28}  # Exemplo de dicionário
  ```

## 4. Alterando o valor de variáveis

Uma vez que uma variável é criada, você pode mudar seu valor a qualquer momento, sem precisar declarar o tipo novamente.

Exemplo:
```python
x = 10      # 'x' é um inteiro
print(x)

x = "Olá"   # Agora 'x' é uma string
print(x)
```

## 5. Regras para operadores com variáveis

- **Operadores aritméticos**: Como soma (`+`), subtração (`-`), multiplicação (`*`), divisão (`/`), etc., podem ser usados com variáveis de tipos numéricos, como inteiros e flutuantes.
  
  Exemplo:
  ```python
  a = 10
  b = 5
  soma = a + b  # Soma de dois inteiros
  print(soma)
  
  c = 2.5
  soma_real = b + c  # Soma de inteiro e flutuante
  print(soma_real)
  ```

- **Concatenando strings**: Você pode usar o operador de soma (`+`) para concatenar strings.

  Exemplo:
  ```python
  nome = "João"
  saudacao = "Olá, " + nome  # Concatenando duas strings
  print(saudacao)
  ```

- **Misturando tipos**: Você pode somar variáveis de tipos diferentes, como inteiros e flutuantes. O Python vai automaticamente fazer a conversão para o tipo mais geral, que é o flutuante (quando há mistura de tipos).

  Exemplo:
  ```python
  idade = 25
  altura = 1.75
  soma = idade + altura  # Soma de inteiro com flutuante resulta em um flutuante
  print(soma)
  ```

## 6. Boas práticas

- **Escolher nomes significativos**: Em vez de usar nomes vagos como `a`, `b` ou `x`, é uma boa prática escolher nomes que descrevam o valor que a variável está armazenando, como `nome`, `idade`, `altura`, etc.
  
- **Usar o estilo "snake_case"**: O estilo recomendado para nomes de variáveis em Python é o "snake_case", onde todas as palavras são minúsculas e separadas por um sublinhado (`_`).
  - Exemplo: `nome_completo`, `idade_usuario`, `total_vendas`.

## 7. Exemplo completo com regras e boas práticas

Aqui está um exemplo de código com variáveis, comentários e boas práticas:

```python
# Variáveis
nome_completo = "Maria Silva"  # Nome da pessoa (string)
idade = 30  # Idade da pessoa (inteiro)
altura = 1.65  # Altura da pessoa (flutuante)

# Operações
idade_mais_5 = idade + 5  # Soma da idade com 5
altura_aumento = altura + 0.10  # Soma da altura com um aumento de 0.10

# Exibição
print("Nome:", nome_completo)  # Exibe o nome completo
print("Idade após 5 anos:", idade_mais_5)  # Exibe a idade após 5 anos
print("Altura com aumento:", altura_aumento)  # Exibe a altura com aumento
```

## Conclusão

- **Nomes de variáveis** devem seguir as regras de sintaxe e boas práticas para garantir que o código seja legível e funcione corretamente.
- O tipo da variável em Python é **dinâmico**, ou seja, o Python atribui o tipo de acordo com o valor atribuído, sem a necessidade de declarações explícitas.
- O uso correto dos **tipos de dados** e **operações** pode garantir que seu código funcione sem erros.
```