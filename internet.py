

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



    #miConexion = mysql.connector.connect( host="ace.com.pe", user= 'acecompe_prueba1', passwd='.&ve3Z5_VJW0', db="acecompe_prueba1" )
    #miConexion = mysql.connector.connect( host="ace.com.pe", user= 'acecompe_prueba1', passwd='.&ve3Z5_VJW0', db="acecompe_prueba1" )
    miConexion = mysql.connector.connect( host="estacion.educatics.org", user= 'educaics_usr_est', passwd='F5z!xZ5jhSyg', db="educaics_db_estacion" )

    cur = miConexion.cursor()
    csv_data = csv.reader(open('/home/pi/lecturas.csv'))

    for row in csv_data:
          print (row)
          cur.execute('insert into datos (fecha,uv,valo2,pluviometro,metrosc,humedad,temperatura) values (%s,%s,%s,%s,%s,%s,%s)',row)


          miConexion.commit()
          with open("/home/pi/lecturas.csv",'w') as f:
              pass

    s.close()
