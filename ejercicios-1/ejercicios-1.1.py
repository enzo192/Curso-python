#promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#diferencias de duracion

diferencia_con_min = 100 - (dalto_curso / otros_cursos_min * 100)
diferencia_con_max = 100 - (dalto_curso * 1000 // otros_cursos_max / 10)
diferencia_con_promedio = 100 - (dalto_curso/otros_cursos_promedio * 100)

#calculando el porcentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - (otros_cursos_promedio * 1000 // crudo_promedio / 10)
tiempo_vacio_dalto = 100 - (dalto_curso * 1000 // crudo_dalto / 10)

#mostrando las diferencias de duracion (ejercicio A)
print("--------------------")
print("El curso de Dalto dura: ")
print(f" - un {diferencia_con_min}% menos que el mas rapido")#El curso de Dalto dura un 40.0% menos que el mas rapido
print(f" - un {diferencia_con_max}% menos que el mas lento")#El curso de Dalto dura un 78.6% menos que el mas lento
print(f" - un {diferencia_con_promedio}% menos que el promedio")#El curso de Dalto dura un 62.5% menos que el promedio
print("--------------------")
#mostrando la cantidad de espacios vacios que se remueven (ejercicio B)
print(f"El curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio")
print(f"El curso Dalto elimina un {tiempo_vacio_dalto}% de tiempo vacio")
print("--------------------")
#mostrando diferencias si los cursos duraran 10 horas
print(f"ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos")
print(f"ver 10 horas de otros cursos equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de este curso")
print("--------------------")