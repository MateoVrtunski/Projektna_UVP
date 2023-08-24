import re


def izlusci_podatke_map(mapa):
    with open(f"{mapa}.html") as f:
            podatki = f.read()

    procenti = []
    vzorec_procentov = r"\d+\.\d{2}%" 
    procenti.append(re.findall(vzorec_procentov,podatki))
    procenti = procenti[0]

    

    procenti = procenti[3:]

    pojavitve = []
    vzorec_nn = r"/assets/civ_crests/\w+\.webp" 
    pojavitve.append(re.findall(vzorec_nn,podatki))
    pojavitve = pojavitve[0]
    
    for i in range(len(pojavitve)):
        pojavitve[i] = pojavitve[i].replace('/assets/civ_crests/','')
        pojavitve[i] = pojavitve[i].replace('.webp','')

    konec = []
    for i in range(len(pojavitve)):
        baza = {}
        baza['civilizacija'] = f'{pojavitve[i]}'
        baza['igralna stopnja'] = procenti[3 * i]
        baza['zmagovalna stopnja'] = procenti[(3 * i) + 2]
        konec.append(baza)
    
    return konec

print(izlusci_podatke_map('megarandom'))




