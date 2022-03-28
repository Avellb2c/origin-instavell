import os
import locale
#Selección de sistema Win ENG/ES
def Lenguages ():
    systemLenguage = locale.getdefaultlocale()
    listLenguage = []
    listLenguage.append(systemLenguage)
    letters = ()
    for listLeng in listLenguage:
        letters = tuple(listLeng[0]) #recorrido de tupla para convertir la palabra en una tupla con caracteres separados y poder extraer luego solo los 2 primeros valores.
    leng = ''.join(letters[0]+letters[1]) #concatena los 2 primeros digitos de lenguage en o es para usarlo en la dirección de carpeta a buscar por Program Files o Archivos de Programas
    return leng