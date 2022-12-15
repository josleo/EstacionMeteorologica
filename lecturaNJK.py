from time import sleep
import RPi.GPIO as GPIO
import csv
import time
import os
# Set up BCM GPIO numbering.
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# Set up input pins.
SENSOR_1_INPUT = 18
GPIO.setup(SENSOR_1_INPUT, GPIO.IN)

lista = [" "]
lista2 = ["1"]
#datos =  pd.DataFrame()
# Initiate the loop.
while True:
    # Get signals from Arduino as digital input values.
    SENSOR_1_VALUE = GPIO.input(SENSOR_1_INPUT)
    # Print values.
    if(SENSOR_1_VALUE == 0):
        lista.append(str(SENSOR_1_VALUE))
        valorSTR = str(SENSOR_1_VALUE)

        with open('datos.txt', 'a', newline='') as csvfile:
            os.chmod("/home/pi/datos.txt", 0o755)

            csvfile.write(','.join(valorSTR)+'\n')
            print (valorSTR)
            time.sleep(0.1)

    else:
        with open('datos.txt', 'a', newline='') as csvfile:
            os.chmod("/home/pi/datos.txt", 0o755)
            csvfile.write(','.join(" ")+'\n')
            os.chmod("datos.txt", 0o755)

#            break
            print (lista2)
            time.sleep(0.1)

#datos['Nombre'] = lista

#print (datos)
