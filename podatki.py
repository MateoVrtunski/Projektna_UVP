import requests

stran = requests.get("https://aoestats.io/civs/")

with open("stran.html", "w", encoding = 'utf-8') as dat:
    dat.write(stran.text)

