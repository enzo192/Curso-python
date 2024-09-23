
#Creando mi propia excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"El error es: {err}")


#lanzando mi propia excepcion
# raise MiExcepcion("jajajaja, persona poco culta")

#manejandola
try:
    raise MiExcepcion("jajajaja")
except:
    print("Como vas a cometer ese error?")