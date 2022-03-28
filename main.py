import subprocess, os, locale, shutil
import tkinter, tkinter.filedialog
import fileMaker

#Busqueda de carpetas existentes y en caso no existan se las crea, sea ruta de servidor o local según el idioma
fileMaker.createFiles()

#Listado de programas en ruta especificada
listPrograms = []
listPrograms.append(os.listdir(os.getcwd())) #imprime una lista de una carpeta
print(listPrograms)

#Borrando carpetas
fileMaker.deleteFiles()

#seccion de programas - Drivers - a seleccionar de los encontrados en la carpeta Drivers - checkbox

#seccion de programas - Apps - a seleccionar de la lista encontradas en la carpeta - checkbox

# instalación en background de los programas
