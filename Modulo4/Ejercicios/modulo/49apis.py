
import requests
url="https://pokeapi.co/api/v2/pokemon/ditto"
data=requests.get(url)
datajson=data.json()
print(datajson['abilities'])
