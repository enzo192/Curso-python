#creando diccionario con dict()
diccionario = dict(nombre="Enzo",apellido="guido")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["Enzo","Guido"]):"jajaja"}

#creando diccionarios con fromkeys() con valores indefinidos None
diccionario = dict.fromkeys(["nombre","apellido"])

#creando diccionarios con fromkeys() cambiando valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre","apellido"],"No se")


print(diccionario)