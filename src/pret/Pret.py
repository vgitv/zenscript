import numpy as np
import matplotlib.pyplot as plt


def autolabel(rects, xpos="center"):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    ha = {"center": "center", "right": "left", "left": "right"}
    offset = {"center": 0, "right": 1, "left": -1}

    for rect in rects:
        height = round(rect.get_height(), 2)
        plt.annotate(
            "{}".format(height),
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(offset[xpos] * 3, 3),
            textcoords="offset points",
            ha=ha[xpos],
            va="bottom",
        )


class Pret(object):
    def __init__(self, capital, T, duree, total_assurance, frais_dossier):
        # ---------------------------------------------------------------------------------------------------
        # attributs paramètres
        # ---------------------------------------------------------------------------------------------------

        # taux d'intérêts annuel
        self.m_T = T

        # reste du capital à payer
        self.m_capital = capital

        # frais dossier
        self.m_frais_dossier = frais_dossier

        # durée remboursement en années
        self.m_duree = duree

        # coût total assurance
        self.m_total_assurance = total_assurance

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

        # assurance mensuelle (constante)
        self.m_assurance = self.m_total_assurance / self.m_duree / 12

        # montant (constant) d'une mensualité sans l'assurance (intérêts + capital)
        self.m_mens = (self.m_t * self.m_C[0]) / (1 - (self.m_t + 1) ** (-self.m_n))

        # part du remboursement chaque mois (varie)
        self.m_partCapital = np.repeat(0.0, self.m_n + 1)
        self.m_partInteret = np.repeat(0.0, self.m_n + 1)
        self.m_partAssurance = np.repeat(0.0, self.m_n + 1)

        # somme d'intérêts remboursés à la fin du prêt
        self.m_totInteret = 0.0

        # Total remboursé à la fin (assurance + intérêts + capital)
        self.m_totRemboursement = 0.0

        # par années, pour représentations graphiques
        self.m_partAssuranceAnnee = np.repeat(0.0, self.m_duree)
        self.m_partInteretAnnee = np.repeat(0.0, self.m_duree)
        self.m_partCapitalAnnee = np.repeat(0.0, self.m_duree)

    def build(self):
        # calcul part assurance / intérêts / capital par mois
        for mois in range(self.m_n):
            self.m_partAssurance[mois + 1] = self.m_assurance
            self.m_partInteret[mois + 1] = self.m_t * self.m_C[mois]
            self.m_partCapital[mois + 1] = self.m_mens - self.m_partInteret[mois + 1]

            self.m_C[mois + 1] = self.m_C[mois] - self.m_partCapital[mois + 1]

        # calcul des totaux
        self.m_totInteret = sum(self.m_partInteret)
        self.m_totRemboursement = (
            self.m_total_assurance + self.m_totInteret + self.m_capital + self.m_frais_dossier
        )

        # regroupement par années
        for i in range(self.m_duree):
            # print(i, "   ", 12*i+1, ':', 12*(i+1)+1, '|', self.m_partInteret[12*i+1:12*(i+1)+1])
            self.m_partAssuranceAnnee[i] = 12 * self.m_assurance
            self.m_partInteretAnnee[i] = sum(
                self.m_partInteret[12 * i + 1: 12 * (i + 1) + 1]
            )
            self.m_partCapitalAnnee[i] = sum(
                self.m_partCapital[12 * i + 1: 12 * (i + 1) + 1]
            )

    def __str__(self):
        chaine = ""

        chaine += "Taux intérêts   : {} %\n"
        chaine += "Total assurance : {} €\n"
        chaine += "Capital         : {} €\n"
        chaine += "Frais dossier   : {} €\n"
        chaine += "Total intérêts  : {} €\n"
        chaine += "Total assurance : {} €\n"
        chaine += "Coût prêt       : {} €\n"
        chaine += "Mensualitées    : {} + {} = {} €\n"

        return chaine.format(
            round(self.m_T * 100, 2),
            round(self.m_total_assurance),
            self.m_capital,
            self.m_frais_dossier,
            round(self.m_totInteret, 2),
            round(self.m_total_assurance, 2),
            round(self.m_totRemboursement, 2),
            round(self.m_mens, 2),
            round(self.m_assurance, 2),
            round(self.m_mens + self.m_assurance, 2),
        )

    def verif(self):
        print("int")
        print(self.m_partInteret)
        print("cap")
        print(self.m_partCapital)
        print("int + cap")
        print(self.m_partInteret + self.m_partCapital)
        print("sum cap")
        print(np.sum(self.m_partCapital))
        print("sum int")
        print(np.sum(self.m_partInteret))
        print("assurance")

    def graph(self):
        # indice des mois
        ind = np.arange(self.m_n + 1)

        # bar plot
        plt.bar(ind, self.m_partAssurance, color="#5cacee")
        plt.bar(ind, self.m_partInteret, bottom=self.m_partAssurance, color="#ffc125")
        plt.bar(
            ind,
            self.m_partCapital,
            bottom=self.m_partAssurance + self.m_partInteret,
            color="#00688b",
        )

        # paramètres graphiques
        plt.ylabel("Montant")
        plt.xlabel("Mois")
        t = self.__str__()
        plt.title(t)
        plt.xticks(np.arange(0, self.m_n + 1, 12))
        # plt.legend((p1[0], p2[0], p3[0]), ('Assurance', 'Intérêts', 'Capital'))

        plt.show()

    def graph2(self):
        plt.figure(0)
        plt.subplot2grid((2, 2), (0, 0), colspan=2)

        # indice des années
        ind = np.arange(1, self.m_duree + 1)

        # bar plot
        # subplot 1
        p1 = plt.bar(ind, self.m_partAssuranceAnnee, color="#5cacee")
        p2 = plt.bar(
            ind,
            self.m_partInteretAnnee,
            bottom=self.m_partAssuranceAnnee,
            color="#ffc125",
        )
        p3 = plt.bar(
            ind,
            self.m_partCapitalAnnee,
            bottom=self.m_partAssuranceAnnee + self.m_partInteretAnnee,
            color="#00688b",
        )

        # paramètres graphiques
        plt.ylabel("Montant")
        plt.xlabel("Années")
        plt.title("Remboursements par année")
        plt.xticks(ind)
        plt.legend((p3[0], p2[0], p1[0]), ("Capital", "Intérêts", "Assurance"))

        # subplot 2
        plt.subplot2grid((2, 2), (1, 0))
        values = [
            self.m_capital,
            self.m_totRemboursement,
            self.m_total_assurance,
            self.m_totInteret,
            self.m_total_assurance + self.m_totInteret,
        ]
        labels = ["capital", "total", "assurance", "intérêts", "total"]
        p1 = plt.bar(
            range(len(values)), [int(round(elt)) for elt in values], tick_label=labels
        )
        autolabel(p1)
        axes = plt.gca()
        axes.set_ylim([0, self.m_totRemboursement * 1.2])
        plt.title("Remboursement total")

        plt.suptitle(
            "Pret à taux : Ti = {} % ; assurance = {} €\nMensualité : {} + {} ~= {}€ sur {} ans".format(
                round(self.m_T * 100, 2),
                round(self.m_total_assurance),
                round(self.m_mens, 2),
                round(self.m_assurance, 2),
                round(self.m_mens + self.m_assurance, 2),
                self.m_duree,
            )
        )

        plt.show()
