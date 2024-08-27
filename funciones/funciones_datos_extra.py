#creando una funcion de 3 parametros

# def frase(nombre, apellido, adjetivo):
#     return f"Hola {nombre} {apellido}, eres un {adjetivo}"

#utilizando keyboards arguments
# frase_resultante = frase(nombre = "Enzo",apellido = "Guido",adjetivo = "capo")
# print(frase_resultante)

#creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre, apellido, adjetivo = "tonto"):
    return f"Hola {nombre} {apellido}, eres un {adjetivo}"

frase_resultante = frase("Enzo","Guido","inteligente")
print(frase_resultante)
