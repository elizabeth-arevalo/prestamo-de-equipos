import RPi.GPIO as GPIO  # Importamos la librería RPi.GPIO para controlar los pines GPIO de la Raspberry Pi
from time import sleep  # Importamos la función sleep desde el módulo time para pausas en el programa
from mfrc522 import SimpleMFRC522  # Importamos la clase SimpleMFRC522 del módulo mfrc522 para el manejo del lector RFID
from paho.mqtt import client as mqtt  # Importamos el módulo cliente del paquete paho.mqtt para la comunicación MQTT
from datetime import datetime  # Importamos la clase datetime del módulo datetime para trabajar con fechas y horas

# MQTT
cliente = mqtt.Client()  # Creamos una instancia del cliente MQTT
cliente.connect("52.28.227.73", 1883, 60)  # Establecemos la conexión con el servidor MQTT en la dirección IP y puerto especificados
cliente.loop_start()  # Iniciamos un hilo de fondo para el manejo de comunicación MQTT

# RFID
reader = SimpleMFRC522()  # Creamos una instancia del lector RFID SimpleMFRC522
print("Coloca una tarjeta sobre el lector")  # Imprimimos un mensaje para indicar al usuario que coloque una tarjeta en el lector
while True:  # Iniciamos un bucle infinito
    try:  # Manejamos cualquier excepción que ocurra en este bloque
        id, text = reader.read()  # Leemos el ID y el texto de la tarjeta colocada en el lector
        print("El ID de la tarjeta es:\n")
        print(id)  # Imprimimos el ID de la tarjeta leída
        text = input('Estatus (Prestamo o Devolucion):')  # Solicitamos al usuario ingresar el estado de la tarjeta

        timestamp = datetime.now()  # Obtenemos la fecha y hora actual
        print("Timestamp: {}".format(timestamp))  # Imprimimos la marca de tiempo
        print("Now place your tag to write")  # Indicamos al usuario que coloque la tarjeta para escribir
        reader.write(text)  # Escribimos el estado de la tarjeta en la misma

        mensaje = "{{\"lector\": {}, \"tarjeta\": {}, \"hora\": \"{}\"}}".format(id, text, timestamp)  # Formateamos un mensaje JSON con el ID, el estado de la tarjeta y la marca de tiempo
        cliente.publish("prestamoEquipos/rpi/rfid", mensaje)  # Publicamos el mensaje en el tema "prestamoEquipos/rpi/rfid" en el servidor MQTT

        sleep(2)  # Hacemos una pausa de 2 segundos
    except:  # Si ocurre una excepción
        GPIO.cleanup()  # Limpiamos la configuración de los pines GPIO
        exit()  # Salimos del programa