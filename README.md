# Benjamin_Lopez_proyectoM4_Pokedex2.py

# Pokédex en Python

Esta Pokédex en Python es una aplicación simple que te permite buscar información sobre los Pokémon utilizando la API de Pokémon. Puedes ingresar el nombre o el número de la Pokédex Nacional de un Pokémon, y la aplicación mostrará información detallada y una imagen del Pokémon.

## Requisitos

Para ejecutar este proyecto, necesitas tener instaladas las siguientes bibliotecas de Python:

- `requests`: Utilizada para hacer solicitudes HTTP a la API de Pokémon.
- `PIL` (Python Imaging Library): Utilizada para trabajar con imágenes, en este caso, para mostrar las imágenes de los Pokémon.
- `json`: Utilizada para manejar datos JSON.
- `os`: Utilizada para trabajar con el sistema de archivos y crear un directorio para guardar datos JSON.
- `io`: Utilizada para trabajar con flujos de bytes y abrir imágenes desde una respuesta HTTP.

Puedes instalar estas bibliotecas utilizando el siguiente comando:

```
pip install requests pillow
```

## Cómo usar

1. Ejecuta el programa `pokedex.py` en tu terminal.

```
python pokedex.py
```

2. Verás un mensaje de bienvenida que te pedirá que ingreses el nombre o el número de la Pokédex Nacional de un Pokémon.

3. Ingresa el nombre o número del Pokémon que deseas buscar.

4. La aplicación buscará información sobre el Pokémon y mostrará su nombre, peso, altura, movimientos, habilidades y tipos.

5. También se guardará una imagen del Pokémon en un archivo PNG en el directorio `pokedex`.

6. Se creara un Archivo .json con las caracteristicas buscadas del pokemon.

7. Se abrirá la imagen en el visor de imágenes predeterminado de tu sistema operativo.

## Aprendizaje

Este proyecto fue una oportunidad para aprender y aplicar los siguientes conceptos y técnicas:

- Uso de la biblioteca `requests` para realizar solicitudes a una API web.
- Tratamiento de datos JSON para obtener información detallada de los Pokémon.
- Trabajo con imágenes utilizando la biblioteca `PIL` para mostrar imágenes de los Pokémon.
- Manipulación de archivos y directorios en Python.
- Manejo de errores y validación de entrada del usuario.

¡Diviértete explorando el mundo de los Pokémon con tu propia Pokédex en Python!
