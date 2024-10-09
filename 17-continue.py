# Ferramenta continue
# A ferramenta continue no python vai começar a interromper o loop
# Mas vai dar continuidade a ele

contador = 0

while contador <= 40:
    contador += 1

    # Verifica se o valor de 'contador' é multiplo de 4
    if (contador % 4 == 0):
        print("pim") # Se for multiplode 4, imprime "pim"
        continue # Interrompe a iteração atual e volta para o início do loop

    # Se o número não for multiplo de 4, imprime o valor do contador
    print(contador)

 # Após o término do loop, imprime a mensagem de finalização
print("fim  do programa")