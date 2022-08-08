

import pymysql
import csv
import mysql.connector
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
try:
    s.connect(("www.google.com", 80))
except (socket.gaierror, socket.timeout):
    print("Sin conexión a internet")
else:

    miConexion = mysql.connector.connect( host="estacion.educatics.org", user= 'educaics_usr_est', passwd='F5z!xZ5jhSyg', db="educaics_db_estacion" )
    cur = miConexion.cursor()
    csv_data = csv.reader(open('/home/pi/lecturas.csv'))

    for row in csv_data:
          print (row)

#cursor.execute('''INSERT INTO ejemplo5 (sensor,fecha,nombre,apellido,condicion,foto,termica) VALUES(%s,%s,%s,%s,%s,%s,%s)''', row)
          cur.execute('insert into datos (fecha,valo1,valo2,valo3,valo4,valo5,valo6) values (%s,%s,%s,%s,%s,%s,%s)',row)


          miConexion.commit()
          with open("/home/pi/lecturas.csv",'w') as f:
              pass

    s.close()
