# Configuración para RFID

En el caso del archivo **Config_RFID.py**, este deberá ser ejecutado desde la Raspberry Pi 4 Modelo B. Para esto, cabe señalar los siguientes puntos de configuración, a continuación, dejaremos una serie de instrucciones para realizar dicha configuración.

### Réquisitos previos.

1. Realizar la instalación del Sistema Operativo de Raspberry junto con la configuración de este.
- Nota: Para ello, te recomendamos seguir el siguiente [curso](https://edu.codigoiot.com/mod/lesson/view.php?id=2089&pageid=2580). 
2. Contar con los contenedores de Docker del repositorio:
    - [Servidor IoT básico con docker compose](https://github.com/codigo-iot/servidor-IoT-basico-docker-compose/tree/main)


## Instrucciones.

1. Entrar a la terminal de Raspberry Pi 4 y entrar a documentos para crear un directorio con los siguientes comandos:

~~~
cd Documentos
mkdir codigo
cd codigo
~~~

2. Una vez hayas entrado a la carpeta creada, para poder utilizar el sensor RFID RC522 de manera adecuada, es necesario preparar Python. Para ello, se instala python3-dev y python-pip con el siguiente comando:  

~~~
sudo apt install python3-dev python3-pip 
~~~

3. Para poder realizar una comunicación SPI como la necesaria para interactuar con el RFID RC522 se necesita instalar la librería spidev con el siguiente comando: 

~~~
pip3 install spidev 
~~~

4. A continuación, es necesario instalar la librería MFRC522 en la Raspberry Pi, con el siguiente comando: 

~~~
pip3 install mfrc522  
~~~

5. Seguido de esto, se instalará la librería paho para realizar las conexiones a MQTT.

~~~
pip3 install paho-mqtt
~~~

6. Realizado esto se creará o copiará el archivo Config_RFID.py y realizado esto, se correrá el programa con el comando 

~~~
python Config_RFID.py
~~~

- Nota: Para comprobar su funcionamiento, puedes suscribirte al tópico usando los contenedores docker del [servidor IoT](https://github.com/codigo-iot/servidor-IoT-basico-docker-compose/tree/main) con el comando:

~~~
docker exec -it [nombre-contenedor] mosquitto_sub -h [direccion_ip/localhost] -t [tema-o-tópico-de-publicación]
~~~

## Resultados

![](https://github.com/elizabeth-arevalo/prestamo-de-equipos-con-RFID/blob/main/img/congig-rfid.jpeg)

![](https://github.com/elizabeth-arevalo/prestamo-de-equipos-con-RFID/blob/main/img/circuito.jpeg)
