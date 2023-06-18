## Actualizacion por lotes mediante csv
En el presente proyecto se realiza la actualizacion por lotes mediante un archivo csv, mediante el  framework Django de python.

## Ejecutar el servicio
Paso 1.	Clonar el proyecto desde GitHub desde el bash de git con el siguiente comando:

git clone https://github.com/AndresCevallos7/actualizacion_datos_csv_django

Paso 2.	Abrimos VS Code, ejecutamos el terminal en la ruta ra�z del proyecto en ese caso actualizacion_datos_csv_django ejecutamos los siguientes comandos para crear y activar el entorno virtual e instalar todas las dependencias.

python -m venv venv : crear un entorno virtual con el nombre �venv�

.\venv\Scripts\activate : se active el ambiente virtual

pip install -r requirements.txt : se instalan todas las dependencias requeridas

Paso 3.	Levantar el servicio, cuando activamos el ambiente virtual �venv�utilizar el siguiente comando:
[python manage.py runserver]

Paso 4.	Vamos a la p�gina principal del servicio mostrada en HTML, ir a la direcci�n: localhost:8000, se mostrar� un men� con las siguientes opciones. 
En lista, se observar�n los registros que se tienen de la siguiente forma: 
En subir, se puede cargar el archivo csv, que debe contener los campos vistos anteriormente
En actualizar, se pueden actualizar los registros(actualizar o crear nuevos usuarios), y se envia un correo.

Paso 5. Al dar clic en subir se nos mostrar� los siguiente  , seleccionar el archivo y subir el mismo, nos llevar� a la p�gina inicial si el archivo se carg� correctamente.

Paso 6.	Dar clic en actualizar y nos arrojar� el mensaje �Realizado�, en este punto se habr� actualizado la tabla, enviado el correo para enviar el saludo (se mostrar� por consola) y se nos redirige al inicio.
 
Paso 7.	Al dar clic en Lista se nos mostrar� la lista actualizada.

## myapp 
Se trabaja con la aplicaci�n "myapp" donde se tienen los siguientes archivos.py

-urls.py: en esta capa se se realiza el direcionamiento de las paginas.
-models.py: En esta capa se inicializa la base de datos y es necesario realizar migraciones.
-urls.py #En esta capa se realiza las tareas de navegacion entre paginas, mediante la def "index" se nos muestra la p�gina inicial y se carga [index.html];mediante la "def" subir se carga el archivo csv la tabla de registros con el archivo [lista.html], cada vez que se sube un archivo cvs se elimina el anterior ; mediante la "def" subir se realiza la carga del archivo csv con la ayuda de [upload.html]; y medinate la def "import_csv" re realiza la actualizaci�n de los usuario, creacion de nuevos usuarios y control de cedula/RUC, envio de mensaje para nuevos usuarios.

## Datos relevantes
Para guardar el archivo csv se debe agregar las siguietnes l�nes al archivo "settings.py":

import os

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

El archivo se va a guardar en la biblioteca media.