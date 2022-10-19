# -*- coding:utf-8 -*-
__projet__ = "Ensginfo"
__nom_fichier__ = "Triangle"
__author__ = "mon_Prénom mon_Nom"
__date__ = "November 2021"

from Arete import *
from math import sqrt
from point import *
from Droite import *
import matplotlib.pyplot as plt


class Triangle:
    def __init__(self, pt1, pt2, pt3):
        self.pt1_ = pt1
        self.pt2_ = pt2
        self.pt3_ = pt3

        # les cotes du triangle
        self.arete1_ = Arete(self.pt1_, self.pt2_)
        self.arete2_ = Arete(self.pt2_, self.pt3_)
        self.arete3_ = Arete(self.pt3_, self.pt1_)

        # parametres du cercle circonscrit a ce triangle
        self.centreCercle_ = self.get_centreCercle()
        self.rayonCercle_ = self.get_rayonCercle()

    def __str__(self):
        """

        @return:  chaine permettant d'afficher les attributs d'un point
        """
        return str([str(self.pt1_) + "-" + str(self.pt2_) + "-" + str(self.pt3_)])

    def get_sommet(self):
        """

        :return: les sommets du triangles : points
        """
        return self.pt1_, self.pt2_, self.pt3_
    

    def get_arete(self):

        return [self.arete1_,self.arete2_,self.arete3_]
    

    def get_centreCercle(self):
        """
        cette fonction calcule le centre du cercle circonscrit au triangle Pt1, Pt2 et Pt3.
        En sachant que le centre du cercle circonscrit d’un triangle est l'intersection
        des deux médiatrices minimum de ses aretes (cotes).
        :return: un point
        """

        # on recupere les mediatrices (deux minimum)
        mediatrice1 = self.arete1_.mediatrice()
        mediatrice2 = self.arete2_.mediatrice()

        # on calcule l'intersection des deux mediatrices
        centre = mediatrice1.intersection(mediatrice2)

        # si les deux mediatrices sont parallele c-a-d les 3 points du triangle alignes
        if centre == "pas intersection":
            return "pas de centre"

        else:
            return centre

    def get_rayonCercle(self):
        """
        cette fonction calcule le rayon du cercle circonscrit qui passe par les points Pt1, Pt2 et Pt3.
        c-a-d disatance entre le centre du cercle et un des points du triangle
        :return: int
        """
        # on recupere les coordonnees du centre du cercle

        if self.get_centreCercle() != "pas de centre":
            x, y = self.get_centreCercle().getx(), self.get_centreCercle().gety()

            # coordonnes du point Pt1 (on peut prendre n'importe quelle point du triangle)
            x1, y1 = self.pt1_.getx(), self.pt1_.gety()

            # calcule du rayon
            rayon = sqrt((x - x1) ** 2 + (y - y1) ** 2)

            return rayon

    def in_cercle(self, pt):
        """
        Cette fonction retourne une valeur booléanne, True Si le point P se trouve à l’intérieur
        du disque Cercle dans le cas contraire False.
        :return: True ou False
        """
        if self.get_centreCercle() != "pas de centre":
            if self.rayonCercle_ >= self.centreCercle_.distance(pt):
                return True
            return False

    def dessine_triangle(self, couleur='b'):
        """
        dessine un triangle
        :return:
        """

        self.arete1_.dessine_arrete(couleur)
        self.arete2_.dessine_arrete(couleur)
        self.arete3_.dessine_arrete(couleur)

    def dessine_cerle(self, couleur='b'):
        """
        dessine le cercle circonscrit au triangle
        :return:
        """
        # coordonnes du centre du cercle

        if self.get_centreCercle() != "pas de centre":
            x, y = self.centreCercle_.getx(), self.centreCercle_.gety()
            rayon = self.rayonCercle_

            return plt.Circle((x, y), rayon, fill=False, color=couleur)

    def __eq__(self, other):
        """on crée la surcharge de l'opérateur = pour la classe triangle"""
        a1 = self.arete1_
        a2 = self.arete2_
        a3 = self.arete3_
        b1 = other.arete1_
        b2 = other.arete2_
        b3 = other.arete3_

        if a1 in [b1, b2, b3] and a2 in [b1, b2, b3] and a3 in [b1, b2, b3]:
            return True
        return False


if __name__ == '__main__':
    pt1 = Point(2, 3)
    pt2 = Point(-1, 3)
    pt3 = Point(5, 7)
    pt4 = Point(0, 0)

    t = Triangle(pt1, pt2, pt3)
    t2 = Triangle(pt4, pt2, pt3)
    print(t == t2)

    t.dessine_cerle()
    t.dessine_triangle()

    print(t)
