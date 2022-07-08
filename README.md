# Practica de Desarrollo N°2
![Imgur](https://imgur.com/iHjjyWI)

## ¿Que es esto? ❓🤔
Acompañado de JuanmaKrum (Juan Martín Barreto Correa) y LechugaTactica (Thomas Kauffman) participamos en la Competencia de "Desarrollo de Sistemas" de las ONIET 2021. 
Este es un sistema que desarrollamos como práctica y el más completo que resultó. 
## Desarrollo ⚡
Este sistema se suplió de la API de igual nombre, fue creado utilizando Vanilla JS, Django, SQLite3 y Bulma.io (framework de CSS). 
Fué creado en un par de horas para simular la competencia de la ONIET, por lo que pedimos que no sea tan tomada en cuenta la desplolijidad.

## Como correr el sistema 🚀
Primero deben ser instalados los requerimientos:

```
$ pip install -r requirements.txt
```
Recomendamos utilizar un Entorno Virtual.

Posteriormente se posiciona el cmd en la carpeta ```pokeapi/``` y se escribe el comando para levantar el servidor Django:
```
$ python manage.py runserver
```
Una vez ejecutado el servidor se situa en http://localhost:8000 

## Y que hago con esto?
Esta app muestra pokémon de la primera entrega (Rojo - Azul - Amarillo). Puede mostrar uno random o uno a elección. En la tarjeta aparecerá una imagen del mismo, sus estadísticas y una descripción extraída de los juegos. 

Además tiene un sistema de Likes, por lo que si se crea un perfil podrá añadir y remover pokémons de su lista de favoritos y ver esta lista en su perfil, sirviendo también como acceso rapido a la información de estos.

![Imgur](https://imgur.com/UEZQjgf)