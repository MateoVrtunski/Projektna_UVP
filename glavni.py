import re

with open('stran.html') as f:
    html = f.read()
    


civilizacije = ['huns', "celts","goths","incas","khmer","malay","poles","slavs","turks","aztecs","cumans","franks","mayans","romans","tatars","berbers","britons","burmese",
                "chinese","koreans","magyars","malians","mongols","spanish","teutons","vikings","bengalis","gurjaras","italians","japanese","persians","saracens","bohemians",
                "sicilians","bulgarians","byzantines","dravidians","ethiopians","portuguese","vietnamese","burgundians","hindustanis","lithuanians"]
def izlusci_podatke(stran):
    podatki = []
    for i in range(len(civilizacije)- 1):
        vzorec = r"Aw." + f'{civilizacije[i]}' + r"=\{.*\};Aw." + f'{civilizacije[i+1]}'
        podatki.append(re.findall(vzorec,stran))
    vzorec2 = r"Aw.lithuanians=\{.*\};RF.arena"
    podatki.append(re.findall(vzorec2,stran))
    return podatki 


test = izlusci_podatke(html)
print(test)
