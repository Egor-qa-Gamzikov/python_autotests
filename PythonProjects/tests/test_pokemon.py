import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '58a56f8ed7845ae8f401263cf1311368'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '4406'



def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200