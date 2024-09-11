# Tipos de Dados Primitivos:
# - Inteiro (int): números inteiros
# - Float (float): números reais, decimais
# - String (str): cadeia de caracteres, utilizando aspas
# - Boolean (bool): tipo lógico True ou False
# - Complex (complex): números complexos, com parte real e imaginária
# - List (list): lista de elementos, ordenados e indexados
# - Tuple (tuple): tupla de elementos, ordenados e imutáveis
# - Dictionary (dict): dicionário de elementos, não ordenados e indexados

# Atribuição de variável por captura
nome = input("Digite o seu nome: ")
print("Olá ", nome)
idade = input("Digite a sua idade: ")
print(idade)
altura = input("Digite a sua altura: ")
print(type(altura))

print(f"nome: {nome} idade: {idade} altura: {altura}")

valorA = int(input("digite o valor de A: "))
valorB = int(input("digite o valor de B: "))
resultado = valorA + valorB
print(f"a soma = {resultado}")


valorA = float(input("digite o valor de A: "))
valorB = float(input("digite o valor de B: "))
resultado = valorA + valorB
print(f"a soma = {resultado}")