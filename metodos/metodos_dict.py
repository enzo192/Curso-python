diccionario = {
    "nombre": "Enzo",
    "apellido": "Guido",
    "edad": 31
}

#nos devuelve un objeto dict_item
claves = diccionario.keys() #(['nombre', 'apellido', 'edad'])

#obteniendo un elemento con get() (sino encuentra devuelve none)
valor_de_keys = diccionario.get("nombre") #Enzo

#elimina todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("edad") #{'nombre': 'Enzo', 'apellido': 'Guido'}

#obteniendo un elemento dict_item iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)