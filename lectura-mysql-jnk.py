from os import remove
import pandas as pd
import mysql.connector
import os

from datetime import date
from datetime import datetime


fecha=datetime.now()


df = pd.read_csv('datos.txt', sep=" ",header=None,error_bad_lines=False)
cantidad =(df.count())

a = cantidad[0] *2.5
b=cantidad[0]
#conexion1 = mysql.connector.connect( host="sql11.freesqldatabase.com", user= 'sql11507352', passwd='SPg5nlIj2u', db="sql11507352" )
conexion1 = mysql.connector.connect( host="estacion.educatics.org",
				     user= 'educaics_usr_est', passwd='F5z!xZ5jhSyg', db="educaics_db_estacion" )


cursor1=conexion1.cursor()
sql="insert into jnk (fecha,conteo, m3) values (%s,%s,%s)"
datos=(fecha ,str(b) , str(a))
cursor1.execute(sql, datos)
conexion1.commit()
conexion1.close()
print ("insertado")
remove('datos.txt')
