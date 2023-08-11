# prestamo-de-equipos-con-RFID
En este repositorio, se desarrolla el proyecto de préstamo de equipos orientado a una universidad por medio de IoT

# Introducción

En este proyecto, buscamos automatizar el proceso de prestámo de equipos en las instituciones, todo esto haciendo uso del conocimiento impartido, se te enseñará paso a paso el desarrollo del proyecto para que lo puedas implementar en tu institución o empresa. 

## Requisitos

### Requisitos previos. 

Para consultar el montaje del contenedor en Docker que se utilizará para el desarrollo del proyecto, comparto el siguiente repositorio: 

- [Servidor IoT básico con docker compose](https://github.com/codigo-iot/servidor-IoT-basico-docker-compose/tree/main)


### Lista de materiales necesarios.

A continuación, está una lista de los dispositivos necesarios para el desarrollo del proyecto.

- Raspberry corriendo Ubuntu 20.04
- Software Visual Studio Code configurado para proyectos MAVEN
- Sensor RFID MFRC522 RF IC
- Protoboard
- GPIO Extension Board
- Jumpers
- Tarjeta RFID
- Etiqueta RFID (Opcional)

### Software necesario
Para realizar este ejercicio necesitas lo siguiente

- [Ubuntu 20.04](https://releases.ubuntu.com/20.04/)
- [Docker Engine](https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script)
- [Mosquitto Docker Image](https://hub.docker.com/_/eclipse-mosquitto/)
- [NodeRed Docker Image](https://hub.docker.com/r/nodered/node-red)
- [MySQL Docker Image](https://hub.docker.com/_/mysql)
- Visual Studio Code
- Virtual Box

#### Hardware.
- Computadora

### Material de referencia

En los siguientes enlaces puedes encontrar cursos en la plataforma de edu.codigoiot.com que contienen el conocimiento necesario para llevar a cabo las configuraciones necesarias.

- [Linux Essentials](https://edu.codigoiot.com/course/view.php?id=984)
- Máquinas Virtuales
- [Instala Ubuntu en Virtual Box](https://edu.codigoiot.com/course/view.php?id=812)
- [Introducción a Docker]()
- [Instalación de Docker]()
- [Docker Compose]()

## Circuito sugerido

El siguiente circuito te puede mostrar las conexiones necesarias para comunicar el sensor RFID MFRC522 RF IC con la Raspberry Pi.

![](https://github.com/elizabeth-arevalo/prestamo-de-equipos-con-RFID/blob/main/img/circuito.png)

## Flow sugerido

El siguiente Flow fue utilizado en el desarrollo del proyecto, mismo que puedes encontrar en l carpeta NodeRed de este repositorio.

![](https://github.com/elizabeth-arevalo/prestamo-de-equipos-con-RFID/blob/main/img/flow.png)

## Dashboard

![](https://github.com/elizabeth-arevalo/prestamo-de-equipos-con-RFID/blob/main/img/dashboard.png)
