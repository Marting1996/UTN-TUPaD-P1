def contar_digito(num, dig):
    if num == 0:
        return 0
    else:
        return (1 if num % 10 == dig else 0) + contar_digito(num // 10, dig)
    
num = int(input("Ingrese un número entero positivo: "))
dig = int(input("Ingrese el digito a contar: "))
print(f"El dígito {dig} aparece {contar_digito(num, dig)} veces")