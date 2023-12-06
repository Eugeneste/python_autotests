import requests


def create_pokemons():
      response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons', 
              json={
                    "name": "generate",
                    "photo": "generate"
                    },
                    headers={'trainer_token': '65b2e30db07c6e8df73d582661751b9a', 'Content-Type': 'application/json'})

      print(f'Code: {response.status_code} json: {response.json()}')
      r = response.json()
      res = response.status_code

      response = requests.patch(url='https://api.pokemonbattle.me:9104/pokemons', 
                              json={
                                    "pokemon_id": r['id'],
                                    "name": "generate"
                              },
                              headers={'trainer_token': '65b2e30db07c6e8df73d582661751b9a', 'Content-Type': 'application/json'})

      print(f'Code: {response.status_code} json: {response.json()}')

      response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball', 
                              json={
                                    "pokemon_id": r['id'],
                              },
                              headers={'trainer_token': '65b2e30db07c6e8df73d582661751b9a', 'Content-Type': 'application/json'})

      print(f'Code: {response.status_code} json: {response.json()}')






# Создание покемона
response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons', 
              json={
                    "name": "generate",
                    "photo": "generate"
                    },
                    headers={'trainer_token': '65b2e30db07c6e8df73d582661751b9a', 'Content-Type': 'application/json'})

print(f'Code: {response.status_code} json: {response.json()}')
r = response.json()
res = response.status_code


if res == 400: #Если покоменов 5
            
            # Cписок покемонов

            response = requests.get(url='https://api.pokemonbattle.me:9104/pokemons?trainer_id=3777', 
                         
                                headers={'trainer_token': '65b2e30db07c6e8df73d582661751b9a', 'Content-Type': 'application/json'})
            r_list = response.json()

            print(f'Code: {response.status_code}')

            # Убить покемона

            response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons/knockout', 
                          json={
                                "pokemon_id": r_list[0]['id']
                                },
                                headers={'trainer_token': '65b2e30db07c6e8df73d582661751b9a', 'Content-Type': 'application/json'})

            print(f'Code: {response.status_code} json: {response.json()}')

            # Добавить функцию
            create_pokemons()



# Смена имени покемона
else:
      response = requests.patch(url='https://api.pokemonbattle.me:9104/pokemons', 
                              json={
                                    "pokemon_id": r['id'],
                                    "name": "generate"
                              },
                              headers={'trainer_token': '65b2e30db07c6e8df73d582661751b9a', 'Content-Type': 'application/json'})

      print(f'Code: {response.status_code} json: {response.json()}')

# Поймать покемона в покебол
      response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball', 
                              json={
                                    "pokemon_id": r['id'],
                              },
                              headers={'trainer_token': '65b2e30db07c6e8df73d582661751b9a', 'Content-Type': 'application/json'})

      print(f'Code: {response.status_code} json: {response.json()}')