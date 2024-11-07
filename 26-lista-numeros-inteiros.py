# Lista para guardar os números fornecidos pelo usuário
numeros = []

# Leitura dos 5 números fornecidos pelo usuário
for i in range(5):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

# Imprimindo o maior, o menor e a soma dos números
maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)

# Mostrando os resultados
print("Maior número:", maior)
print("Menor número:", menor)
print("Soma de todos os números:", soma)