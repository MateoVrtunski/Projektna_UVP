import requests
import re

# naložimo glavno stran

stran = requests.get("https://aoestats.io/civs/")

with open("htmlji/stran.html", "w", encoding = 'utf-8') as dat:
    dat.write(stran.text)

# izluščimo vse civilizacije v seznam

def zajem_civilizacij(html):
    with open(html) as f:
        podatki = f.read()

    civ = []
    vzorec = r"/assets/civ_crests/\w+\.webp" 
    civ.append(re.findall(vzorec,podatki))
    civ = civ[0]
   
    for i in range(len(civ)):
        civ[i] = civ[i].replace('/assets/civ_crests/','')
        civ[i] = civ[i].replace('.webp','')

    return civ


civilizacija = zajem_civilizacij("stran.html")

# s pomočjo seznama prenesemo stran vsake civilizacije

for i in range(len(civilizacija)):
    stran = requests.get(f"https://aoestats.io/civs/{civilizacija[i]}/")
    with open(f"htmlji/{civilizacija[i]}.html", "w",encoding = 'utf-8') as dat:
        dat.write(stran.text)

# enako naredimo za mape

def mapa(html):
    with open(html) as f:
        neka_civilizacija = f.read()
    mape = []
    vzorec_mape = r"/assets/maps/\w+\.webp" 
    mape.append(re.findall(vzorec_mape,neka_civilizacija))
    mape = mape[0]
    return mape

mape = mapa('htmlji/huns.html')

for i in range(len(mape)):
    mape[i] = mape[i].replace('/assets/maps/','')
    mape[i] = mape[i].replace('.webp','')

for i in range(len(mape)):
    stran = requests.get(f"https://aoestats.io/maps/{mape[i]}/")
    with open(f"htmlji/{mape[i]}.html", "w",encoding = 'utf-8') as dat:
        dat.write(stran.text)

