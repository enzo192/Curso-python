#importar modulo y renombrarlo
# import modulo_saludar as m_saludar

#desde ese modulo importamos la funcion a usar
from modulo_saludar import saludar

#usamos la funcion saludar del modulo importado
# saludo = m_saludar.saludar("Enzo")

#usamos directamente la funcion sin mencional el modulo importado
saludo = saludar("enzo")

#mostramos resultado
print(saludo)

