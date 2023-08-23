import re

import civilizacije

civilizacija = civilizacije.zajem_civilizacij("stran.html")


with open('stran33.html') as f:
    html_sicilianci = f.read()

procenti = []
vzorec_procentov = r"\d+\.\d{2}%" 
procenti.append(re.findall(vzorec_procentov,html_sicilianci))
procenti = procenti[0]
procenti = procenti[4:]


najboljsi_najslabsi = []

vzorec_nn = r"/assets/civ_crests/\w+.webp" 
najboljsi_najslabsi.append(re.findall(vzorec_nn,html_sicilianci))
najboljsi_najslabsi = najboljsi_najslabsi[0]
najboljsi_najslabsi.remove(najboljsi_najslabsi[0])
for i in range(len(najboljsi_najslabsi)):
    najboljsi_najslabsi[i] = najboljsi_najslabsi[i].replace('/assets/civ_crests/','')
    najboljsi_najslabsi[i] = najboljsi_najslabsi[i].replace('.webp','')

sicilianci = []
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
    
sicilianci.append(baza)



print(sicilianci)

