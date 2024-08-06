#pedimos una frese
frase = input("dime una frase y te calculo cuanto tardas si tuvieras que decirla: ")
#separamos las palabras por espacios
palabras_separadas = frase.split(" ")
#contamos el numero de palabras
cantidad_de_palabras = len(palabras_separadas)

#imprimimos cuanto tardariamos en decirlas
print(f"Dijiste {cantidad_de_palabras} palabras y tardarias {cantidad_de_palabras/2} segundos en decirlas")
#imprimimos cuanto tardaria Dalto en decirlo
print(f"Dalto tardaria {cantidad_de_palabras/2 - cantidad_de_palabras/2*0.30} segundos")
#imprimimos que es mucho lo que escribio
if cantidad_de_palabras/2 > 120:
    print("Para hermano tampoco te pedi un testamento")