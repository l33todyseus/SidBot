import os
import requests
import json

def get_price(coin):
  if not coin:
    return 1
  

  url = 'https://api.coinbase.com/v2/prices/'+coin+'-USD/spot'
  headers = {'Authorization' : os.environ['Authorization']}

  response = requests.get(url, headers=headers)
  json_data = json.loads(response.text)
  precio = json_data['data']['amount']

  return precio
