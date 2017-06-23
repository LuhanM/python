import math
a = float(input("digite o valor de a: "))
b = float(input("digite o valor de b: "))
c = float(input("digite o valor de c: "))

delta = b ** 2 - 4 * a * c

if delta == 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    print("a unica raiz é:", raiz1)
else:
    if delta < 0:
        print("Esta equação não possui raizes reais")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print("raiz 1:",raiz1)
        print("raiz 2:",raiz2)
