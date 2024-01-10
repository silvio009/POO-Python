import requests
import json

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    dados_rest = {}
    print(dados_json)

    for item in dados_json:
        nome_do_rest = item['Company']
        if nome_do_rest not in dados_rest:
            dados_rest[nome_do_rest] = []

        dados_rest[nome_do_rest].append({
            "item" : item ['Item'],
            "price": item['price'],
            "description": item['description']
        })
else:
    print(f'Erro localizado:{response.status_code}')

for nome_do_rest, dados in dados_rest.items():
    nome_do_arq = f'{nome_do_rest}.json'
    with open(nome_do_arq,'w') as arquivo_restaurante:
        json.dump(dados,arquivo_restaurante,indent=4)
