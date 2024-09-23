#2 listas, una con nombres otra con apellidos
nombres = {"Enzo","matias","camila","pedro","roberto"}
apellidos = {"Guido","zing","villa","prado","tarado"}

#registrar esta informacion en un txt de forma optima

with open("archivos_problemas\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n---------\n") for n,a in zip(nombres,apellidos)]
    