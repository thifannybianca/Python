# Lista para guardar os dados dos alunos
alunos = []

# Leitura dos nomes e notas de 5 alunos
for i in range(5):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    alunos.append((nome, nota))

# Exibindo o nome e a nota de cada aluno
print("\nNome e Nota de cada aluno:")
for nome, nota in alunos:
    print(f"Aluno: {nome}, Nota: {nota}")