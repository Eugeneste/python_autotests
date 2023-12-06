import requests
import pytest

def test_status_code():
    response = requests.get(url='https://api.pokemonbattle.me:9104/trainers?page=10')
    assert response.status_code == 200

def test_name_tainer():
    response = requests.get(url='https://api.pokemonbattle.me:9104/trainers?trainer_id=3777')
    r = response.json()
    assert r['trainer_name'] == 'SJ'