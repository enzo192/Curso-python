
# #creando una funcion simple
# def saludar():
#     print("Hola")
    

# #llamando la funcion
# saludar()

#creando funciona con parametros
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if sexo == "mujer":
        return (f"Hola maestra {nombre}, como estas?")
    else:
        return (f"Hola maestro {nombre}, como estas?")
        
saludo = saludar("Enzo","Hombre")
print(saludo)