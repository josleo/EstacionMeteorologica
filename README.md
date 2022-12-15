# EstacionMeteorologica
proyecto de iot para la creacion de una estacion meteorologica de bajo costo

## almacenarDatos.py
en este archivo encontraremos la logica de extracion de los datos de los diferentes sensores que utilizamos en el proyecto , dht22, jnk.50001c , uv 
el  cual almacena estas lecturas en un archivo 
## lecturas.csv
es un archivo creado para el almacenamiento temporal de las lecturas de los sensores 

## lecturaNJK.py
es un archivo python que se ejecuta para la lecura del sensor jnk.50001c el cual almancea las lecturas en un archivo plano llamad datos.txt

## datos.txt

es un archivo plano el cual sirve como almacen temporal de las lecturas del sensor jnk.50001c

## internet.py
 este archivo python no ayuda a enviar todas las ecturas que se realizaron de los diferentes sensores  que se almanceanron en el archivo lecturas.csv-- son enviados a una base de datos en la nube

 ## bot_M.py 
es un archivo python el cual contiene codigo de nuestro bot creado en Telegram 

## GUVA-125.ino 
archivo para arduino el cual sera leido por puerto serial de la rasberry pi