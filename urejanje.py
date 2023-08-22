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

#for i in range(42):
    #with open(f'stran{i}.html') as f:
        #koda = f.read()
        #iskanje = r""

with open('stran0.html') as f:
    huni = f.read()
huni_zmage = []
vzorec2 = r"\d+\.\d{2}%" 
huni_zmage.append(re.findall(vzorec2,huni))



print(huni_zmage)
