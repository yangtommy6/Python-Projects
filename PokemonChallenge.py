import requests
import json

url = 'https://pokeapi.co/api/v2/pokemon/'
type_url = 'https://pokeapi.co/api/v2/type/'
pokename_url = "https://pokeapi.co/api/v2/type/pokemon"

api_call_data = requests.get(type_url).text
api_call_data = json.loads(api_call_data)

print("Below are all of the Pokemon types:\n")
for print_type in api_call_data['results']:
    print(print_type['name'])
print('select a type: ')
user_input = input()
use_this_url = type_url + user_input

api_call_pokemon = requests.get(use_this_url).text
api_call_pokemon = json.loads(api_call_pokemon)
j = 0
for print_pokemon in api_call_pokemon['pokemon']:
    print(api_call_pokemon['pokemon'][j]['pokemon']['name'])
    j = j + 1

print("These are the Pokemons from this type. Please input the Pokemon you want to learn about:\n")
pokemon_name_input = input()


info_url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name_input
api_call_data_info = requests.get(info_url).text
api_call_data_info = json.loads(api_call_data_info)
i = 0
print("\nPokemon ID: ")
print(api_call_data_info['id'])
print("\nPokemon type(s): ")
for types in api_call_data_info['types']:
    print(api_call_data_info['types'][i]['type']['name'])
    i += 1
print("\nHeight: ")
print(api_call_data_info['height'])
print("\nWeight: ")
print(api_call_data_info['weight'])

print("\nAppeared games: ")
temp = 0
for gens in api_call_data_info['game_indices']:
    print(api_call_data_info['game_indices'][temp]['version']['name'])
    temp = temp + 1


#BROCK IS THE BESTTTTTTTTTTTTTTTTTTTTTTTTT


# ---------------Below are some codes that I tried, just for rememberance =)--------------------------

# print(api_call_data)
# api_call_data = json.loads(api_call_data)
# for inputdata in api_call_data['']


# for offset in range(0, 1000, 1000):
#     params['offset'] = offset  # add new value to dict with `limit`
#     response = requests.get(url, params=params)

#     if response.status_code != 200: 
#         print(response.text)
#     else:
#         data = response.json()
#         print(data)
        #pp.pprint(data)
        # for item in data['results']:
        #     print(item['name'])

# params = {'limit': 100}

# api_call_data_name = requests.get(use_this_url).text
# api_call_data_name = json.loads(api_call_data_name)
# tempNum = 0
# # for pokedata in api_call_data_name['results']:
# for pokedata in api_call_data_name:
#     for print_all_pokemon_in_this_type in api_call_data_name['pokemon'][tempNum]['pokemon']['name']:
#     print(api_call_data_name['pokemon'][tempNum]['pokemon']['name'])
#     tempNum += 1


    # num = 1
    
    # url += str(num)
    # api_call_data_pokemon = requests.get(url).text
    # api_call_data_pokemon = json.loads(api_call_data_pokemon)
    # name = api_call_data_pokemon['species']['name']
    # matchExam = False
    # tempNum = 0
    # for check in api_call_data_pokemon['types']:
    #     if api_call_data_pokemon['types'][tempNum]['type']['name'] == user_input:
    #         matchExam = True
    #     tempNum += 1
    
    # if matchExam:
    #     namedata.append(name)
    
# print(namedata)
