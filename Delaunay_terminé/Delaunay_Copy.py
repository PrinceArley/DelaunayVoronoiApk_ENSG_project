# -*- coding:utf-8 -*-
__projet__ = "Ensginfo"
__nom_fichier__ = "Delaunay"
__author__ = "mon_Prénom mon_Nom"
__date__ = "November 2021"

# Imports
from scipy.spatial import Delaunay as Dl
from point import *
from Nuage import *
import matplotlib.pyplot as plt
import random
from copy import copy
from Triangle import *
from clockwise_sorter import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


# on crée la classe Delaunay
class Delaunay:
    def __init__(self, filename):
        """on initialise l'objet de la classe Delaynay en lui créant les attributs
        -listPoints qui contient la liste des points à trianguler
        -listTrianglesDelaunay qui contient la liste des triangles qui appartiennent à la triangulation
        
        puis on fait appel à la méthode initialisation"""

        lpoints = []
        file = open(filename)
        for ligne in file:
            x, y = ligne.split()
            x, y = float(x), float(y)
            lpoints.append(Point(x, y))

        self.listPoints_ = lpoints
        self.listTrianglesDelaunay_ = []
        self.liste_centres = []

        self.initiallisation()

    def __str__(self):
        """Cette méthode crée la surcharge str pour la classe triangle"""
        chaine = ""
        for triangle in self.listTrianglesDelaunay_:
            chaine += str(triangle)
        return chaine

    def initiallisation(self):
        """
        creation des triangles initiaux avec lequel on debutera la methode incrementale
        :return: rien car cette méthode se contente de modifier les attributs de l'objet'
        """

        # on va commencer par creer l'enveloppe convexe de tous les point de donnee
        self.nuage_pts_ = Nuage(self.listPoints_)
        self.enConvexe_ = self.nuage_pts_.get_boite_nuage()

        # on cree les deux primier triangle de delaunay de la boite et on les ajoutes dans la liste des triangle de delaunay

        first_triangle = Triangle(self.enConvexe_[0], self.enConvexe_[1], self.enConvexe_[2])
        self.listTrianglesDelaunay_.append(first_triangle)
        second_triangle = Triangle(self.enConvexe_[2], self.enConvexe_[3], self.enConvexe_[0])
        self.listTrianglesDelaunay_.append(second_triangle)

    def triangle_conflit(self, point):
        """
        permet de collecter tout les triangles en conflit avec le point courant

        :param point: point a tester
        :return: retourne la liste des triangles en conflit avec le ajouter pt
        """
        l_triangle_conflit = []
        for triangle in self.listTrianglesDelaunay_:
            if triangle.in_cercle(point) == True:
                l_triangle_conflit.append(triangle)
        return l_triangle_conflit

    def mise_a_jour(self):
        """cette méthode sert à tester tous les triangles de la liste des triangles de
        la triangulation et ne garder que ceux qui respectent les conditions de Delaunay"""
        l_mise_a_jour = []

        for triangle in self.listTrianglesDelaunay_:
            if triangle.get_centreCercle() != None and triangle.get_rayonCercle() != None:
                l_mise_a_jour.append(triangle)

        self.listTrianglesDelaunay_ = l_mise_a_jour

        return l_mise_a_jour

    def ajouter_pt(self, point):
        """
        permet d'ajouter un nouveau point, teste la condition de Delaunay ,
        supprime les triangles en conflits et creee des nouveaux triangles
        :param point: point
        :return:
        """

        list_sommets_conflit = []
        list_triangle_conflit = self.triangle_conflit(
            point)  # on crée la liste de triangles dont le cercle circonscrit contient le point qu'on a ajouté

        if list_triangle_conflit != []:
            # on retire l’intérieur de la cavité, qui est l'ensemble des triangles dont le cercle
            # circonscrit contient le point à insérer
            # on supprime les triangles en conflit avec le point de la liste des triangles de delaunay

            for triangle in list_triangle_conflit:

                self.listTrianglesDelaunay_.remove(triangle)

                # on stocke les sommets des triangles en conflit pour ainsi construite
                # des nouveaux triangles respectants delaunay
                pt1, pt2, pt3 = triangle.get_sommet()
                l = [pt1, pt2, pt3]
                for pt in l:
                    if pt not in list_sommets_conflit:
                        list_sommets_conflit.append(pt)

            # list_sommets_conflit = self.recup_sommets(list_triangle_conflit)

            # on trie les sommets dans le sens des auguilles d'une montre
            list_sommets_ordre = clockwise_sorter(list_sommets_conflit, point, clockwise=True)
            # on ajoute le primier point a la fin de la liste ainsi obtenir une boucle fermee
            list_sommets_ordre.append(list_sommets_ordre[0])

            # On onstruire les nouveaux triangles formés en joignant le point à insérer aux arêtes externes de la cavité
            for i in range(len(list_sommets_ordre) - 1):
                new_triangle = Triangle(point, list_sommets_ordre[i], list_sommets_ordre[i + 1])
                self.listTrianglesDelaunay_.append(new_triangle)

    def recup_sommets(self, liste_triangle):
        """cette méthode prend en argument une liste de triangles et retourne la liste
        des sommets de ces triangles sans doublons"""
        sommets = []
        for triangle in liste_triangle:
            pt1, pt2, pt3 = triangle.get_sommet()
            l = [pt1, pt2, pt3]
            for pt in l:
                if pt not in sommets:
                    sommets.append(pt)
        return sommets

    def finalisation(self):
        """Cette méthode permet de retirer de la triangulation les 4 points qui
        ont été rajoutés afin de débuter la triangulation"""
        for pt in self.enConvexe_:  # on parcourt les points de l'enveloppe
            for triangle in self.mise_a_jour():
                pt1, pt2, pt3 = triangle.get_sommet()
                if pt in [pt1, pt2, pt3]:  # si l'un des sommets du triangles est un des points de l'enveloppe convexe
                    self.mise_a_jour().remove(triangle)  # on le retire de la triangulation


    def delaunay_iter(self, point):
        """Cette fonction permet d'ajouter un point et mettre ajour la liste des 
        triangles , elle retourne la liste des triangles"""
        # for point in self.listPoints_:
        self.ajouter_pt(point)

        listTriangleD = self.mise_a_jour()
        
        return listTriangleD
    
    
    def get_voisin_triangle(self, triangle):
        """

        :param triangle:
        :return: la liste des voisins de triangle
        """
        list_voisins = []
        l_arete_en_commun = []

        l_autres_triangles = copy(self.mise_a_jour())
        l_autres_triangles.remove(triangle)

        for arete in triangle.get_arete():
            for autre_triangle in l_autres_triangles:
                for autre_arete in autre_triangle.get_arete():
                   if arete == autre_arete:
                       list_voisins.append(autre_triangle)
                       l_arete_en_commun.append(arete)
        return list_voisins,l_arete_en_commun
    



if __name__ == '__main__':
    filename1 = "points_hasard.dta"
    filename2 = "points.dta"
    filename3 = "points_non_tries.dta"
    filename4 = "set1_10pts.txt"
    filename5 = "set2_30pts.txt"
    filename6 = "set3_50pts.txt"

    delaunaytest = Delaunay(filename6)
    delaunaytest.delaunay_iter(1, 0)
