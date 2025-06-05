""" # 1
precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melón': 3000, 'Uva': 1450}
#Añadir frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)
print("//////////////////////////////////////////////////")
# 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)
print("//////////////////////////////////////////////////")

# 3
frutas = list(precios_frutas.keys())
print(frutas)
print("//////////////////////////////////////////////////")

# 4
contactos = {}
#Agregar contacto
for i in range(5):
    nombre = input("Ingresa el nombre del contacto: ")
    telefono = int(input("Ingrese el telefono: "))
    contactos[nombre] = telefono

#Consultar contacto
consulta = input("Ingresa el nombre a consultar: ")
if consulta in contactos:
    print(f"El telefono de {consulta} es {contactos[consulta]}")
else:
    print("El contacto no existe")

# 5
frase = input("Ingrese una frase: ")

palabras = frase.split()
print(palabras)
palabras_unicas = set(palabras)

recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1
print("Palabras unicas", palabras_unicas)
print("Recuento de palabras:", recuento) 

# 6
alumnos = {}
for i in range(3):
    nombre = input(f"Ingresa el nombre del alumno {i+1}: ")
    notas = []

    for n in range(3):
        nota = float(input(f"ingrese la nota {n+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

print("Promedio:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio}")
print(alumnos) 

# 7
#Ejemplo de sets

aprobados1 = {1, 2, 3, 4}
aprobados2 = {3, 4, 5, 6}

aprobados_1y2 = aprobados1.intersection(aprobados2)

aprobados_solo1 = aprobados1.symmetric_difference(aprobados2)

aprobados_total = aprobados1.union(aprobados2)

print("Estudiantes que aprobaron ambos parciales", aprobados_1y2)
print("Estudiantes que aprobaron solo un parcial", aprobados_solo1)
print("Estudiantes que aprobaron al menos un parcial", aprobados_total)

# 8
inventario = {'Pera': 3, 'Banana': 2}
while True:
    print("Opciones")
    print("1 Consultar stock")
    print("2 Agregar/Actualizar stock")
    print("3 Salir")
    opcion = input("Seleccione una opcion: ")

    if opcion == '1':
        producto = input("Ingresa el nombre del producto a consultar: ")
        if producto in inventario:
            print(f"El stock de {producto} es : {inventario[producto]}")
        else:
            print("El producto no existe")
    elif opcion == '2':
        producto = input("Ingresa el nombre del producto a consultar: ")
        cantidad = int(input("Ingresa la cantidad a agregar: "))
        if producto in inventario:
            inventario[producto] += cantidad
            print(f"Stock actualizado de {producto}: {inventario[producto]}")
        else:
            inventario[producto] = cantidad
            print(f"Stock actualizado de {producto}: {inventario[producto]}")
    elif opcion == '3':
        print("Saliendo...")
        break
    else:
        print("Opcion no valida")

# 9
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}

dia = input("Ingresa el día: ").lower()
hora = input("Ingresa la hora: ")

evento = agenda.get((dia, hora), "No hay actividad programada")
print(f"Actividad: {evento}")"""

# 10
paises_capitales = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Brasil": "Brasilia"}

dict_invertido = {capital: pais for pais, capital in paises_capitales.items()}

print("Diccionario invertido (capitales : países):", dict_invertido)