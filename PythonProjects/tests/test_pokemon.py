import requests
import pytest

def test_status_code():
    response = requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200

def test_body_part():
    response = requests.get('https://pokemonbattle.me:5000/trainers', params = {'trainer_id' : '1590'})
    assert response.json()['trainer_name'] == 'Alexandra'

@pytest.mark.parametrize('key, value', [('trainer_name', 'Alexandra'),('city', 'Moscow')])

def test_parameters_body(key, value):
    response = requests.get('https://pokemonbattle.me:5000/trainers', params = {'trainer_id' : '1590'})
    assert response.json()[key] == value