import requests
r = requests.get('https://api.nasa.gov/planetary/apod?api_key=Zex7CBAHQmbVfomUeIOyZXt9d8JccD4R50fNNhal')
r1 = r.json()
print (r1)

