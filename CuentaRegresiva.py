from tkinter import *
from datetime import *
from tkinter import ttk
#import time


#-----------------------------------------------------------------------
# Funcion del timer
# Se ejecuta una vez por segundo
# Actualiza la hora y el temporizador
def tmrUnSegundo():

	# Referencio variables globales
	global strvHoraActual
	global strTemporizador
	global titilar
	global temporizadorTime
	
	# Actualizao hora actual
	strvHoraActual.set(datetime.now().strftime("%H:%M:%S"))
	
	if stopTemporizador.get() == 1:
		if temporizadorTime > time.min:
			temporizadorTime = (datetime.combine(date(1,1,1), temporizadorTime) - timedelta(seconds = 1)).time()
			strTemporizador.set(temporizadorTime.strftime("%H:%M:%S"))

	# Si hago el else el primer segundo en "0" no se pone en rojo...
	if temporizadorTime == time.min:
		if titilar.get() == 0:
			lblTemporizador.config(fg="red")
			titilar.set(1)
		else:
			lblTemporizador.config(fg="black")
			titilar.set(0)

	arrancarTmrUnSegundo()

#-----------------------------------------------------------------------
def arrancarTmrUnSegundo():
	lblReloj.after(1000, tmrUnSegundo)
#-----------------------------------------------------------------------

def cronometro():
	global strTimeCrono
	global stopCrono
	global cronometroTime

	if stopCrono.get() == 1:
		cronometroTime = (datetime.combine(date(1,1,1), cronometroTime) + timedelta(milliseconds = 100)).time()

	strTimeCrono.set(cronometroTime.strftime("%H:%M:%S:%f"))
	arrancarTmrCrono()

#-----------------------------------------------------------------------

def arrancarDetenerCrono():
	global stopCrono
	global txtBtnArrancarDetener
	if stopCrono.get() == 1:
		stopCrono.set(0)
		txtBtnArrancarDetener.set("Start")
	else:
		stopCrono.set(1)
		txtBtnArrancarDetener.set("Stop")
#-----------------------------------------------------------------------
def resetDetenerCrono():
	global strTimeCrono
	global cronometroTime
	cronometroTime = time.min
	strTimeCrono.set(cronometroTime.strftime("%H:%M:%S:%f"))
	lblCronometro.after(100, cronometro)
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
def arrancarTmrCrono():
	global strTimeCrono
	lblCronometro.after(100, cronometro)


#-----------------------------------------------------------------------
def setTemporizador():
	inputTime = Tk()
	Label(inputTime, text="Tiempo en Segundos... FALTA IMPLEMENTAR ESTA VENTANA").grid(row=0)

	
	e1 = Entry(inputTime)

	e1.grid(row=0, column=1)

	Button(inputTime, text='Cancelar', command=dummyFun).grid(row=3, column=0, sticky="W", pady=4)
	Button(inputTime, text='Set', command=dummyFun).grid(row=3, column=1, sticky="W", pady=4)

	inputTime.mainloop()

#-----------------------------------------------------------------------
def __callback(self, P):
    if str.isdigit(P) or P == "":
        return True
    else:
        return False
#-----------------------------------------------------------------------
def arrancarDetenerTemp():
	global stopTemporizador
	global txtBtnArrancarDetenerTemp
	if stopTemporizador.get() == 1:
		stopTemporizador.set(0)
		txtBtnArrancarDetenerTemp.set("Start")
	else:
		stopTemporizador.set(1)
		txtBtnArrancarDetenerTemp.set("Stop")

def dummyFun():
	pass


#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------

# main 
root=Tk()

root.title("Manipulacion de tiempos....")
root.config(width=300, height=300)

frameRoot = Frame()
frameRoot.pack(expand = 1, fill='both')


# Tabs --------------------------------------------------------------------------------------
tabRoot = ttk.Notebook(frameRoot)

tabReloj = ttk.Frame(tabRoot)
tabTemporizador = ttk.Frame(tabRoot)
tabCronometro = ttk.Frame(tabRoot)

tabRoot.add(tabReloj, text="Reloj")
tabRoot.add(tabTemporizador, text="Temporizador")
tabRoot.add(tabCronometro, text="Cronometro")
tabRoot.pack()


# Solapa Reloj -----------------------------------------------------------------------------
strvHoraActual = StringVar()
strvHoraActual.set(datetime.now().strftime("%H:%M:%S"))

lblReloj = Label(tabReloj, textvariable=strvHoraActual, width=40)
lblReloj.pack()

# Solapa temporizador -----------------------------------------------------------------------
titilar = IntVar()
titilar.set(0)

temporizadorTime = time.min
temporizadorTime = (datetime.combine(date(1,1,1), temporizadorTime) + timedelta(seconds = 10)).time()

strTemporizador=StringVar()
strTemporizador.set(temporizadorTime.strftime("%H:%M:%S"))

lblTemporizador = Label(tabTemporizador, textvariable=strTemporizador, width=40)
lblTemporizador.grid(row=0, column=0,  padx=10, pady=10, columnspan = 2)

btnSetTemporizador = Button(tabTemporizador,text="Set Temporizador", width=20, command=lambda:setTemporizador())
btnSetTemporizador.grid(row=1, column=0,  padx=10, pady=10)

txtBtnArrancarDetenerTemp = StringVar()
txtBtnArrancarDetenerTemp.set("Start")
btnSetTemporizador = Button(tabTemporizador,textvariable=txtBtnArrancarDetenerTemp, width=20, command=lambda:arrancarDetenerTemp())
btnSetTemporizador.grid(row=1, column=1,  padx=10, pady=10 )

stopTemporizador = IntVar()
stopTemporizador.set(0)

# Solapa Cronometro ------------------------------------------------------------------------
cronometroTime = time.min

strTimeCrono = StringVar()
strTimeCrono.set(cronometroTime.strftime("%H:%M:%S:%f"))

lblCronometro = Label(tabCronometro, textvariable=strTimeCrono, width=40)
lblCronometro.grid(row=0, column=0,  padx=10, pady=10, columnspan = 2)

txtBtnArrancarDetener = StringVar()
txtBtnArrancarDetener.set("Start")
btnArrancarDetenerCrono=Button(tabCronometro, textvariable=txtBtnArrancarDetener, width=15, command=lambda:arrancarDetenerCrono())
btnArrancarDetenerCrono.grid(row=1, column=0,  padx=10, pady=10)
btnResetCrono=Button(tabCronometro,text="Reset", width=15, command=lambda:resetDetenerCrono())
btnResetCrono.grid(row=1, column=1,  padx=10, pady=10 )

stopCrono = IntVar()
stopCrono.set(0)

# --------------------------------------------------------------------------------------------


arrancarTmrUnSegundo()
arrancarTmrCrono()

root.mainloop()