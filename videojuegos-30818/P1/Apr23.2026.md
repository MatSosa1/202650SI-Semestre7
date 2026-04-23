# Creación de Videojuegos con un Game Engine

Un Game Engine o motor de juego es un conjunto de herramientas y bibliotecas que facilita la creación de videojuegos al encargarse de muchos apesctos técnicos: gráficos, físicas, sonido, animaciones, redes, inteligencia artificial, etc.

El uso de un motor permite a los desarrolladores enfocarse más en el diseño del juego y menos en programar desde cero aspectos de bajo nivel como la detección de colisiones o el renderizado de imágenes.

## Definición

El programa principal de un videojuego es el ciclo de vida que controla cómo se inicializa, actualiza y termina el juego. Es la base del software, la que coordina todos los componentes y lógica del juego.

Se conoce como ***Game Loop***.

## Funcionalidad

- Inicialización: Carga de recursos.
- Bucle principal
    - Captura de entradas: Leer teclado, ratón, controlador.
    - Actualización de la Lógica: Movimiento de personajes, IA, físicas.
    - Renderizado: Dibujar en pantalla la escena actualizada.
- Finalización: Liberar memoria, guardar datos, cerrar recursos.

Es el núcleo de control que:

- Inicia el juego
- Coordina todos los sistemas
- Ejecuta el ciclo continuo (game loop)

## Gestión de Estados (State Manager)

El programa principal controla en qué parte del juego estás:

1. Menú
2. Juego
3. Pausa
4. Game Over

El programa principal NO hace el juego, coordina todos los sistemas para que el mismo funcione en tiempo real.

# El Motor Lógico de un Videojuego

## Definición

El motor lógico es la parte del programa que gestiona las reglas del juego, reacciones a las acciones del juegador y cimoortamientos de los elementos del mundo del juego.

El motor lógico es el sistema que transforma entradas (input, IA, red) en cambios de estado del juego siguiendo reglas definidas.

## Responsabilidades Principales

- Manejar el comportamiento de los personajes
- Gestionar las condiciones de victoria/derrota
- Administrar colisiones y consecuencias
- Controlar el flujo de niveles, escenas o misiones

## Ejemplos de lógica de un juego

- Si el jugador recoge 100 monedas -> Gana una vida extra
- Si la vida del enemigo llega a 0 -> Se elimina del juego
