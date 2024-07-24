
lista = ["Enzo Guido", "Soy Enzo", True, 1.85] # se pueden modificar
print(lista) # ['Enzo Guido', 'Soy Enzo', True, 1.85]
print(lista[1]) # Soy Enzo

tupla = ("Enzo Guido", "Soy Enzo", True, 1.85) # no se pueden modificar despues estos datos


lista[3] = "maquina" #modificar el elemento de la lista

#tupla[3] = "maquina" TypeError: 'tuple' object does not support item assignment

#creando un conjunto (set)

conjunto = {"Enzo Guido", "Soy Enzo", True, 1.85, "Soy Enzo"} # no se puede modificar valores y al imprimir no muestra valores duplicados
print(conjunto) #{'Soy Enzo', True, 'Enzo Guido', 1.85}

#creando un diccionario (dict) estructura es key : value y separado por comas

diccionario = {
    'nombre' : "Enzo Guido",
    'esta_emocionado': True,
    'altura': 1.85,
    'edad': 32    
}

print(diccionario["altura"])