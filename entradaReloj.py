#sudo apt -get install python3-tk

from tkinter import *

raiz=Tk()

raiz.title("Cuenta Regresiva")
raiz.iconbitmap("reloj.ico")
raiz.geometry('250x250')

miFrame=Frame(raiz)

miFrame.pack(expand = True)


miHora=StringVar()
miMin=StringVar()
miSeg=StringVar()


informacion=StringVar()
output="" #VARIABLE GLOBAL PARA informar


cuadroHora=Entry(miFrame,width=10,textvariable=miHora)
cuadroHora.grid(row=0,column=1,padx=10,pady=10)

cuadroMin=Entry(miFrame,width=10,textvariable=miMin)
cuadroMin.grid(row=1,column=1,padx=10,pady=10)

cuadroSeg=Entry(miFrame,width=10,textvariable=miSeg)
cuadroSeg.grid(row=2,column=1,padx=10,pady=10)

horaLabel=Label(miFrame,text="Hora:",justify=LEFT)
horaLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

minLabel=Label(miFrame,text="Min:",justify=LEFT)
minLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

segLabel=Label(miFrame,text="Seg:",justify=LEFT)
segLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

informacionPantalla=Label(miFrame,textvariable=informacion)
informacionPantalla.grid(row=3,column=1,padx=10,pady=10)


def codigoBoton(horas,minutos,segundos):
	global output
	output="HH : " + horas + "MM : " + minutos + "SS: " + segundos
	informacion.set(output)

	
botonEnvio=Button(raiz,text="Setear",command=lambda:codigoBoton(miHora.get(),miMin.get(),miSeg.get()))
botonEnvio.pack()



raiz.mainloop()