def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])
    
texto = input("Ingrese una palabra: ").lower()
print(f"Es {texto} un palindromo? {es_palindromo(texto)}")