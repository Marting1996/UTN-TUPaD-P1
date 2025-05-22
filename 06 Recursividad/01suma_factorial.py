def suma_factorial(num):
    if num == 0:
        return 0
    else:
        return num + suma_factorial(num - 1)
print(f"{suma_factorial(int(input("Por favor ingresa un número para calcular su factorial ")))}") 