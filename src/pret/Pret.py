import numpy as np
import matplotlib.pyplot as plt



class Pret(object):

    def __init__(self, capital, T, duree):


        # taux d'intérêts mensuel (taux annuel / 12)
        self.m_t = T / 12

        # nombre de mensualités
        self.m_n = duree * 12

        # durée remboursement en années
        self.m_duree = duree

        # reste du capital à payer
        self.m_capital = capital

        # reste du capital à rembourser après la i-ème mensualité
        self.m_C = np.repeat(0.0, self.m_n + 1)
        self.m_C[0] = capital

        # mensualité
        self.m_mens = (self.m_t * self.m_C[0]) / (1 - (self.m_t + 1)**(-self.m_n))

        # part du remboursement par année
        self.m_partCapital = np.repeat(0.0, self.m_n + 1)
        self.m_partInteret = np.repeat(0.0, self.m_n + 1)
        self.m_partAssurance = np.repeat(0.0, self.m_n + 1)

        self.m_annuite = (capital * T) / (1 - (1 + T/12)**(-12*duree))
        self.m_annuite = 10000.0
    #}

    def build(self):
        for mois in range(self.m_n):
            self.m_partAssurance[mois + 1] = 0.0
            self.m_partInteret[mois + 1] = self.m_t * self.m_C[mois]
            self.m_partCapital[mois + 1] = self.m_mens - self.m_partInteret[mois + 1] - self.m_partAssurance[mois + 1]

            self.m_C[mois + 1] = self.m_C[mois] - self.m_partCapital[mois + 1]
        #}


        # print(self.m_capital)
        # print('part cap')
        # print(self.m_partCapital)
        # print('part int')
        # print(self.m_partInteret)
        # print('part ass')
        # print(self.m_partAssurance)

        # i = 0
        # while sum(self.m_partCapital) < self.m_capital and i < 25:
        #     self.m_partInteret.append(self.m_tauxAnnuel * (self.m_capital - sum(self.m_partCapital[0:i+1])))
        #     self.m_partCapital.append(self.m_annuite - self.m_partInteret[i + 1])
        #     print(self.m_partInteret[i], self.m_partCapital[i])
        #     i += 1
        # #}

        # print()
        # print(sum(self.m_partInteret))
        # print(sum(self.m_partCapital))
    #}

    def graph(self):
        # N = 5
        # menMeans = (20, 35, 30, 35, 27)
        # womenMeans = (25, 32, 34, 20, 25)
        # menStd = (2, 3, 4, 1, 2)
        # womenStd = (3, 5, 2, 3, 3)
        # ind = np.arange(N)    # the x locations for the groups
        # width = 0.35       # the width of the bars: can also be len(x) sequence

        # p1 = plt.bar(ind, menMeans, width, yerr=menStd)
        # p2 = plt.bar(ind, womenMeans, width, bottom=menMeans, yerr=womenStd)

        # plt.ylabel('Scores')
        # plt.title('Scores by group and gender')
        # plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
        # plt.yticks(np.arange(0, 81, 10))
        # plt.legend((p1[0], p2[0]), ('Men', 'Women'))

        # plt.show()



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

        # ind = np.arange(self.m_n)    # the x locations for the groups
        # width = 0.35       # the width of the bars: can also be len(x) sequence

        # p1 = plt.bar(ind, self.m_partInteret, width)
        # p2 = plt.bar(ind, self.m_partCapital, width, bottom=self.m_partInteret)

        # plt.show()
    #}
#}
