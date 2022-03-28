import tkinter, tkinter.filedialog
import os
#seleccionador de carpeta para ejecución de codigo guaradado en una variable tempdir
def Selector():
    root = tkinter.Tk()
    root.withdraw() #use to hide tkinter window

    #Selección de carpeta raíz donde buscará el programa las carpetas
    currdir = os.getcwd()
    tempdir = tkinter.filedialog.askdirectory(parent=root, initialdir=currdir, 
    title='Please select a directory') #selector de ruta guardada en una variable
    return tempdir