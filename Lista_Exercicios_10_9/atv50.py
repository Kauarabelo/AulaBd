import math

perimetro = 5
area = 10
diagonal = 7

Base = int(input("Fale a base do retângulo: "))
altura = int(input("Fale a altura do retângulo: "))

perimetro = (2 * Base) + (2 * altura)
area = Base * altura
diagonal = math.sqrt(Base*Base + altura * altura)

print("perimetro: ",perimetro,"\narea: ", area,"\ndiagonal: ", diagonal)