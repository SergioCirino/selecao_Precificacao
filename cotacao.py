import json
import requests

def get_cotacao():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

    response = requests.get(url)
    try:
        data = json.loads(response.text)
        cotacao = data['USDBRL']['bid']
        return f'R$ {(f'{float(cotacao):.2f}').replace('.', ',')}'
    except:
         return f"Erro ao obter cotação {response.status_code}"

print(get_cotacao())