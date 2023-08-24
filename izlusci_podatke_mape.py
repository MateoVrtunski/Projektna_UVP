import re


def izlusci_podatke_map(mapa):
    with open(f"{mapa}.html") as f:
            podatki = f.read()

    procenti = []
    vzorec_procentov = r"\d+\.\d{2}%" 
    procenti.append(re.findall(vzorec_procentov,podatki))
    procenti = procenti[0]

    igranje = procenti[0]

    procenti = procenti[3:]

    pojavitve = []
    vzorec_nn = r"/assets/civ_crests/\w+\.webp" 
    pojavitve.append(re.findall(vzorec_nn,podatki))
    pojavitve = pojavitve[0]

    for i in range(len(pojavitve)):
        pojavitve[i] = pojavitve[i].replace('/assets/civ_crests/','')
        pojavitve[i] = pojavitve[i].replace('.webp','')

    baza = {}

    baza[f'igralna stopnja celotne mape {mapa}'] = igranje

    baza['igralna stopnja'] = []
    igralna_stopnja = {}
    baza['igralna stopnja'].append(igralna_stopnja)

    for i in range(len(pojavitve)):
        igralna_stopnja[f'{pojavitve[i]}'] = procenti[3 * i]

    baza['zmagovalna stopnja'] = []
    zmagovalna_stopnja = {}
    baza['zmagovalna stopnja'].append(zmagovalna_stopnja)

    for i in range(len(pojavitve)):
        zmagovalna_stopnja[f'{pojavitve[i]}'] = procenti[(3 * i) + 2]

    konec = []
    konec.append(baza)

    return konec

    
high = izlusci_podatke_map('highland')
print(high)



