import re
import civilizacije

civilizacija = civilizacije.zajem_civilizacij("stran.html")

glavni_seznam = []
for i in range(len(civilizacija)):
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

    igre[0] = igre[0].replace(' picks','')
    igre[0] = igre[0].replace('<p class="text-sm">','')


    baza = {}
    baza['civilizacija'] = f'{civilizacija[i]}'
    baza['zmagovalna stopnja'] = seznam[0]
    baza['igralna stopnja'] = seznam[3]
    baza['stevilo iger'] = igre[0]
    glavni_seznam.append(baza)

 
print(glavni_seznam)


