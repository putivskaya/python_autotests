import requests
import json

token = '0299ed9286b88fc1d0841903a235c39f'

response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "name": "Покемонище",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})

print(response.text)

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": 2558,
    "name": "Sharky",
    "photo": "https://upload.wikimedia.org/wikipedia/ru/4/49/%D0%9F%D0%BE%D0%BA%D0%B5%D0%BC%D0%BE%D0%BD_%D0%98%D0%B2%D0%B8.png"
})

print(response_put.text)

response_post = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers={'trainer_token' : token}, json={
    "pokemon_id": 2558
})

print(response_post.text)

'''response = requests.get('https://pokemonbattle.me:5000/trainers')

response_pretty = json.dumps(response.json(), indent=4, ensure_ascii=False)

print(response.status_code, response_pretty)

if response.status_code == 200:
    print('ok')
else:
    print('not ok')

response_getout = requests.put('https://pokemonbattle.me:5000/trainers/delete_pokeball', headers={'trainer_token' : token}, json={
    "pokemon_id": 2558
})

print(response_getout.text)'''