# Contador

contador = 0

while contador <= 100:
    contador += 1

    # Verifica se o valor de 'contador' é  6
    if (contador == 6):
        print("Não vou exibir o número") # Se for o número 6, imprime "Não vou exibir o número"
        continue # Interrompe a iteração atual e volta para o início do loop 
    
    # Verifica se o valor de 'contador' é de 10 a 27
    elif (contador >= 10 and contador <= 27):
        print("Não vou exibir o número ") # Se for o número 10, imprime "Não vou exibir o número"
        continue # Interrompe a iteração atual e volta para o início do loop  

    #Exibição interrompida
    print(contador)

    #Looping
    if contador == 40:
        break # para a execução do while, sai do loop de repetição

    
