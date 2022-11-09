#############################
# Primer commit main App- Prueba
# *Subir a Github
# * Index.py
# ejecutable.exe
# release: 26/10/2022
# developer: Salto Juan Bautista
##############################

from ast import While
from cgitb import reset
from operator import concat
from tkinter import N, Y

#forma de importacion simple de otro archivo.py
#funciona solo si comparten proyecto
import  calendario


#main-resources
talles = "L", "M", "S", "X" "XL", "XXL" 

modelo = "tiro ancho", "tiro bajo", "chupin", "acampanado", "roto", "corte inglés"

#index

#GUIA BASICA INPUT SIN VERIFICACION
talles = input('ingrese talle')
print ('usted quiere, ' + talles)

modelo = input('ingrese modelo')
print ('usted quiere, ' + modelo)


while True:
        talles = input('ingrese talle')
        if talles != "XL":
            print("Pone un talle valido")
        else:
            print("Genial")
            break
        continue

while True:
        modelo = input('ingrese modelo')
        if modelo != "tiro bajo":
            print("elija un modelo valido")
        else:
            print("Bien")
            break
        continue


#calendario-utilidad en calendario.py

