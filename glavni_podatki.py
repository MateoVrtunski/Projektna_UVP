import re
import civilizacije

civilizacija = civilizacije.civilizacija

glavni_seznam = []
for i in range(len(civilizacija)):
    with open(f'htmlji/{civilizacija[i]}.html') as f:
        civ = f.read()
    seznam = []
    vzorec_procentov = r"\d+\.\d{2}%" 
    seznam.append(re.findall(vzorec_procentov,civ))
    seznam = seznam[0]
    for j in range(len(seznam)):
        seznam[j] = seznam[j].replace('%','')
    

    igre = []
    vzorec_iger = r"<p class=\"text-sm\">\d+,\d{3} picks"
    igre.append(re.findall(vzorec_iger,civ))
    igre = igre[0]

    igre[0] = igre[0].replace(' picks','')
    igre[0] = igre[0].replace('<p class="text-sm">','')
    igre[0] = igre[0].replace('"','')
    


    baza = {}
    baza['civilizacija'] = f'{civilizacija[i]}'
    baza['igralna stopnja'] = seznam[3]
    baza['zmagovalna stopnja'] = seznam[0]
    baza['stevilo iger'] = igre[0]
    glavni_seznam.append(baza)

print(glavni_seznam)



