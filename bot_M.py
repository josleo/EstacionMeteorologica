import telebot
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




bot = telebot.TeleBot("5537330469:AAEa_kLtkGnqmxAUhA3e09FsRbqzGUhevMM")

#5537330469:AAEa_kLtkGnqmxAUhA3e09FsRbqzGUhevMM




chat_id= str(-781602172)


@bot.message_handler(commands=['ayuda'])
def ayuda(messaje):

        texto = messaje.text

#        bot.send_message(chat_id, messaje.chat.id)        #chatID = messaje.chat.id # <--- ChatID para todos los ejercicios
        #bot.send_message(chat_id, texto)
        bot.send_message(chat_id,'....BIENVENIDO AL BOT  ....')
       # bot.send_message(x|, text="/temperatura -comando para ver el ultimo registro de temperatura")
        bot.send_message(chat_id, text='/temp  -comando  para ver  temperatura y humedad ')
        bot.send_message(chat_id, text='/uv  -comando  para ver  radiación ultravioleta ')



@bot.message_handler(commands=['temp'])
def ayuda(messaje):


        import Adafruit_DHT
        import time
        sensor = Adafruit_DHT.DHT22 #Cambia por DHT22 y si usas dicho sensor
        pin = 4 #Pin en la raspberry donde conectamos el sensor
        humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

	#return(round(humedad,2), round(temperatura,2))
        bot.send_message(chat_id, text=("humedad - "+str(humedad)))
        bot.send_message(chat_id, text="temperatura - "+str(temperatura))


@bot.message_handler(commands=['uv'])
def ayuda(messaje):


        ser = serial.Serial("/dev/ttyACM0", 9600)
        global value
        value = (ser.readline().strip())
        value = float(value)
        bot.send_message(chat_id, text="UV - "+str(value))
        ser.close()


bot.infinity_polling()
