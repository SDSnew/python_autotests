import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "1e177347991a0f7f82867159a1e56bd0"
HEADER = {"Content-Type": "application/json", "trainer_token": TOKEN}
TRAINER_ID = "37588"
json_create_pokemon = {
    "name": "Данил",
    "photo_id": 12
}
json_change_name = {
    "pokemon_id": "372802",
    "name": "Данилка чемпион",
    "photo_id": 2
}

json_add_to_pokebol = {
    "pokemon_id": "372802"
}

"""response = requests.post(url= f'{URL}/pokemons', headers= HEADER, json= json_create_pokemon)
print(response.json())

response = requests.put(url= f'{URL}/pokemons', headers= HEADER, json= json_change_name)
print(response.json())

response = requests.post(url= f'{URL}/trainers/add_pokeball', headers= HEADER, json= json_add_to_pokebol)
print(response.json())"""

response = requests.get(url=f"{URL}/trainers", headers=HEADER, params={"trainer_id": TRAINER_ID})
print(response.json())