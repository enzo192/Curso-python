
#creando una lista con list()
lista = list(["Hola","Enzo","32"])
lista2 = list(["Hola","Enzo","32"])

#devuelve la canidad de elementos de la lista
cantidad_elementos = len(lista) #3

#agregando un elemento a la lista
lista.append("jajajaja") #['Hola', 'Enzo', '32', 'jajajaja']

#agregando un elemento a la lista en un indice especifico
lista.insert(2,"que") #['Hola', 'Enzo', 'que', '32', 'jajajaja']

#agregando varios elementos a la lista
lista.extend([False,2023]) #['Hola', 'Enzo', 'que', '32', 'jajajaja', False, 2023]

#eliminando un elemento de la lista por su indice
lista.pop(0) #['Enzo', 'que', '32', 'jajajaja', False, 2023]   /  -1 para eliminar el ultimo

#remueve un elemento de la lista por su valor
lista.remove("Enzo") #['que', '32', 'jajajaja', False, 2023]

#elimina todos los elemento de la lista
#lista.clear()

#ordenando la lista de forma ascendente (si usamos el parametro reverse=True lo ordena en reversa)
lista2.sort()#['32', 'Enzo', 'Hola']

#invirtiendo los elementos de una lista
lista2.reverse()#['Hola', 'Enzo', '32']

#verificando si un elemento se encuentra en la lista y responde con la posicion en la lista 
elemento_encontrado = lista2.index("32")#2

print(elemento_encontrado)

