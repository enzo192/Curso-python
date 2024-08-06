
animales = ["gato","perro","loro","cocodrilo"]
numeros = [52,16,23,36]




#recorriendo la lista animales
for animal in animales:
    print(f"Ahora la variable es ogial a: {animal}")
    

#recorriendo la lista numeros y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)
    
    
#iterando dos listas al tiempo del mismo tamaño
for numero,animal in zip(animales,numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")
    
    
for num in range(5,10):
    print(num)
    
#forma no optima de recorrer una lista
for num in range(len(numeros)):
    print(numeros[num])
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    print(num)