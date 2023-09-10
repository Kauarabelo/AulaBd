import math

angulo = float(input("Fale um ângulo: "))
radiano = math.radians(angulo)
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)
secante = 1/cosseno
cossecante = 1/seno
cotangente = 1/tangente

print("\nseno: ", seno,"\ncosseno: ", cosseno,"\ntangente: ", tangente,"\nsecante: ", secante,"\ncossecante: ", cossecante,"\ncotangente: ", cotangente)