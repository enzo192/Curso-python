with open("archivos\\texto_de_dalto.txt","w",encoding="UTF-8") as archivo:
    #sobreescribiendo el archivo
    #archivo.write("jajajajaja se mamo")
    
    #agregando 2 lineas con writelines
    archivo.writelines(["jajaajaja asi esta mejor\n","cómo\n"])
    
    #agregando otras 2 lineas con writelines
    archivo.writelines(["que rayos!? asi esta mejor\n","cómo\n"])
    