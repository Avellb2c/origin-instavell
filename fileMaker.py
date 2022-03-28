import os
import getLenguage
import windowFunction
#Busqueda de carpetas existentes y en caso no existan se las crea, sea ruta de servidor o local según el idioma
leng = getLenguage.Lenguages()
path = windowFunction.Selector()
def createFiles():
    if leng == "en":
        if os.path.isdir(f"{path}/Drivers") == False:
            os.mkdir(f"{path}/Drivers")
            if os.path.isdir(f"{path}/Apps") == False:
                os.mkdir(f"{path}/Apps")
    elif leng == "es":
        if os.path.isdir(f"{path}/Controladores") == False:
            os.mkdir(f"{path}/Controladores")
            if os.path.isdir(f"{path}/Aplicaciones") == False:
                os.mkdir(f"{path}/Aplicaciones")
                
def deleteFiles():
    if leng == "en":
        if os.path.isdir(f"{path}/Drivers") == True:
            os.rmdir(f"{path}/Drivers")
            if os.path.isdir(f"{path}/Apps") == True:
                os.rmdir(f"{path}/Apps")
    elif leng == "es":
        if os.path.isdir(f"{path}/Controladores") == True:
            os.rmdir(f"{path}/Controladores")
            if os.path.isdir(f"{path}/Aplicaciones") == True:
                os.rmdir(f"{path}/Aplicaciones")