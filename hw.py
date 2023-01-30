import requests
import operator


url = "https://akabab.github.io/superhero-api/api/all.json"
resp = requests.get(url)
heroes_list = ['Hulk', 'Captain America', 'Thanos']
list_of_dictionaries = resp.json()


for value in list_of_dictionaries:
    result = value['powerstats']['intelligence']
    if value['name'] in heroes_list:
        dictionary = {
            'name':value['name'],
            'intelligence':result
        }
