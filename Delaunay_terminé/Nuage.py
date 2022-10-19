# -*- coding:utf-8 -*-
__projet__ = "Ensginfo"
__nom_fichier__ = "Nuage"
__author__ = "mon_Prénom mon_Nom"
__date__ = "October 2021"

# Imports
from pointNuage import Point
from trace_courbe_liste import trace_courbe_liste
from ccw import ccw


# on créé la classe Nuage
class Nuage:
    """

    """

    def __init__(self, list):

        self.enspoints_ = list

    def get_ancre(self):
        """
         permet de rechercher l’ancre de l’ensemble de points,
         c’est-àdire le point le plus bas dans le nuage de points.
        :return: le point ancre
        """
        ancre = min(self.enspoints_)

        return ancre

    def get_boite_nuage(self, delta=50):
        """
        methode qui modifie et cree une enCov. artificielle et renvoie les 4 points de
        cette qui englobe le nuage de pt y compris l'enveloppe convexe
        :param delta: marge d'espacement
        :return:
        """
        liste_x = []
        liste_y = []
        # pour dimunier la tache on utilise l'enveloppe convexe qui contient que des pts extremes
        for point in self.get_enveloppe_Graham():
            x = point.getx()
            liste_x.append(x)

            y = point.gety()
            liste_y.append(y)

        # on recupere les extremes
        x_min = min(liste_x) - delta
        x_max = max(liste_x) + delta

        y_min = min(liste_y) - delta
        y_max = max(liste_y) + delta

        # alors on a les point:
        pt1 = Point(x_min, y_min)
        pt2 = Point(x_max, y_min)
        pt3 = Point(x_max, y_max)
        pt4 = Point(x_min, y_max)

        boite = [pt1, pt2, pt3, pt4]  # boite du nuage

        return boite

    def get_polygone(self):
        """
        permet de trier les points initiaux par rapport à cette ancre
        et de construire ainsi un « polygone
        :return:
        """
        ancre = self.get_ancre()
        self.enspoints_.remove(
            ancre)  # on enleve l'ancre pour ne pas avoir un angle des pbs dans les calcules de l'angle
        self.enspoints_.sort(key=lambda pt: pt.calcule_angle(ancre))

        self.enspoints_.append(ancre)  # on remet
        return self.enspoints_

    def get_enveloppe_Graham(self):
        """
        execute l'algorithme de Graham à la liste de point
        afin de construire une liste qui constitue l'enveloppe convexe
            """

        self.get_polygone()

        pp = self.get_ancre()
        Env = [pp]

        for indice in range(1, len(self.enspoints_) - 1):
            p = self.enspoints_[indice]
            ps = self.enspoints_[indice + 1]

            if ccw(pp, p, ps) != -1:
                # on tourne dans le sens des aiguilles d une montre
                Env.append(p)
            else:
                p = pp
                pp = Env[-2]
                while ccw(pp, p, ps) == -1:
                    Env.pop()
                    p = pp
                    pp = Env[-2]
            pp = p
        self.Env_ = Env  # creatiion d'un nouvel attribut
        return self.Env_

    def get_interieur_Env(self):
        """

        Returns
        -------
        List
            return la liste des points interieurs à l'enveloppe convexe'

        """
        inter = []
        for pt in self.enspoints_:
            if not (pt in self.Env_):
                inter.append(pt)
        self.inter_ = inter
        return self.inter_


if __name__ == '__main__':
    filename1 = "points_non_tries.dta"
    filename2 = "points.dta"
    filename3 = "points_hasard.dta"
    nuage = Nuage([Point(1, 2), Point(0, 3), Point(5, 3), Point(0.5, 0)])

    # nuage.get_polygone()
    # trace_courbe_liste(nuage.enspoints_)
    nuage.get_enveloppe_Graham()
    trace_courbe_liste(nuage.Env_)
    # print(nuage.get_ancre())
