# -*- coding:utf-8 -*-

__nom_fichier__ = "trace_courbe_liste"
__author__ = "fay7"
__date__ = "novembre 2016"

import matplotlib.pyplot as plt


def trace_courbe_liste(liste_points):
    """

    :param segments: liste de points (x, y)
    :return:         affiche la courbe représentée par les points de la liste des segments
    """

    segments = []
    for i in range(-1, len(liste_points) - 1):
        pt1 = ((liste_points[i].getx(), liste_points[i].gety()))
        pt2 = ((liste_points[i + 1].getx(), liste_points[i + 1].gety()))

        segments.append((pt1, pt2))

    plt.figure()
    for (a,b) in segments:
        plt.plot([a[0], b[0]], [a[1], b[1]])
    plt.show()

