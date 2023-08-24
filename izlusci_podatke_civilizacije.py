import re



def izlusci_vse_podatke(ime):
    with open(f'{ime}.html') as f:
        html_civilizacija = f.read()
  

    procenti = []
    vzorec_procentov = r"\d+\.\d{2}%" 
    procenti.append(re.findall(vzorec_procentov,html_civilizacija))
    procenti = procenti[0]
    procenti = procenti[4:]
    

    najboljsi_najslabsi = []
    vzorec_nn = r"/assets/civ_crests/\w+\.webp" 
    najboljsi_najslabsi.append(re.findall(vzorec_nn,html_civilizacija))
    najboljsi_najslabsi = najboljsi_najslabsi[0]
    najboljsi_najslabsi.remove(najboljsi_najslabsi[0])
    for i in range(len(najboljsi_najslabsi)):
        najboljsi_najslabsi[i] = najboljsi_najslabsi[i].replace('/assets/civ_crests/','')
        najboljsi_najslabsi[i] = najboljsi_najslabsi[i].replace('.webp','')


    otvoritve = []
    vzorec_otvoritve = r"/assets/openings/\w+\.webp" 
    otvoritve.append(re.findall(vzorec_otvoritve,html_civilizacija))
    otvoritve = otvoritve[0]
    for i in range(len(otvoritve)):
        otvoritve[i] = otvoritve[i].replace('/assets/openings/','')
        otvoritve[i] = otvoritve[i].replace('.webp','')

    mape = []
    vzorec_mape = r"/assets/maps/\w+\.webp" 
    mape.append(re.findall(vzorec_mape,html_civilizacija))
    mape = mape[0]
    for i in range(len(mape)):
        mape[i] = mape[i].replace('/assets/maps/','')
        mape[i] = mape[i].replace('.webp','')

    
    baza = {}

    

    baza['želeni nasprotniki'] = []
    zeleni_nasprotniki = {}
    baza['želeni nasprotniki'].append(zeleni_nasprotniki)

    for i in range(5):
        zeleni_nasprotniki[f'{najboljsi_najslabsi[i]}'] = procenti[i]
    

    baza['neželeni nasprotniki'] = []
    nezeleni_nasprotniki = {}
    baza['neželeni nasprotniki'].append(nezeleni_nasprotniki)

    for i in range(5,10):
        nezeleni_nasprotniki[f'{najboljsi_najslabsi[i]}'] = procenti[i]

    procenti_otvoritev = procenti[10:]
    

    baza['igralna stopnja otvoritev'] = []
    otvoritve_igranje = {}
    baza['igralna stopnja otvoritev'].append(otvoritve_igranje)

    for i in range(len(otvoritve)):
        otvoritve_igranje[f'{otvoritve[i]}'] = procenti_otvoritev[3 * i]

    baza['zmagovalna stopnja otvoritev'] = []
    otvoritve_zmage = {}
    baza['zmagovalna stopnja otvoritev'].append(otvoritve_zmage)

    for i in range(len(otvoritve)):
        otvoritve_zmage[f'{otvoritve[i]}'] = procenti_otvoritev[(3 * i) + 2]

    procenti_mape = procenti[37:]


    baza['igralna stopnja na posamezni mapi'] = []
    mape_igranje = {}
    baza['igralna stopnja na posamezni mapi'].append(mape_igranje)

    for i in range(len(mape)):
        mape_igranje[f'{mape[i]}'] = procenti_mape[(3 * i)]

    baza['zmagovalna stopnja na posamezni mapi'] = []
    mape_zmage = {}
    baza['zmagovalna stopnja na posamezni mapi'].append(mape_zmage)

    for i in range(len(mape)):
        mape_zmage[f'{mape[i]}'] = procenti_mape[(3 * i) + 2]

    civi = []
    civi.append(baza)
    return civi



mongol = izlusci_vse_podatke('mongols')
print(mongol)