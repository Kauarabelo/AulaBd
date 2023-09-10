import math
perimetro = 2
area = 10
diagonal = 5

lado = int(input("digite o lado do quadrado"))

perimetro = 4 * lado
area = lado * lado
diagonal = math.sqrt(lado)

print("perimetro: ",perimetro,"\narea: ", area,"\ndiagonal: ", diagonal)