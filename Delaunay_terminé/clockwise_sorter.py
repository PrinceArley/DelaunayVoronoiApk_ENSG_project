# -*- coding:utf-8 -*-
__projet__ = "Ensginfo"
__nom_fichier__ = "clockwise_sorter"
__author__ = "mon_Prénom mon_Nom"
__date__ = "December 2021"

# Imports
from functools import reduce
import operator
from math import atan2
from point import *
from Nuage import *
import matplotlib.pyplot as plt


def argsort(seq):
    # http://stackoverflow.com/questions/3382352/equivalent-of-numpy-argsort-in-basic-python/3382369#3382369
    # by unutbu
    # https://stackoverflow.com/questions/3382352/equivalent-of-numpy-argsort-in-basic-python
    # from Boris Gorelik
    return sorted(range(len(seq)), key=seq.__getitem__)


def rotational_sort(list_of_pts, centre_of_rotation, clockwise=True):
    """
    tries une liste de coordonnees (x,y) dans le sens des aiguilles d'une montre ou contriare suivant un point pivot
    :param liste: liste originalee
    :return: une liste triee
    """
    # convertit les points en coord cartesiennes
    centre_of_rotation_xy_coord = centre_of_rotation.getx(), centre_of_rotation.gety()

    list_of_xy_coords = []
    for point in list_of_pts:
        list_of_xy_coords.append((point.getx(), point.gety()))

    cx, cy = centre_of_rotation_xy_coord
    angles = [atan2(x - cx, y - cy) for x, y in list_of_xy_coords]
    indices = argsort(angles)
    if clockwise:
        return [list_of_xy_coords[i] for i in indices]
    else:
        return [list_of_xy_coords[i] for i in indices[::-1]]


def clockwise_sorter(list_of_pts, centre_of_rotation, clockwise=True):
    """
    tries une liste des instances de la class Point dans le sens des aiguilles d'une montre ou contriare suivant un point pivot
    :param list_of_pts:
    :param centre_of_rotation:
    :param clockwise: bol
    :return:
    """

    liste_coord_sorted = rotational_sort(list_of_pts, centre_of_rotation, clockwise=True)
    liste_pt_sorted = []
    for coord in liste_coord_sorted:
        x, y = coord
        liste_pt_sorted.append(Point(x, y))

    return liste_pt_sorted


if __name__ == '__main__':
    pts = [Point(2, 3), Point(5, 2), Point(4, 1), Point(3.5, 1), Point(1, 2), Point(2, 1), Point(3, 1), Point(3, 3),
           Point(4, 3)]

    l_x = [pt.getx() for pt in pts]
    l_y = [pt.gety() for pt in pts]

    l = clockwise_sorter(pts, Point(3, 2))
    for pt in l:
        print(pt)

    plt.plot(l_x, l_y, "o")

    # plt.show()
