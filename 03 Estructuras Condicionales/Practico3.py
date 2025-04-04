## Actividad 1
edad = int (input("Ingresa tu edad: "))
if edad > 18 :
    print("Eres mayor de edad!")

## Actividad 2
nota = int (input("Ingresa la nota: "))
if nota >= 6 :
    print("Aprobaste!")
else:
    print("Desaprobaste") 
    
## Actividad 3
num1 = int(input("Ingresa un número par: "))
if num1 % 2 == 0 :
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par") 

## Actividad 4
edad2 = int (input("Ingrese su edad: "))
if edad2 < 12:
    print ("Eres un niño!")
elif  12 <= edad2 < 18:
    print("Eres un adolescente!")
elif 18 >= edad2 < 30:
    print("Eres un adulto joven")
else:
    print("Eres un adulto!") 

## Actividad 5
password = input("Ingrese una contraseña con un minimo de 8 caracteres y un maximo de 14: ")
caracteres = len(password)
if  8 <= caracteres <= 14 :
    print("Contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres") 

## Actividad 6 en un archivo python aparte

## Actividad 7

frase = input("Por favor ingrese una frase ")
ultima_letra = frase[-1]

if ultima_letra == ("a" or "e" or "i" or "o" or "u"):
    print(frase + "!")
else:
    print(frase) 

## Actividad 8

nombre = input("Ingrese su nombre ")
opcion = int(input("""Ingrese la opcion que desee: 
               1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO
               2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
               3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro
                Elija su opcion: """))
    

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("No eligio una opcion correcta")

## Actividad 9 

magnitud = int(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print('"Muy leve" (imperceptible)')
elif 3 <= magnitud < 4 :
    print('"Leve" (ligeramente perceptible).')
elif 4 <= magnitud < 5 :
    print('"Moderado" (sentido por personas, perogeneralmente no causa daños).')
elif 5 <= magnitud < 6 :
    print('"Fuerte" (puede causar daños en estructurasdébiles).')
elif 6 <= magnitud < 7 :
    print('"Muy Fuerte" (puede causar daños significativos).')
else:
    print('"Extremo" (puede causar graves daños a gran escala).') 


## Actividad 10

hemisferio = input("En que hemisferio te encuentras? responde S para hemisferio sur y N para hemisferio norte ")
mes = int(input("Ingresa el mes actual de forma numerica, por ejemplo 1 para Enero 2 para Febrero "))
dia = int(input("Ingresa el día actual de forma numerica "))
fecha_logica = (mes * 100) + dia

if hemisferio == "N":
    if 1221 <= fecha_logica <= 320:
        estacion = "Invierno"
    elif 321 <= fecha_logica <= 620:
        estacion = "Primavera"
    elif 621 <= fecha_logica <= 920:
        estacion = "Verano"
    elif 921 <= fecha_logica <= 1220:
        estacion = "Otoño"
    else:
        estacion = "Fecha inválida"

elif hemisferio == "S":
    if 1221 <= fecha_logica <= 320:
        estacion = "Verano"
    elif 321 <= fecha_logica <= 620:
        estacion = "Otoño"
    elif 621 <= fecha_logica <= 920:
        estacion = "Invierno"
    elif 921 <= fecha_logica <= 1220:
        estacion = "Primavera"
    else:
        estacion = "Fecha inválida"

else:
    estacion = "Hemisferio inválido"

print("La estación en la que te encuentras es:", estacion)


