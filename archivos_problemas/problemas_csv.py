#cambiar tipo de dato de una columna
import pandas as pd
df = pd.read_csv("archivos_problemas\\datos.csv")

#convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

#mostrar el tipo de dato del primer elemento de la columna edad
#print(type(df['edad'][0]))

#remplazando los datos "guido" por "abuchaaibe"
df['apellido'].replace("guido","abuchaibe",inplace=True)

#mostrando columna apellido
#print(df['apellido'])

#eliminado filas con datos faltantes
df = df.dropna()
#print(df)

#eliminando filas repetidas
df = df.drop_duplicates()
print(df)


#creado un CSV con el dataframe resultante (limpio)
df.to_csv("archivos_problemas\\datos_limpios.csv")