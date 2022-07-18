from time import sleep
import RPi.GPIO as GPIO
import csv

# Set up BCM GPIO numbering.
GPIO.setmode(GPIO.BCM)
# Set up input pins.
SENSOR_1_INPUT = 18
GPIO.setup(SENSOR_1_INPUT, GPIO.IN)

lista = []
lista2 = ["2"]
#datos =  pd.DataFrame()
# Initiate the loop.
while True:
    # Get signals from Arduino as digital input values.
    SENSOR_1_VALUE = GPIO.input(SENSOR_1_INPUT)
    # Print values.
    if(SENSOR_1_VALUE == 0):
        lista.append(str(SENSOR_1_VALUE))
        print (SENSOR_1_VALUE)
#    datos['Nombre'] = lista
#    datos.append(SENSOR_1_VALUE)
        with open('Phj.txt', 'a', newline='') as csvfile:
            csvfile.write(','.join(lista)+'\n')
#            break

    else:
        with open('Phj.txt', 'a', newline='') as csvfile:
            csvfile.write(','.join(lista2)+'\n')
#            break

#datos['Nombre'] = lista

#print (datos)

