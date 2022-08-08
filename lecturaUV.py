from os import remove
import pandas as pd
import mysql.connector
import serial

from datetime import date
from datetime import datetime

#fecha=datetime.now()


def arduino ():
    ser = serial.Serial("/dev/ttyACM0", 9600)
    global value
    value = (ser.readline().strip())
    value = int(value)

    #condiciones(value)
    if (value==0):
        condicion  = "ninguna"
    if (value==1):
        condicion  = "bajo"
    if (value==2):
        condicion  = "moderado"
    if (value==3):
        condicion  = "alto"
    if (value==4):
        condicion  = "muy altoa"
    if (value==5):
        condicion  = "extremadamente  alto"
    condiciones(value,condicion)
    ser.close()

def condiciones(valor,condicion):
    valor= value
    condicional = condicion
    fecha=datetime.now()
    #print(valor)
    conexion1 = mysql.connector.connect( host="estacion.educatics.org", user= 'educaics_usr_est', passwd='F5z!xZ5jhSyg', db="educaics_db_estacion" )

    #conexion1 = mysql.connector.connect( host="sql11.freesqldatabase.com", user= 'sql11507352', passwd='SPg5nlIj2u', db="sql11507352" )
    cursor1=conexion1.cursor()
    sql="insert into uv (fecha,valor, condicion) values (%s,%s,%s)"
    datos=(fecha, valor , condicional)
    cursor1.execute(sql, datos)
    conexion1.commit()
    conexion1.close()

valores =arduino()
