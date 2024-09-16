import pandas as pd

#usando la funsion read_csv para leer el archivo CSV
#df = pd.read_csv("archivos\\datos.csv",names=["name","lastname","age"])
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

#obteniendo los datos de la columna nombre
nombre = df["nombre"]

#ordenando el dataframe por la edad
df_orden_ascendente = df.sort_values("edad")

#ordenando de forma descendente
df_orden_descendente = df.sort_values("edad",ascending=False)

#concatenando los dos dataframes
df_concatenado = pd.concat([df,df2])

#accediendo a la primeras 3 filas con head()
primer_fila = df.head(3)

#accediendo a la ultimas 3 filas con tail()
ultimas_filas = df.tail(3)

#sccediendp a la cantidad de filas y columnas con shape
filas_y_columnas_totales = df.shape #(3,3)
filas_totales,columnas_totales = df.shape

#obteniendo data estadistica del dataframe
df_info = df.describe()

#accediendo a un elemento especifico del dt con loc
elemento_especifico_loc = df.loc[2,"edad"]

#accediendo a un elemento especifico del dt con iloc
elemento_especifico_loc = df.iloc[2,2]

#accediendo a todas las filas de una columna
apellidos = df.loc[:,"apellido"]

#accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]

#accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]

#accediendo a la fila 3 con iloc
fila_3 = df.iloc[2,:]

#accediendo a filas con edad mayor que 30
mayor_que_30 = df.loc[df["edad"]>30,:]


print(mayor_que_30)