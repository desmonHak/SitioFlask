# SitioFlask

----

Este es un sitio hecho en Flask basico el cual he hecho como trabajo para final de trimeste. Usa Sqlite 3 para guardar los usuarios y password's. Permite crear templates html desde la pagina para cada usuario, crear usuarios nuevos con password y la visualizacion de cada sitio web hecho por usuarios.

----

# Instalacion

```batch
pip install -r requirements.txt
```

----

# Ejecucion

Para ejecutar el servicio Http basta con hacer:
```batch
python index.py 
```
Acontinuacion vera que el servicio inicia en `http://127.0.0.1:5000`:
```batch
 * Serving Flask app 'index'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 378-660-635
```

Usted puede ver los datos que hay en la base de datos `data_base.db` usando `python print_db.py`:
```batch
❯ python print_db.py
+--------------------+--------------------+------------------------------+
|        user        |      password      |        fecha_creacion        |
+--------------------+--------------------+------------------------------+
|       Desmon       |        1234        |  2023-02-16 22:01:03.769712  |
+--------------------+--------------------+------------------------------+
```

----
Una vez crea un usuario, se crea una carpeta nueva con el nombre del usuario en el directorio `templates`. En este nuevo directorio se almacena un archivo `.html` con el nombre de usuario que puede visualizarse llendo a la ruta `http://127.0.0.1:5000/home/Desmon`. Donde en lugar de Desmon pone el nombre de usuario que esta registrado en la base de datos. La plantillas creada para los usuarios es el codigo que se situa en `default.html`. En el caso de que se agrege un usuario nuevo, si su carpeta de trabajo no existe, se crea.