import re

def es_palindromo(texto):
    texto_limpio = re.sub(r'[^a-zA-Z0-9]', '', texto.lower())
    return texto_limpio == texto_limpio[::-1]

if __name__ == "__main__":
    cadena = "Anita lava la tina"
    if es_palindromo(cadena):
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")