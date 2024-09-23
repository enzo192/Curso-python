
#creando funcion que suma numeros
def sumar_dos():
    #iniciando un bucle
    while True:
        #pidiendo los numeros
        a = input("numero 1: ")
        b = input("numero 2: ")
        #convirtiendo a enteros y sumarlos
        try:
            resultado = int(a) + int(b)
            #si lanza una excepcion pedirle que reingrese los datos
            break
        except ValueError as e:
            print("por favor ingresa un numero")
            print(f"ERROR: {e}")
            #si todo salio bien terminamos el bucle
        else:
            break
        #el finally se ejecuta siempre
        finally:
            print("Esto se ejecuta siempre")
    
    #mostrando el resultado        
    return resultado

print(sumar_dos())