from os import remove
import pandas as pd
import mysql.connector


df = pd.read_csv('Phj.txt', sep=" ",header=None)
cantidad =(df.count())
a = cantidad[0] *2.5
conexion1 = mysql.connector.connect( host="sql11.freesqldatabase.com", user= 'sql11507352', passwd='SPg5nlIj2u', db="sql11507352" )
cursor1=conexion1.cursor()
sql="insert into estacion(temperatura, humedad) values (%s,%s)"
datos=( str(a) , 1)
cursor1.execute(sql, datos)
conexion1.commit()
conexion1.close()
print ("insertado")
remove('Phj.txt')