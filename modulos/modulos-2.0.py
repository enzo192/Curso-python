

#si el modulo esta dentro de una carpeta en la misma tura se importa asi
# import funciones_buenas.saludar as m_saludar


# print(m_saludar.saludar("Enzo"))

import sys

sys.path.append("d:\\developer\\Curso de python DALTO\\funciones_buenas")

import saludar as modulo_saludo

# print(sys.path)

print(modulo_saludo.saludar("Enzo"))