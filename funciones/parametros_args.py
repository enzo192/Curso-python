#forma no optima de sumar valores
# def suma(lista):
#     numeros_sumados = 0
#     for numero in lista:
#         numeros_sumados = numeros_sumados + numero
#     return numeros_sumados

#utilizando el operador * como parametro (*args), siempre tiene que ser el ultimo parametro
def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"
    
resultado = suma("Enzo",5,3,9,10,20,3)
print(resultado)