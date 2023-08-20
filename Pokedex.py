# Importamos las bibliotecas necesarias
import os
import requests
import json
from PIL import Image
from io import BytesIO

# Mensaje de bienvenida para el usuario
print("""
    Bienvenido entrenador, esta es una Pokédex, la cual te ayudará a conocer más acerca de los Pokémon.
    Para iniciar, ingresa un Pokémon por su nombre o usando su número de la Pokédex Nacional.
""")

# Función para obtener datos de un Pokémon
def get_pokemon_data(pokemon_name):
    # URL base para la API de Pokémon
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    # Combinamos la URL base con el nombre del Pokémon en minúsculas
    url = f"{base_url}{pokemon_name.lower()}"
    
    # Realizamos una solicitud GET a la API
    response = requests.get(url)
    
    # Verificamos el código de estado de la respuesta
    if response.status_code == 404:
        return None  # Pokémon no encontrado
    elif response.status_code == 200:
        # Convertimos la respuesta JSON en un diccionario de datos
        pokemon_data = response.json()
        return pokemon_data

# Función para mostrar información de un Pokémon
def show_pokemon_info(pokemon_data):
    # Extraemos datos relevantes del diccionario de datos del Pokémon
    name = pokemon_data['name'].capitalize()
    image_url = pokemon_data['sprites']['front_default']
    weight = pokemon_data['weight']
    height = pokemon_data['height']
    moves = [move['move']['name'] for move in pokemon_data['moves']]
    abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
    types = [poke_type['type']['name'] for poke_type in pokemon_data['types']]
    
    # Mostramos la información por pantalla
    print(f"Nombre: {name}")
    print(f"Peso: {weight}")
    print(f"Altura: {height}")
    print("Movimientos:", ', '.join(moves))
    print("Habilidades:", ', '.join(abilities))
    print("Tipos:", ', '.join(types))
    
    # Descargamos y mostramos la imagen del Pokémon
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img.save(f"{name}.png")  # Guardamos la imagen en un archivo
    os.system(f"start {name}.png")  # Abre la imagen con el visor de imágenes predeterminado en Windows.

# Función para guardar datos del Pokémon en un archivo JSON
def save_pokemon_to_json(pokemon_data):
    name = pokemon_data['name']
    image_url = pokemon_data['sprites']['front_default']
    data_to_save = {
        'name': name,
        'image_url': image_url,
        'data': pokemon_data
    }
    
    # Creamos un directorio "pokedex" si no existe
    if not os.path.exists("pokedex"):
        os.mkdir("pokedex")
    
    # Guardamos los datos en un archivo JSON
    with open(f"pokedex/{name}.json", "w") as file:
        json.dump(data_to_save, file, indent=4)

# Función principal
def main():
    # Solicitamos al usuario ingresar el nombre o número del Pokémon mediante un while que no dejara el espacio en blanco
    # Tampoco permite que pokemon inexistentes
    while True:
        try:
            pokemon_name = input("Ingresa un Pokémon por su nombre o por su número de la Pokédex Nacional: ")
            while not pokemon_name:
                print("\t ¡Error!: Debe ingresar al menos un pokemon")
                pokemon_name = input("Ingresa un Pokémon por su nombre o por su número de la Pokédex Nacional: ")
            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
            response = requests.get (url)
            if response.status_code != 200:
                print(f"El Pokémon {pokemon_name} no fue encontrado, intentalo de nuevo")
            else: break
        except: pass
    pokemon_data = get_pokemon_data(pokemon_name)
    
    
    # Si se encontraron datos del Pokémon, mostramos la información y la guardamos en JSON
    if pokemon_data:
        show_pokemon_info(pokemon_data)
        save_pokemon_to_json(pokemon_data)
    else:
        print(f"Error: Pokémon '{pokemon_name}' no encontrado.")

# Punto de entrada principal del programa
if __name__ == "__main__":
    main()
