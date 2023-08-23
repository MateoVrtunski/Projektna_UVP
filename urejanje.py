import re

with open('stran.html') as f:
    html = f.read()

civilizacije = []
vzorec1 = r";Ay\.\w+=" 
civilizacije.append(re.findall(vzorec1,html))
civilizacije = civilizacije[0]

for i in range(len(civilizacije)):
    civilizacije[i] = civilizacije[i].replace(';Ay.','')
    civilizacije[i] = civilizacije[i].replace('=','')


def izlusci_podatke(stran):
    podatki = []
    for i in range(len(civilizacije)- 1):
        vzorec = r"Ay." + f'{civilizacije[i]}' + r"=\{.*\};Ay." + f'{civilizacije[i+1]}'
        podatki.append(re.findall(vzorec,stran))
    vzorec2 = r"Ay.lithuanians=\{.*\};RK.arena"
    podatki.append(re.findall(vzorec2,stran))
    return podatki 

test1 = izlusci_podatke(html)

def slovar(seznam):
    urejeno1 = {}
    for i in range(len(civilizacije)):
        urejeno1[civilizacije[i]] = seznam[i]
    return urejeno1

test2 = slovar(test1)


glavni_seznam = []
for i in range(len(civilizacije)):
    with open(f'stran{i}.html') as f:
        civ = f.read()
    seznam = []
    vzorec_procentov = r"\d+\.\d{2}%" 
    seznam.append(re.findall(vzorec_procentov,civ))
    seznam = seznam[0]

    igre = []
    vzorec_iger = r"<p class=\"text-sm\">\d+,\d{3} picks"
    igre.append(re.findall(vzorec_iger,civ))
    igre = igre[0]
    igre[0] = igre[0].replace('<p class="text-sm">','')
    igre[0] = igre[0].replace(' picks','')


    baza = {}
    baza['civilizacija'] = f'{civilizacije[i]}'
    baza['zmagovalna stopnja'] = seznam[0]
    baza['igralna stopnja'] = seznam[3]
    baza['stevilo iger'] = igre[0]
    glavni_seznam.append(baza)

 



print(glavni_seznam)
