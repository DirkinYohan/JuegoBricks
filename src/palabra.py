def contar_palabras_y_letras(texto):
    palabras = texto.split()
    cantidad_palabras = len(palabras)
    cantidad_letras = sum(len(palabra) for palabra in palabras)
    return cantidad_palabras, cantidad_letras

# Ejemplo de uso
texto = "Hola, este es un ejemplo de conteo."
palabras, letras = contar_palabras_y_letras(texto)
print(f"El texto tiene {palabras} palabras y {letras} letras.")