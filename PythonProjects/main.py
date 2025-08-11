import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "Trainer_token"
HEADER = {"Content-Type": "application/json", "trainer_token": TOKEN}
TRAINER_ID = "37588"
json_create_pokemon = {"name": "Данил", "photo_id": 12}


response = requests.post(
    url=f"{URL}/pokemons", headers=HEADER, json=json_create_pokemon
)
print(response.json())

pokemon_id = response.json()["id"]

json_change_name = {"pokemon_id": pokemon_id, "name": "Пикачу", "photo_id": 2}
json_add_to_pokebol = {"pokemon_id": pokemon_id}


response = requests.put(url=f"{URL}/pokemons", headers=HEADER, json=json_change_name)
print(response.json())


response = requests.post(
    url=f"{URL}/trainers/add_pokeball", headers=HEADER, json=json_add_to_pokebol
)
print(response.json())

response = requests.get(
    url=f"{URL}/trainers", headers=HEADER, params={"trainer_id": TRAINER_ID}
)
print(response.json())
