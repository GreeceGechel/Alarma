from tkinter import *
import time
import pygame, sys
from pygame.locals import*
from pygame import mixer
from tkinter import filedialog
from tkinter import messagebox as messageBox
import tkinter as tk
root = Tk()
pygame.init()

root.geometry("600x600")

def clock():

    horas=time.strftime("%H")
    horaLocal = horas 
    print(horaLocal)
    miEtiqueta.config(text=horaLocal)
    miEtiqueta.after(1000,clock)


def clock2():
    minutos=time.strftime("%M")

    
    minutosLocal =minutos 
    print(minutosLocal)
    miEtiquetaMI.config(text=minutosLocal)
    miEtiquetaMI.after(1000,clock2)
     
def clock4():
     
    segundos=time.strftime("%S")

    global horaLocal
    horaLocal =segundos 
    print(horaLocal)
    miEtiquetaS.config(text=horaLocal)
    miEtiquetaS.after(1000,clock4)
    


def clock3():

 horas=time.strftime("%H")
 minutos=time.strftime("%M")
 segundos=time.strftime("%S")
 horaL= horas + ":"+ minutos +":" + segundos 
 miEtiquetaM.after(1000,clock3)

 

 
 if horaL==tiempo.get():
            ventanaPrin.config(bg="#00ffff")
            pygame.mixer.music.load("C:\\Users\\Junio\\OneDrive\\Escritorio\\PROGRAMAS DE PYTHON\\INTERFAZ_GRAFICA\\NoSurprises.mp3")
            pygame.mixer.music.play()

def parar():
    pygame.mixer.music.pause()


ventanaPrin=Frame(root)
ventanaPrin.pack(fill="both", expand=1)#permite visualizar el archivo

sonar=StringVar()
tiempo=StringVar()




titulo=Label(ventanaPrin,text="Alarma",font=("Comic Sans Ms",20),bg="#00ffff")
titulo.place(relx=0.3,rely=0.0)


Reloj=Label(ventanaPrin,text="RELOJ:",font=("Comic Sans Ms",20),bg="#00ffff")
Reloj.place(relx=0.1,rely=0.1)

miEtiquetaMI=Label(ventanaPrin,text=":",font=("Comic Sans Ms",20),bg="#00ffff",width=5,height=1)
miEtiquetaMI.place(relx=0.50,rely=0.1)

miEtiquetaS=Label(ventanaPrin,text="",font=("Comic Sans Ms",20),bg="#00ffff",width=5,height=1)
miEtiquetaS.place(relx=0.65,rely=0.1)

miEtiqueta=Label(ventanaPrin,text="",font=("Comic Sans Ms",20),bg="#00ffff",width=5,height=1)
miEtiqueta.place(relx=0.35,rely=0.1)

miEtiquetaM=Label(ventanaPrin,text="",font=("Comic Sans Ms",20),bg="#00ffff",width=5,height=1)




Alarma=Label(ventanaPrin,text="Establecer Alarma",font=("Comic Sans Ms",18),bg="#00ffff")
Alarma.place(relx=0.1,rely=0.3)

Am=Entry(ventanaPrin,textvariable=tiempo,font=("Comic Sans Ms",15))
Am.place(relx=0.5,rely=0.3)

def preguntar_ok():
    respuesta=messageBox.askyesno("Pregunta","¿Deseas establecer esta alarma?")
    print(type(respuesta))
    print(respuesta)
    if respuesta == bool("True"):
         clock3()
    


boton5=Button(root,text="Establecer alarma", bg="#FF0000",fg="#FFFACD",font=("Comic Sans Ms",15,"bold"),width=15,height=1,command=preguntar_ok)
boton5.place(relx=0.2,rely=0.5)

Stop1=Button(ventanaPrin,text="Detener",bg="#00ffff",width=15,height=3,command=parar)
Stop1.place(relx=0.6,rely=0.5)


clock()

clock4()
clock2()



root.mainloop()