def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return(n % 10) + suma_digitos(n // 10)
numero = int(input("Ingrese un número entero positivo: "))
print(f"La suma de los digitos de {numero} es {suma_digitos(numero)}")