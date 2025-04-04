## Actividad 6
from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
print("La moda es: ", moda)

mediana = median(numeros_aleatorios)
print("La mediana es: ", mediana)

media = mean(numeros_aleatorios)
print("La media es: ", media)

if moda < mediana < media:
    print("El sesgo es positivo")
elif moda > mediana > media:
    print("El sesgo es negativo")
else:
    print("Sin sesgo")
    