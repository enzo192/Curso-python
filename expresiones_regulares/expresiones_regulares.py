import re

texto = '''Hola maestro, esta es la cadena 1, como estas mi capitan?
Esta es la linea 2 de texto
y esta es la final (linea 3).'''

#haciendo una busqueda simple
#resultado = re.findall("esta",texto)

#\d -> busca digitos numericos del 0 - 9
# resultado = re.findall(r"\d",texto) #['1', '2', '3']

#\d -> busca TODO MENOS digitos numericos del 0 - 9
# resultado = re.findall(r"\D",texto)

#\w -> busca caracteres alfanumericos [a-z A-Z 0-9 _]
# resultado = re.findall(r"\w",texto)

#\W -> busca TODO MENOS caracteres alfanumericos [a-z A-Z 0-9 _]
# resultado = re.findall(r"\W",texto)

#\s -> busca espacios en blanco -> espacios, tabs, saltos de linea
# resultado = re.findall(r"\s",texto)

#\S -> busca TODO MENOS espacios en blanco -> espacios, tabs, saltos de linea
# resultado = re.findall(r"\S",texto)

#. -> busca TODO menos saltos en linea
# resultado = re.findall(r".",texto)

#\n -> busca saltos en linea
# resultado = re.findall(r"\n",texto)

#\ -> cancelar caracteres especiales
resultado = re.findall(r"\.",texto)

print(resultado)