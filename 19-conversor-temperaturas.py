# Início 

print("Conversão de escalas")

def fahrenheit_para_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def kelvin_para_celsius(k):
    return k - 273.15

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_para_kelvin(c):
    return c + 273.15

def menu():
    print("\nMenu de escolhas:")
    print("1. Converter Fahrenheit para Kelvin")
    print("2. Converter Fahrenheit para Celsius")
    print("3. Converter Kelvin para Fahrenheit")
    print("4. Converter Kelvin para Celsius")
    print("5. Converter Celsius para Fahrenheit")
    print("6. Converter Celsius para Kelvin")
    print("7. Sair do programa")

while True:
    menu()
    opcao = input("\nSelecione uma escolha (1-7): ")

    if opcao == "1":
        temp = float(input("Digite a temperatura em Fahrenheit: "))
        print(f"{temp} Fahrenheit é igual a {fahrenheit_para_kelvin(temp)} Kelvin")
    elif opcao == "2":
        temp = float(input("Digite a temperatura em Fahrenheit: "))
        print(f"{temp} Fahrenheit é igual a {fahrenheit_para_celsius(temp)} Celsius")
    elif opcao == "3":
        temp = float(input("Digite a temperatura em Kelvin: "))
        print(f"{temp} Kelvin é igual a {kelvin_para_fahrenheit(temp)} Fahrenheit")
    elif opcao == "4":
        temp = float(input("Digite a temperatura em Kelvin: "))
        print(f"{temp} Kelvin é igual a {kelvin_para_celsius(temp)} Celsius")
    elif opcao == "5":
        temp = float(input("Digite a temperatura em Celsius: "))
        print(f"{temp} Celsius é igual a {celsius_para_fahrenheit(temp)} Fahrenheit")
    elif opcao == "6":
        temp = float(input("Digite a temperatura em Celsius: "))
        print(f"{temp} Celsius é igual a {celsius_para_kelvin(temp)} Kelvin")
    elif opcao == "7":
        print("Saindo do programa...")
        break
    else:
        print("Escolha inválida, tente novamente.")
