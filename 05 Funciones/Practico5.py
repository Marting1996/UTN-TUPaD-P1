# Actividad 1
def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()

# Actividad 2
def saludar_usuario():
    nombre = input("Por favor ingrese su nombre: ")
    print(f"Hola {nombre}")
saludar_usuario()

# Actividad 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ") 
informacion_personal(nombre, apellido, edad, residencia)

# Actividad 4
import math
radio = float(input("Ingrese el radio del circulo: "))
def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    print(f"El area es: {area}")

def calcular_perimetro_circulo(radio):
    perimetro = (2 * math.pi) * radio
    print(f"El perimetro es: {perimetro}")
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

# Actividad 5
def segundos_a_horas(segundos):
    horas = (segundos / 60) /60
    print(f"{segundos} equivale a {horas} horas")
segundos = int(input("Por favor ingrese la cantidad de segundos "))
segundos_a_horas(segundos)

# Actividad 6
def tabla_de_multiplicar(numero):
    for i in range(0, 11):
        print(f"{numero} x {i} = {numero * i}")
numero = int(input("Ingrese un número entero "))
tabla_de_multiplicar(numero)

# Actividad 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b == 0:
        division = "No se puede dividir por 0"
    else:
        division = a / b
    print(f"""{a} + {b} = {suma}
    {a} - {b} = {resta}
    {a} x {b} = {multiplicacion}
    {a} / {b} = {division}""")
a = float(input("Ingresa el primer número "))
b = float(input("Ingresa el segundo número "))
operaciones_basicas(a, b)

# Actividad 8
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"Tu indice de masa corporal es de {imc}")
peso = int(input("Por favor ingresa tu peso en kg "))
altura = float(input("Por favor ingresa tu altura en metros "))
calcular_imc(peso, altura)

# Actividad 9
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    print(f"{celsius}°C es igual a {fahrenheit}°F")
celsius = float(input("Por favor ingresa los grados Celsius "))
celsius_a_fahrenheit(celsius)

# Actividad 10
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio de los 3 números ingresados es de: {promedio}")
num1 = int(input("Ingresa el primer número "))
num2 = int(input("Ingresa el segundo número "))
num3 = int(input("Ingresa el tercer número "))
calcular_promedio(num1, num2, num3)