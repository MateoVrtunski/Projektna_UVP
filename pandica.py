import pandas as pd
import matplotlib.pyplot as plt


civ = pd.read_csv('civilizacije_tabela.csv')
sici_zeleni = pd.read_csv('sicilijanci_zeleni_nasprotniki.csv')
sici_nezeleni = pd.read_csv('sicilijanci_nezeleni_nasprotniki.csv')
sici_otvoritve = pd.read_csv('sicilijanci_otvoritve.csv')
sici_mape = pd.read_csv('sicilijanci_mape.csv')
megrandom = pd.read_csv("megarandom_tabela.csv")


def graf_glavni(file):

    file.plot(kind= 'bar',
        x = "civilizacija",width = 0.6, xlabel = "Civilizacije", ylabel = 'Procenti (%)',
        secondary_y= 'igralna stopnja', rot= 90 )

    plt.title('Razmerje igralne in zmagovalne stopnje posamezne civilizacije')
    plt.legend(loc='best')
    plt.show()

def civ_zeleni(file):
    file.plot(kind= 'bar',
        x = "civilizacija",width = 0.6, xlabel = "Civilizacije", y = "zmagovalna stopnja", ylabel ='Procenti(%)', color = 'green')
    plt.title('Želeni nasprotniki')
    plt.ylim(50,63)
    plt.show()

def civ_nezeleni(file):
    file.plot(kind= 'bar',
        x = "civilizacija",width = 0.6, xlabel = "Civilizacije", y = "zmagovalna stopnja", ylabel ='Procenti(%)', color = 'red')
    plt.title('Neželeni nasprotniki')
    plt.ylim(35,47)
    plt.show()

def civ_otvoritve_igr(file):
    file.plot(kind= 'pie',
        y = 'igralna stopnja', labels = file['otvoritev'],radius = 1.8)
    plt.legend('',frameon=False)
    plt.ylabel('')
    plt.show()

def civ_otvoritve_zmg(file):
    file.plot(kind= 'bar',
        x = "otvoritev",width = 0.6, xlabel = "Otvoritve", y = "zmagovalna stopnja", ylabel ='Procenti(%)', color = 'turquoise')
    plt.title('Procenti zmag pri posameznih otvoritvah')
    plt.ylim(30,55)
    plt.show()


def civ_mape(file):

    file.plot(kind= 'bar',
        x = "mapa",width = 0.6, xlabel = "Mape", ylabel = 'Procenti (%)',
        secondary_y= 'igralna stopnja', rot= 90, color = ["violet", "blue"] )

    plt.title('Razmerje igralne in zmagovalne stopnje na posamezni mapi')
    
    plt.show()

def mapa_vse(file):

    file.plot(kind= 'bar',
        x = "civilizacija",width = 0.8, xlabel = "Civilizacije", ylabel = 'Procenti (%)',
        secondary_y= 'igralna stopnja', rot= 90, color = ["turquoise", "orange"] )
    plt.title('Razmerje igralne in zmagovalne stopnje na megarandom')
    plt.legend(loc='best')
    plt.show()



hej = mapa_vse(megrandom)







