import os
import sys

def ruta_base():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.abspath(".")

def ruta_datos(nombre_archivo):
    return os.path.join(ruta_base(), "data", nombre_archivo)
