# -*- coding:utf-8 -*-
__projet__ = "Ensginfo"
__nom_fichier__ = "Droite"
__author__ = "mon_Prénom mon_Nom"
__date__ = "November 2021"

from point import *
from Droite import *
import matplotlib.pyplot as plt
from math import *


class Arete:
    """
    les instances de cette classe sont des segments d'extremite pt1  et pt2
    """
    def __init__(self, pt1, pt2):
        self.pt1_ = pt1
        self.pt2_ = pt2

    def get_droite(self):
        """
         donne l’équation (ax +by+ c =0) réduite d’une droite associee a l'arete (passant par les points Pt1 et Pt2)
        :return: Droite
        """
        # on extrait les coordonnees des points pt1 , pt2
        x1, y1 = self.pt1_.getx(), self.pt1_.gety()
        x2, y2 = self.pt2_.getx(), self.pt2_.gety()
        a = y1 - y2
        b = x2 - x1
        c = y2 * x1 - y1 * x2
        return Droite(a, b, c)

    def mediatrice(self):
        """
        cette fonction retourne l’équation d’une médiatrice (ax +by +c=0) de l'arete
        :return: Droite
        """
        x1, y1 = self.pt1_.getx(), self.pt1_.gety()
        x2, y2 = self.pt2_.getx(), self.pt2_.gety()

        a = 2 * (x2 - x1)
        b = 2 * (y2 - y1)
        c = x1 ** 2 + y1 ** 2 - x2 ** 2 - y2 ** 2

        return Droite(a, b, c)

    def dessine_arrete(self, couleur='b'):
        x1, y1 = self.pt1_.getx(), self.pt1_.gety()
        x2, y2 = self.pt2_.getx(), self.pt2_.gety()
        plt.plot([x1, x2], [y1, y2], marker="o", color=couleur)
        
    
    def longueur(self):
        """cette méthode retourne la longueur du segment"""
        x1, y1 = self.pt1_.x_,self.pt1_.y_
        x2, y2 = self.pt2_.x_, self.pt2_.y_
        ln = sqrt((x1-x2)**2+(y1-y2)**2)
        return ln

    def __eq__(self, other):
        """
        surcharge permettant de comparer si deux aretes sont egaux
        :param other: autre arete
        :return: Bol
        """
        pt1, pt2 = self.pt1_, self.pt2_
        pt3, pt4 = other.pt1_, other.pt2_
        if pt1 == pt3 and pt2 == pt4:
            return True
        if pt1 == pt4 and pt2 == pt3:
            return True
        return False
