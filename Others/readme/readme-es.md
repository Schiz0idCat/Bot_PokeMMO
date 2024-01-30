Este es un bot que automatiza la captura de magikarps de la Zona Safari en PokeMMO.

## Configuraciones

### Configurar botones en game_interaction.py
En la linea 24 en el archivo *game_interaction.py* verás un diccionario *self.button* que almacena la configuración de los botones, ajustalo según tu comodidad:
```python
class Bot():
    def __init__(self):
        self.ss_path = "Main\\ss.png"

        # Set your own configurations here
        self.button = { 
            'A' : 'z',
            'B' : 'x',
            'Rod' : '4',
            'UP' : 'up',
            'DOWN' : 'down',
            'LEFT' : 'left',
            'RIGHT' : 'right'
        }

        # For magikarp bot
        self.safariballs = 30
        self.turn = False
```

### Configuraciones gráficas y del juego
Este es mi primer proyecto con manejo de imágenes así que el bot es sensible a lo que pasa en pantalla, por lo que te recomiendo las siguientes configuraciones para que el bot funcioné correctamente.

tienes que configurar el juego en las condiciones en las que el bot fue testeado:

1.- La resolución de tu monitor debe ser de 1920x1080.

2.- La resolución del juego debe ser de 1024x768 y estar en modo ventana.

3.- Los fps deben ser superiores a 30.

4.- El tema del juego tiene que ser el que viene por default.

5.- La velocidad del texto debe ser x4.

6.- Tamaño de la ventana de batalla en 100

### Funcionamiento del bot


1.- El bot tiene que ser ejecutado desde el archivo *bot.py* y de forma predeterminada captura solo 30 magikarps.

2.- Si quieres que el bot no esté en un loop infinito tienes que hacer que parta en el lago para que pesque.

![](..\Photos\lake.png)

Pero si quieres que el bot sí esté en un loop infinito tienes que hacer que parta a la entrada de la zona safari (antes de pagar por la entrada).

![](..\Photos\pay.png)

3.- De forma predeterminada el bot considera que el personaje se mueve caminando (así que asegúrate de que tu personaje no se mueva corriendo).

4.- Si configuras el bot para que actue en un loop infinito podría fallar al cabo de un tiempo por problemas con el lag del servidor.