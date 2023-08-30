import re

# tu bomo izluščili vse podatke iz strani ene civilizacije

def izlusci_vse_podatke(ime):
    with open(f'htmlji/{ime}.html') as f:
        html_civilizacija = f.read()
  
    # poiščemo vse procente

    procenti = []
    vzorec_procentov = r"\d+\.\d{2}%" 
    procenti.append(re.findall(vzorec_procentov,html_civilizacija))
    procenti = procenti[0]
    for j in range(len(procenti)):
        procenti[j] = procenti[j].replace('%','')
    procenti = procenti[4:]
    
    # poiščemo želene in neželen nasprotnike

    najboljsi_najslabsi = []
    vzorec_nn = r"/assets/civ_crests/\w+\.webp" 
    najboljsi_najslabsi.append(re.findall(vzorec_nn,html_civilizacija))
    najboljsi_najslabsi = najboljsi_najslabsi[0]
    najboljsi_najslabsi.remove(najboljsi_najslabsi[0])
    for i in range(len(najboljsi_najslabsi)):
        najboljsi_najslabsi[i] = najboljsi_najslabsi[i].replace('/assets/civ_crests/','')
        najboljsi_najslabsi[i] = najboljsi_najslabsi[i].replace('.webp','')

    # poiščemo otvoritve

    otvoritve = []
    vzorec_otvoritve = r"/assets/openings/\w+\.webp" 
    otvoritve.append(re.findall(vzorec_otvoritve,html_civilizacija))
    otvoritve = otvoritve[0]
    for i in range(len(otvoritve)):
        otvoritve[i] = otvoritve[i].replace('/assets/openings/','')
        otvoritve[i] = otvoritve[i].replace('.webp','')
        otvoritve[i] = otvoritve[i].replace('_',' ')

    # poiščemo vse mape

    mape = []
    vzorec_mape = r"/assets/maps/\w+\.webp" 
    mape.append(re.findall(vzorec_mape,html_civilizacija))
    mape = mape[0]
    for i in range(len(mape)):
        mape[i] = mape[i].replace('/assets/maps/','')
        mape[i] = mape[i].replace('.webp','')
    
    # naredimo slovar v katerega bomo vse podatke shranili po vrsti
    
    baza = {}


    baza['želeni nasprotniki'] = []
    

    for i in range(5):
        zeleni_nasprotniki = {}
        zeleni_nasprotniki['civilizacija'] = f'{najboljsi_najslabsi[i]}'
        zeleni_nasprotniki['zmagovalna stopnja'] = procenti[i]
        baza['želeni nasprotniki'].append(zeleni_nasprotniki)

    baza['neželeni nasprotniki'] = []
    

    for i in range(5,10):
        nezeleni_nasprotniki = {}
        nezeleni_nasprotniki['civilizacija'] = f'{najboljsi_najslabsi[i]}'
        nezeleni_nasprotniki['zmagovalna stopnja'] = procenti[i]
        baza['neželeni nasprotniki'].append(nezeleni_nasprotniki)


    procenti_otvoritev = procenti[10:]
    

    baza['otvoritve'] = []
    
    
    for i in range(len(otvoritve)):
        otvoritve_igranje = {}
        otvoritve_igranje['otvoritev'] = f'{otvoritve[i]}'
        otvoritve_igranje['igralna stopnja'] = procenti_otvoritev[3 * i]
        otvoritve_igranje['zmagovalna stopnja'] = procenti_otvoritev[(3 * i) + 2]
        baza['otvoritve'].append(otvoritve_igranje)


    procenti_mape = procenti[34:]
    

    baza['mape'] = []


    for i in range(len(mape)):
        mape_igranje = {}
        mape_igranje['mapa'] = f'{mape[i]}'
        mape_igranje['igralna stopnja'] = procenti_mape[(3 * i)]
        mape_igranje['zmagovalna stopnja'] = procenti_mape[(3 * i) + 2]
        baza['mape'].append(mape_igranje)
   

    civi = []
    civi.append(baza)
    return civi

# vrne nam slovar s seznami za vsako kategorijo




