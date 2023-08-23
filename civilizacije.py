import requests
import re

stran = requests.get("https://aoestats.io/civs/")

with open("stran.html", "w", encoding = 'utf-8') as dat:
    dat.write(stran.text)

def zajem_civilizacij(html):
    with open(html) as f:
        podatki = f.read()

    civilizacije = []
    vzorec1 = r";Au\.\w+=" 
    civilizacije.append(re.findall(vzorec1,podatki))
    civilizacije = civilizacije[0]

    for i in range(len(civilizacije)):
        civilizacije[i] = civilizacije[i].replace(';Au.','')
        civilizacije[i] = civilizacije[i].replace('=','')

    return civilizacije


civilizacije = zajem_civilizacij("stran.html")

#for i in range(len(civilizacije)):
    #stran = requests.get(f"https://aoestats.io/civs/{civilizacije[i]}/")
    #with open(f"stran{i}.html", "w",encoding = 'utf-8') as dat:
        #dat.write(stran.text)


print(civilizacije)
