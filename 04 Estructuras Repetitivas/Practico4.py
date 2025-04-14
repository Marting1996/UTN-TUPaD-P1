# Hola profe, las actividades estan comentadas para poder realizar un mejor testeo

# Actividad 1
""" for numeros in range(101):
    print("Número:", numeros) """

# Actividad 2
""" num = int(input("Ingrese un número entero "))
contador = 0
for digito in str(num):
    contador +=1
print(f"El número ingresado tiene {contador} dígitos") """

# Actividad 3
""" num1 = int(input("Ingrese un número entero "))
num2 = int(input("Ingrese otro número entero "))
sumatoria = 0

for rango in range(num1+1, num2):
    print(rango)
    sumatoria += rango
print(f"La sumatoria del rango entre los números que colocaste es de: ", sumatoria) """

# Actividad 4
""" num3 = None
sumar = 0
while num3 != 0:
    num3 = int(input("Ingresa un número entero para realizar la sumatoria, si desea finalizar el programa ingrese un 0 "))
    sumar += num3
    print(f"La sumatoria de los números ingresados hasta ahora es de: {sumar} ", )
print("Operación finalizada") """

# Actividad 5
""" import random
numero_aleatorio = random.randint(0, 9) 
print(numero_aleatorio)
contador1 = 0
numero_usuario = input("Ingresa un número entero del 0 al 9 a ver si aciertas ")

while numero_usuario != int(numero_aleatorio):
    numero_usuario = int(input("Intenta de nuevo! "))
print(f"Acertaste! el número correcto era el: {numero_aleatorio}") """

# Actividad 6
""" for pares in range(100, 0, -2):
    print (pares) """

# Actividad 7 
""" num4 = (int(input("Ingresa un número entero positivo ")) + 1)
sumatoria1 = 0
for rango1 in range(0, num4):
    sumatoria1 += rango1
print(f"La sumatoria desde el 0 hasta el {num4 - 1} es de {sumatoria1}") """

# Actividad 8
""" print("Debes ingresar un total de 100 números")
contador2 = 0
pares1 = 0
impares1 = 0
while contador2 < 100:
    num5 = int(input("Ingresa un numero "))
    if num5 % 2 == 0:
        pares1 += 1
    else:
        impares1 += 1
    contador2 +=1
print(f"En total hay {pares1} pares y {impares1} impares")
 """

# Actividad 9
""" num6 = 0
contador3 = 0
media = 0
while contador3 < 100:
    num6 = int(input("Ingresa un número "))
    media += num6
    contador3 += 1
print(f"La media de todos los números ingresados es de: {media / contador3}") """

# Actividad 10
""" num7 = int(input("Ingresa un número aleatorio de 2 o mas digitos "))
numero_invertido = 0
ultimo_digito = 0
while num7 != 0:
    ultimo_digito = num7 % 10
    numero_invertido = numero_invertido * 10 + ultimo_digito
    num7 = num7 // 10
print(f"El número invertido es: {numero_invertido}") """
