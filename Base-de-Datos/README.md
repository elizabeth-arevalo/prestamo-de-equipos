# Base de datos MySQL

A continuación, te mostraremos la creación de la base de datos para el proyecto.

Se incluirán tres tablas principales: 
- Estudiantes, Equipos y Préstamos. 

Vamos a definir las tablas y sus campos con los siguientes query.

- **Tabla estudiantes:**
~~~
CREATE TABLE Estudiantes (

  ID_Estudiante INT AUTO_INCREMENT PRIMARY KEY,

  Matricula VARCHAR(10) UNIQUE NOT NULL,

  Nombre VARCHAR(50) NOT NULL,

  Apellido VARCHAR(50) NOT NULL,

  Correo VARCHAR(100) NOT NULL,

  Telefono VARCHAR(15) NOT NULL

);
~~~

- **Tabla equipos:**

~~~
CREATE TABLE Equipos (

  ID_Equipo INT AUTO_INCREMENT PRIMARY KEY,

  Nombre_Equipo VARCHAR(100) NOT NULL,

  Descripcion VARCHAR(255) NOT NULL,

  Estado ENUM('Disponible', 'En préstamo', 'En reparación') NOT NULL,

);
~~~

- **Tabla préstamo:**
~~~
CREATE TABLE Prestamos (

  ID_Prestamo INT AUTO_INCREMENT PRIMARY KEY,

  ID_Estudiante INT NOT NULL,

  ID_Equipo INT NOT NULL,

  Hora_Prestamo TIMESTAMP NOT NULL,

  Hora_Devolucion DATETIME,

  Comentarios VARCHAR(255),

  FOREIGN KEY (ID_Estudiante) REFERENCES Estudiantes (ID_Estudiante),

  FOREIGN KEY (ID_Equipo) REFERENCES Equipos (ID_Equipo)

);
~~~