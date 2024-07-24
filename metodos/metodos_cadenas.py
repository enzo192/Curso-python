cadena1 = "Hola,soy,enzo"
cadena2 = "Bienvenido"

#DIR devuelve la lista de atributos validos del objeto pasado

resultado = dir(cadena1)

#print(resultado)

#structura para usar un metodo: datos.metodo()

mayusc = cadena1.upper() #HOLA SOY ENZO
minusc = cadena1.lower() #hola soy enzo
primera_letra_mayus = cadena1.capitalize() #Hola soy enzo

#encuentra la primera aparicion del valor especificado, sino encuentra devuelve -1
busqueda_find = cadena1.find("s") #5
#encuentra la primera aparicion del valor especificado, si no encuentra lanza una excepcion
busqueda_index = cadena1.index("s") #5

#si es numero devuelve True, sino False
es_numerico = cadena1.isnumeric() #False
#si es alfanumero devuelve True, sino False / los espacios son caracteres especiales / solo revisa de la A a la Z
es_alfanumerico = cadena1.isalpha() #False

#busca una cadena en otra cadena y devuelve la cantidad de veces que coincida
contar_coincidencias = cadena1.count("o") #3
#contamos el numero de caracteres en una cadena
contar_caracteres = len(cadena1) #13

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith("H") #True
#verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("o") #True

#remplaza un pedazo de la cadena dada, por otra dada / si el valor 1 lo encuentra en la cadena, lo remplaza con el valor 2
cadena_nueva = cadena1.replace("la","lu") #Holu soy enzo

#separar cadenas con la cadena que le pasemos, lo devuelve en una lista
cadena_separada = cadena1.split(",") #['Hola', 'soy', 'enzo']

print(cadena_separada)
