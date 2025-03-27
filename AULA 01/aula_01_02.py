# Escreva um programa que, leia dois valores para as variáveis A e B e efetue a troca dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresente os valores trocados.

# Entrada de Dados
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

# Processamento dos Dados|
aux = a
a = b
b = aux

# Saída de Dados
print(f"O novo valor de A é: {a}")
print(f"O novo valor de B é: {b}")
