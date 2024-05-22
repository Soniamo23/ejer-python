def contar_palabras(cadena):
   
    palabras = cadena.split()
   
    return len(palabras)

cadena_usuario = input("Introduce una cadena de texto:  ")
numero_de_palabras = contar_palabras(cadena_usuario)
print(f"El número de palabras en la cadena es: {numero_de_palabras}")
