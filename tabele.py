import csv
import glavni_podatki
import izlusci_podatke_mape
import izlusci_podatke_civilizacije

podatki = glavni_podatki.glavni_seznam

with open("civilizacije_tabela.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=["civilizacija", "igralna stopnja", "zmagovalna stopnja", "stevilo iger"])
    writer.writeheader()
    for row in podatki:
        writer.writerow(row)
    
megarandom = izlusci_podatke_mape.izlusci_podatke_map('megarandom')

with open("megarandom_tabela.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=["civilizacija", "igralna stopnja", "zmagovalna stopnja"])
    writer.writeheader()
    for row in megarandom:
        writer.writerow(row)

sicilianci = izlusci_podatke_civilizacije.izlusci_vse_podatke('sicilians')

with open("sicilijanci_tabela.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=["želeni nasprotniki", "neželeni nasprotniki", 
                                           "igralna stopnja otvoritev", 'zmagovalna stopnja otvoritev','igralna stopnja na posamezni mapi'
                                           'zmagovalna stopnja na posamezni mapi'])
    writer.writeheader()
    for row in sicilianci:
        writer.writerow(row)