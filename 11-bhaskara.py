#Valores do coeficientes
a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))
 
 #Calculando
delta = (b **2) - (4*a*c)
if a == 0:
    print("O valor de a, não pode ser igual a 0")
elif delta < 0:
    print("Não possui raízes reais")
else:
    x1 = (-b  + delta ** 0.5) / (2 * a)
    x2 = (-b  - delta  **  0.5) / (2 * a)

    print("x1: {},  x2: {}".format(x1, x2))