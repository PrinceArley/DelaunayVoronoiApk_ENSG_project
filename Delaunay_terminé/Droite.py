# -*- coding:utf-8 -*-
__projet__ = "Ensginfo"
__nom_fichier__ = "Droite"
__author__ = "mon_Prénom mon_Nom"
__date__ = "November 2021"

# Imports
from point import *


# on créé la classe Droite
class Droite:
    def __init__(self, a, b, c):
        """une droite est définie pas trois valeurs a, b, c telles que ax+ by + c = 0"""
        self.a_ = a
        self.b_ = b
        self.c_ = c

    def intersection(self, other):
        """
        cette fonction calcule l’intersection de deux droites. c.à.d. qu’il faut résoudre un système de 2 équations à 2
        inconnues : a1x+ b1y + c1 = 0; a2x + b2y + c2 = 0.
        Elle retourne les coordonnées cartésiennes du point d’intersection,
        :param other:
        :return: x et y du pt d'intersection
        """
        # on teste si le denominateur est non nul ou pas (c-a-d si on a deux droite parallele)
        try:
            # apres resolution on trouve :
            x = (-other.b_ * self.c_ + self.b_ * other.c_) / (self.a_ * other.b_ - self.b_ * other.a_)

            y = (-self.a_ * other.c_ + other.a_ * self.c_) / (self.a_ * other.b_ - self.b_ * other.a_)
            return Point(x, y)

        # au cas ou deux droite sont parallele, on retourne ce str qui sera utilise dans la methode get centre de la classe Triangle
        except ZeroDivisionError:
            return "pas intersection"


if __name__ == '__main__':
    droite1 = Droite(1, 2, 1)
    droite2 = Droite(2, 2, 0)

    print(droite1.intersection(droite2))
