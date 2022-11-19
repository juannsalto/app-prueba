#############################
# Primer commit main App- Prueba
# *Subir a Github
# * Index.py
# ejecutable.exe
# release: 26/10/2022
# developer: Salto Juan Bautista
##############################

from ast import While
from operator import concat
from tkinter import N, Y
import math

#forma de importacion simple de otro archivo.py
#funciona solo si comparten proyecto
#import  calendario
 #main-resources
talles_input = "M", "S", "X", "XL", "XXL" 

modelo = "tiro ancho", "tiro bajo", "chupin", "acampanado", "roto", "corte inglés"

quiereSeguir = Y,N

continuamos = Y,N



while True:
 quiereSeguir = input('¿Comenzamos?')
 if quiereSeguir != N:
     #index0

     #GUIA BASICA INPUT SIN VERIFICACION
     #talles = input('ingrese talle')
     #print ('usted quiere, ' + talles)

     #modelo = input('ingrese modelo')
     #print ('usted quiere, ' + modelo)

     #index  con verificacion

     while True:
        talles = input("ingrese un talle")
        if talles!= "XL" and talles!= "S":
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


     #cambios en las variables (CONTADOR)
     #CLASE QUE CUENTA DE FORMA GENERICA E IMPRIME EN CONSOLA

     cuentaModelo = 0
     cuentaTalle = 0

     while True:
        if modelo == "tiro bajo":
         cuentaModelo+=1
         print(cuentaModelo)
         break
        continue
     while True:    
        if talles == "XL":
         cuentaTalle+=1
         print(cuentaTalle)

        break
        continue
 break
 continue



    
   

