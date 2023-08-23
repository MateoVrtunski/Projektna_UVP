import requests
import re

stran = requests.get("https://aoestats.io/civs/")

with open("stran.html", "w", encoding = 'utf-8') as dat:
    dat.write(stran.text)

with open('stran.html') as f:
    html = f.read()

civilizacije = []
vzorec1 = r";Ay\.\w+=" 
civilizacije.append(re.findall(vzorec1,html))
civilizacije = civilizacije[0]

for i in range(len(civilizacije)):
    civilizacije[i] = civilizacije[i].replace(';Ay.','')
    civilizacije[i] = civilizacije[i].replace('=','')



for i in range(len(civilizacije)):
    stran = requests.get(f"https://aoestats.io/civs/{civilizacije[i]}/")
    with open(f"stran{i}.html", "w",encoding = 'utf-8') as dat:
        dat.write(stran.text)



