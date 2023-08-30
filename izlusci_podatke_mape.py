import re

# tu bomo izluščili vse podatke iz strani ene mape

def izlusci_podatke_map(mapa):
    with open(f"htmlji/{mapa}.html") as f:
            podatki = f.read()

    # poiščemo vse procente

    procenti = []
    vzorec_procentov = r"\d+\.\d{2}%" 
    procenti.append(re.findall(vzorec_procentov,podatki))
    procenti = procenti[0]
    for j in range(len(procenti)):
        procenti[j] = procenti[j].replace('%','')
        
    procenti = procenti[3:]

    # poiščemo civilizacije v tistem vrstne redu kot je na strani

    pojavitve = []
    vzorec_nn = r"/assets/civ_crests/\w+\.webp" 
    pojavitve.append(re.findall(vzorec_nn,podatki))
    pojavitve = pojavitve[0]
    
    for i in range(len(pojavitve)):
        pojavitve[i] = pojavitve[i].replace('/assets/civ_crests/','')
        pojavitve[i] = pojavitve[i].replace('.webp','')

    # naredimo slovar, kjer bomo shranili vse podatke

    konec = []
    for i in range(len(pojavitve)):
        baza = {}
        baza['civilizacija'] = f'{pojavitve[i]}'
        baza['igralna stopnja'] = procenti[3 * i]
        baza['zmagovalna stopnja'] = procenti[(3 * i) + 2]
        konec.append(baza)
    
    return konec

# vrne nam slovar s seznami za vsako kategorijo




