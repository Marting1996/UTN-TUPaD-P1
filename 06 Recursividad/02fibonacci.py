def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

posicion = int(input("Ingrese una posición: "))
print(f"Serie de Fibonacci hasta {posicion}:")
for i in range(posicion + 1):
    print(fibonacci(i), end=" ")