#!/usr/bin/env python
# -*-coding:utf-8-*-
import random
import sys
from Tkinter import *


#vector con todas cada string en Mayusculas
vector=['PIEDRA','PAPEL','TIJERA','LAGARTO','SPOCK']

#Funcion que se ejecuta cuando se da click en el boton
def hacer_click():

        eleccion = opcion.get()
        eleccion = eleccion.upper() #convertir la opcion en Mayusculas para no tener problemas
        if eleccion not in vector: #---------------------|
            etiqueta.config(text="Valor incorrecto")   # | condicional que valida si se encuentra esa palabra en
        else:#-------------------------------------------| el vector
            pc=random.choice(vector)
            etiqueta_4.config(text=pc)
            if eleccion == pc:
                etiqueta.config(text="Empate :| ")
            elif eleccion == "PIEDRA":
                if pc == "TIJERA" or pc == "LAGARTO":
                    etiqueta.config(text="Ganaste :) ")
                else:
                    etiqueta.config(text="Perdiste:")
            elif eleccion == "PAPEL":
                if pc == "PIEDRA" or pc == "SPOCK":
                     etiqueta.config(text="Ganaste :) ")
                else:
                     etiqueta.config(text="Perdiste:")
            elif eleccion == "TIJERA":
                if pc == "PAPEL" or pc == "LAGARTO":
                     etiqueta.config(text="Ganaste :) ")
                else:
                    etiqueta.config(text="Perdiste:")
            elif eleccion == "LAGARTO":
                if pc =="SPOCK" or pc=="PAPEL":
                    etiqueta.config(text="Ganaste :) ")
                else:
                    etiqueta.config(text="Perdiste:")
            elif eleccion == "SPOCK":
                if pc == "TIJERAS" or pc == "PIEDRA":
                    etiqueta.config(text="Ganaste :) ")
                else:
                    etiqueta.config(text="Perdiste:")



app = Tk()
app.title('Mi primera App grafica')

vp = Frame(app)
vp.grid(row=0,column=0,padx=(50,50),pady=(10,10))
vp.columnconfigure(0,weight=1)
vp.rowconfigure(0,weight=1)

etiqueta1 = Label(vp,text="PIEDRA,PAPEL,TIJERA")
etiqueta1.grid(row=1,column=1)

etiqueta_2 = Label(vp,text="LAGARTO,SPOCK")
etiqueta_2.grid(row=1,column=2)

#pc eligio:
etiqueta_3 = Label(vp,text="PC eligio:")
etiqueta_3.grid(row=3,column=1)

#Da la opcion que eligio la computadora
etiqueta_4 = Label(vp,text="")
etiqueta_4.grid(row=3,column=2)

#Muestra si Ganaste o Perdiste
etiqueta = Label(vp,text="")
etiqueta.grid(row=5,column=1)

#caja donde se recoge la informacion
valor = ""
opcion = Entry(vp,width=10,textvariable=valor)
opcion.grid(row=2,column=1)

#boton para validar
boton = Button(vp,text="click!",command=hacer_click)
boton.grid(row=2,column=2)


app.mainloop()
