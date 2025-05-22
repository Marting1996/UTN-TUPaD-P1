def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
    
fila_de_abajo = int(input("Ingrese el número de bloques en el nivel mas bajo: "))
print(f"El número de bloques total utilizado es de {contar_bloques(fila_de_abajo)}")
