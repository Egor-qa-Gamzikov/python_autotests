import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '58a56f8ed7845ae8f401263cf1311368'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}

'''response = url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response.text)'''


body_put = {
    "pokemon_id": "45743",
    "name": "Здарова",
    "photo_id": 3
}

'''response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put)
print(response.json)'''


body_pokeball = {
    "pokemon_id": "45743"
}

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response.json)