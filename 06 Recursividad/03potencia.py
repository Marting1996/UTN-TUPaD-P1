def potencia(base, exp):
    if exp == 0:
        return 1
    else:
        return base * potencia(base, exp - 1)

base = int(input("Ingrese la base: "))
exp = int(input("Ingrese el exponente: "))
print(f"{base}^{exp} = {potencia(base, exp)}")