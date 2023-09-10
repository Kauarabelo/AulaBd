import math

xn1 = int(input("Qual o primero valor? "))
xn2 = int(input("E o segundo valor? "))
xn3 = int(input("E o terceiro valor? "))
logaritmo = math.log(64,2)

x = xn1 + xn2/(xn3 + xn1) + 2*(xn1 - xn2) + logaritmo

print("X = ",x)