import csv
import glavni_podatki
import izlusci_podatke_mape
import izlusci_podatke_civilizacije

# uvozimo civilizacije, tu bomo ustvarili csv tabele iz slovarjev, ki smo jih prej naredili

podatki = glavni_podatki.glavni_seznam

# tabela z glavnimi podatki

with open("civilizacije_tabela.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=["civilizacija", "igralna stopnja", "zmagovalna stopnja", "stevilo iger"])
    writer.writeheader()
    for row in podatki:
        writer.writerow(row)

# tabela mape
    
megarandom = izlusci_podatke_mape.izlusci_podatke_map('megarandom')

with open("megarandom_tabela.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=["civilizacija", "igralna stopnja", "zmagovalna stopnja"])
    writer.writeheader()
    for row in megarandom:
        writer.writerow(row)

# tabele civilizacije

sicilianci = izlusci_podatke_civilizacije.izlusci_vse_podatke('sicilians')

with open("sicilijanci_zeleni_nasprotniki.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=["civilizacija", "zmagovalna stopnja"])
    writer.writeheader()
    for row in sicilianci[0]['želeni nasprotniki']:
        writer.writerow(row)

with open("sicilijanci_nezeleni_nasprotniki.csv", "w") as f:    
    writer = csv.DictWriter(f, fieldnames=["civilizacija", "zmagovalna stopnja"])
    writer.writeheader()
    for row in sicilianci[0]['neželeni nasprotniki']:
        writer.writerow(row)
        
with open("sicilijanci_otvoritve.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=["otvoritev", "igralna stopnja","zmagovalna stopnja"])
    writer.writeheader()
    for row in sicilianci[0]['otvoritve']:
        writer.writerow(row)

with open("sicilijanci_mape.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=["mapa", "igralna stopnja","zmagovalna stopnja"])
    writer.writeheader()
    for row in sicilianci[0]['mape']:
        writer.writerow(row)

    

    