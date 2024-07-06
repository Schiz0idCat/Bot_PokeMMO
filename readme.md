bot busca automatizar ciertas tareas dentro de PokeMMO.

## Orden de las carpetas
### API
La carpeta *api* contiene archivos que sirven de herramienta para analizar las cosas que pasan en el juego y para interactuar con este. Tales son: *images.py* e *interaction.py*.

#### images.py
Concentra el procesamiento de imágenes para reconocer lo que pasa dentro del juego.
Contiene las coordenadas de la burbuja de dialogo y de la interfaz de pelea, que nos será útil para analizar los mensajes y si estamos o no en batalla.
Además, tiene una función para procesar imágenes y reconocer contornos, lo que le facilita al computador reconocer qué sucede por pantalla.
En un futuro la idea es ir llenando este archivo de más funciones que nos ayuden a ver qué está pasando en el mundo.

#### interaction.py
Concentra todas las funciones para interactuar con el juego.
Contiene un diccionario que concentra los botones que tenemos configurados en el juego, para globalizar su uso.
Una función que randomiza el tiempo de espera (lo usaremos para que el tiempo entre clicks no sea el mismo siempre).
Una función que nos facilita cambiar ventanas, una que nos ayuda a apretar botones y otra que hace click en la pantalla.
Luego tiene la función que nos mueve al personaje, con los parámetros de 3 tipos de movimiento que hay en el juego.
Finalmente una función para pescar, que se llama así misma iterativamente hasta pescar algo.
En un futuro la idea es ir llenando este archivo de más funciones que nos ayuden a interactuar con el mundo.

### BOT
En este archivo se irán almacenando los distintos bots para el juego.

#### MagikarpSafariZone.py
Este bot automatiza la captura de magikarp en la zona safari de Pokemon Rojo Fuego.

### PHOTOS
En esta carpeta se almacenan fotos de control, que han sido útiles para testear bots, además, las fotos que que vaya sacando el bot se irán almacenando acá.

### TEST
Este archivo contiene funciones que viene bien testear en escenarios controlados para ver cómo se comportan.

## main.py
Acá se irán recopilando todos los bots, para tenerlos a fácil acceso. Además se configurarán para poder usar en bucle.