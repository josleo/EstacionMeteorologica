from csv import writer
from os import remove
import pandas as pd
import mysql.connector
import serial

from datetime import date
from datetime import datetime

from os import remove
import pandas as pd
import mysql.connector
import os

from datetime import date
from datetime import datetime


def jnk():
	fecha=datetime.now()
	df = pd.read_csv('datos.txt', sep=" ",header=None,error_bad_lines=False)
	cantidad =(df.count())

	volumen = cantidad[0] *2.5
	cant=cantidad[0]
	remove('datos.txt')
	return (cant,volumen)


def arduino ():
    ser = serial.Serial("/dev/ttyACM0", 9600)
    global value
    value = (ser.readline().strip())
    value = int(value)

    if (value==0):
        condicion  = "ninguna"
        return (value,condicion)


    if (value==1):
        condicion  = "bajo"
        return (value,condicion)


    if (value==2):
        condicion  = "moderado"
        return (value,condicion)
	
    if (value==3):
        condicion  = "alto"
        return (value,condicion)

    if (value==4):
        condicion  = "muy altoa"
        return (value,condicion)


    if (value==5):
        condicion  = "extremadamente  alto"
        return (value,condicion)

    ser.close()

def dht22():
	import Adafruit_DHT
	import time
	sensor = Adafruit_DHT.DHT22 #Cambia por DHT22 y si usas dicho sensor
	pin = 4 #Pin en la raspberry donde conectamos el sensor
	humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

	return(round(humedad,2), round(temperatura,2))
#	 round(humedad,2))

def insert():
	valor,condiciones= arduino()
	cantidad,volumen= jnk()
	humedad,temperatura = dht22()

	fecha=datetime.now()

	print (valor,condiciones ,cantidad,volumen , humedad,temperatura )



	list_data=[fecha,valor,condiciones,cantidad,volumen,humedad,temperatura]

	with open('lecturas.csv', 'a', newline='') as f_object:

	    os.chmod("/home/pi/lecturas.csv", 0o0777)
	    writer_object = writer(f_object)
	    writer_object.writerow(list_data)
	    f_object.close()
insert()

