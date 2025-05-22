def decimal_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_binario(n // 2) + str(n % 2)
numero = int(input("Ingrese el número decimal: "))
binario = decimal_binario(numero)
print(f"El número {numero} en binario es: {binario if binario else '0'}")
