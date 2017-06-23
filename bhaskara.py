import math
a = float(input("digite o valor de a: "))
b = float(input("digite o valor de b: "))
c = float(input("digite o valor de c: "))

delta = (b ** 2) - (4 * a * c) 

if delta == 0:
    raizX = (-b + math.sqrt(delta)) / (2 * a)
    print("a raiz desta equação é", raizX)
else:
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        raizX = (-b + math.sqrt(delta)) / (2 * a)
        raizY = (-b - math.sqrt(delta)) / (2 * a)
        if raizX < raizY:
            print("as raízes da equação são", raizX, "e", raizY)
        else:
            print("as raízes da equação são", raizY, "e", raizX)