# Configuración del Dashboard en Grafana

## Introducción.

A continuación, explicaremos paso a paso la configuración del entorno de Grafana para hacer su integración con NodeRed, de esta manera logrando tener una interfaz gráfica mucho más amigable.

Toma en cuenta que este proceso esta orientado para el sistema operativo **Ubuntu LTS 20.04**

### Instrucciones.

1. Primeramente como en cualquier instalación, debemos asegurarnos de que no hayan actualizaciones, para ello ejecutaremos los siguientes dos comandos.
~~~
sudo apt update

sudo apt upgrade
~~~

2. Hecho esto, debemos descargar e instalar los paquetes necesarios para los repositorios de Grafana:

~~~
sudo apt-get install -y apt-transport-https

sudo apt-get install -y software-properties-common wget

sudo wget -q -O /usr/share/keyrings/grafana.key https://apt.grafana.com/gpg.key
~~~

3. Para añadir las últimas versiones de los repositorios, ejecutar este comando:

~~~
echo "deb [signed-by=/usr/share/keyrings/grafana.key] https://apt.grafana.com beta main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
~~~

4. Para terminar, se deberá ejecutar el comando para su instalación:

~~~
sudo apt install grafana
~~~

# Configuración de Grafana.
### Réquisitos previos

Para poder iniciar con Grafana, primero debemos realizar su instalación, proceso el cuál puedes encontrar en este mismo curso.

## Instrucciones.

Hecha la instalación, seguiremos con estos pasos.

1. Acceder a la interfaz web de Grafana: Una vez que Grafana esté instalado y funcionando, puedes acceder a su interfaz web a través de un navegador web. Por lo general, se encuentra en http://localhost:3000/. Se te pedirá que inicies sesión con las credenciales predeterminadas.
2. Para el primer inicio de sesión, introduzca admin en los campos username y password.

![](https://github.com/elizabeth-arevalo/prestamo-de-equipos-con-RFID/blob/main/img/grafana-login.png)
    - Hecho esto, se solicitar el cambio de contraseña para el usuario admin.

3. Agregar el origen de datos (Data Source): Después de iniciar sesión en Grafana, el siguiente paso es agregar el origen de datos que se conectará a la base de datos MySQL. Para ello, sigue estos pasos:
    - Haz clic en el ícono de engranaje (Configuration) en la barra lateral izquierda.
    - Selecciona "Data Sources" en la sección "Configuration".
    - Haz clic en "Add data source".
    - Busca y selecciona "MySQL" como el tipo de base de datos.

![](https://github.com/elizabeth-arevalo/prestamo-de-equipos-con-RFID/blob/main/img/grafana.png)

4. Configurar el origen de datos MySQL: A continuación, debes proporcionar la información de conexión para la base de datos MySQL:
    - Nombre del origen de datos (Data Source Name).
    - Dirección del servidor MySQL (Host).
    - Puerto de la base de datos (si es diferente al predeterminado 3306).
    - Nombre de la base de datos que creaste para este proyecto (Database).
    - Nombre de usuario y contraseña con los permisos adecuados para acceder a la base de datos (User y Password).

5. Guardar y probar la configuración: Una vez que hayas ingresado todos los detalles de conexión, haz clic en "Save & Test" para guardar y probar la configuración. Grafana intentará conectarse a la base de datos MySQL utilizando los datos proporcionados.

6. Crear paneles y gráficos: Ahora que el origen de datos está configurado, puedes comenzar a crear paneles y gráficos en Grafana basados en los datos almacenados en la base de datos MySQL. Puedes usar consultas SQL para obtener los datos y luego visualizarlos en forma de gráficos, tablas y otros tipos de visualizaciones.

## Referencias.

- [Documentación de Grafana](https://grafana.com/docs/grafana/latest/setup-grafana/installation/debian/)  