while True:
    nome = input('Digite seu nome ou escreva "sair": ')

    if nome == 'sair':
        break # para a execução do while, sai do loop de repetição

    print(f'Seu nome é  {nome}')

print('Acabou!')