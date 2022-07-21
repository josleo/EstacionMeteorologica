from os import remove
import pandas as pd
import mysql.connector
import serial

def arduino ():
    ser = serial.Serial("/dev/ttyACM0", 9600)
    global value
    value = (ser.readline().strip())
    value = int(value)
#    condiciones(value)
    ser.close()

def condiciones(valor):
    valor= value
    #print(valor)
    conexion1 = mysql.connector.connect( host="sql11.freesqldatabase.com", user= 'sql11507352', passwd='SPg5nlIj2u', db="sql11507352" )
    cursor1=conexion1.cursor()
    sql="insert into estacion(temperatura, humedad) values (%s,%s)"
    datos=( valor , 1)
    cursor1.execute(sql, datos)
    conexion1.commit()
    conexion1.close()

valores =arduino()
