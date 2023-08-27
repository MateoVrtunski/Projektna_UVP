import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

civ = pd.read_csv('civilizacije_tabela.csv')
sici_zeleni = pd.read_csv('sicilijanci')


def graf_glavni(file):

    file.plot(kind= 'bar',
        x = "civilizacija",width = 0.6, xlabel = "Civilizacije", ylabel = 'Procenti (%)',
        secondary_y= 'igralna stopnja', rot= 90 )

    plt.title('Razmerje igralne in zmagovalne stopnje posamezne civilizacije')
    plt.legend(loc='best')
    plt.show()

#def sicilianci_civilizacije(file):




