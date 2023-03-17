import numpy as np
import matplotlib.pyplot as plt



class Pret(object):

    def __init__(self, capital, T, duree):

        # ---------------------------------------------------------------------------------------------------
        # attributs paramètres
        # ---------------------------------------------------------------------------------------------------

        # taux d'intérêts annuel
        self.m_T = T

        # reste du capital à payer
        self.m_capital = capital

        # durée remboursement en années
        self.m_duree = duree



        # ---------------------------------------------------------------------------------------------------
        # autres attributs
        # ---------------------------------------------------------------------------------------------------

        # taux d'intérêts mensuel (taux annuel / 12)
        self.m_t = T / 12

        # nombre de mensualités
        self.m_n = duree * 12

        # reste du capital à rembourser après la i-ème mensualité
        self.m_C = np.repeat(0.0, self.m_n + 1)
        self.m_C[0] = capital

        # montant (constant) d'une mensualité (assurance + intérêts + capital)
        self.m_mens = (self.m_t * self.m_C[0]) / (1 - (self.m_t + 1)**(-self.m_n))

        # part du remboursement chaque mois (varie)
        self.m_partCapital = np.repeat(0.0, self.m_n + 1)
        self.m_partInteret = np.repeat(0.0, self.m_n + 1)
        self.m_partAssurance = np.repeat(0.0, self.m_n + 1)

        # somme d'assurance remboursée à la fin du prêt
        self.m_totAssurance = 0.0

        # somme d'intérêts remboursés à la fin du prêt
        self.m_totInteret = 0.0

        # Total remboursé à la fin (assurance + intérêts + capital)
        self.m_totRemboursement = 0.0


        # par années, pour représentations graphiques
        self.m_partInteretAnnee = np.repeat(0.0, self.m_duree)
        self.m_partCapitalAnnee = np.repeat(0.0, self.m_duree)
    #}



    def build(self):

        # calcul part assurance / intérêts / capital par mois
        for mois in range(self.m_n):
            self.m_partAssurance[mois + 1] = 0.0
            self.m_partInteret[mois + 1] = self.m_t * self.m_C[mois]
            self.m_partCapital[mois + 1] = self.m_mens - self.m_partInteret[mois + 1] - self.m_partAssurance[mois + 1]

            self.m_C[mois + 1] = self.m_C[mois] - self.m_partCapital[mois + 1]
        #}

        # calcul des totaux
        self.m_totAssurance = sum(self.m_partAssurance)
        self.m_totInteret = sum(self.m_partInteret)
        self.m_totRemboursement = self.m_totAssurance + self.m_totInteret + self.m_capital

        # regroupement par années
        for i in range(self.m_duree):
            # print(i, "   ", 12*i+1, ':', 12*(i+1)+1, '|', self.m_partInteret[12*i+1:12*(i+1)+1])
            self.m_partInteretAnnee[i] = sum(self.m_partInteret[12*i+1:12*(i+1)+1])
            self.m_partCapitalAnnee[i] = sum(self.m_partCapital[12*i+1:12*(i+1)+1])
        #}
    #}



    def __str__(self):

        chaine = ''

        chaine += 'Prix achat : {}\n'
        chaine += 'Taux annuel : {}\n'
        chaine += 'Mensualitées : {}\n'
        chaine += 'Total assurance : {}\n'
        chaine += 'Total intérêts : {}\n'
        chaine += 'Total remboursé : {}'

        return chaine.format(self.m_capital, self.m_T, self.m_mens, self.m_totAssurance, self.m_totInteret, self.m_totRemboursement)
    #}



    def verif():

        print('int')
        print(self.m_partInteret)
        print('cap')
        print(self.m_partCapital)
        print('int + cap')
        print(self.m_partInteret + self.m_partCapital)
        print('sum cap')
        print(np.sum(self.m_partCapital))
        print('sum int')
        print(np.sum(self.m_partInteret))
    #}



    def graph(self):

        # indice des mois
        ind = np.arange(self.m_n + 1)

        # bar plot
        p1 = plt.bar(ind, self.m_partInteret, color='r')
        p2 = plt.bar(ind, self.m_partCapital, bottom=self.m_partInteret, color='g')

        # paramètres graphiques
        plt.ylabel('Montant')
        plt.xlabel('Mois')
        t = self.__str__()
        plt.title(t)
        plt.xticks(ind)
        plt.legend((p1[0], p2[0]), ('Intérêts', 'Capital'))

        plt.show()
    #}



    def graph2(self):

        # indice des années
        ind = np.arange(1, self.m_duree + 1)

        # bar plot
        p1 = plt.bar(ind, self.m_partInteretAnnee, color='r')
        p2 = plt.bar(ind, self.m_partCapitalAnnee, bottom=self.m_partInteretAnnee, color='g')

        # paramètres graphiques
        plt.ylabel('Montant')
        plt.xlabel('Années')
        t = self.__str__()
        plt.title(t)
        plt.xticks(ind)
        plt.legend((p1[0], p2[0]), ('Intérêts', 'Capital'))

        plt.show()
    #}
#}
