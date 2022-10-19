# -*- coding: utf-8 -*-

# **************************************
# definitions de la classe Point
# **************************************

# -*- coding: utf-8 -*-

#Imports
from math import sqrt


class Point:
    """ Definit les points de l'espace 2D.
        chaque point a pour attribus une abcisse x et une ordonne y

        """

    def __init__(self, x=0, y=0):
        """

        @param x: abscisse du point
        @param y: ordonnée du point
        """
        self.x_ = x
        self.y_ = y


    def __str__(self):
        """

        @return:  chaine permettant d'afficher les attributs d'un point
        """
        return str((self.x_,self.y_))


    def __lt__(self, other):
        """

        @param autre_point:     autre_point point
        @return:                True si le point est plus en bas ou plus à gauche que le second point
        """

        if self.y_ < other.y_:
            return True

        elif self.y_ == other.y_:
            return self.x_ < other.x_

        return False

        # format avec opérateurs ternaires
        # return True if self.y_ < autre_point.y_ else False if self.y_ < autre_point.y_ else self.x_<autre_point.x_


    def calcule_angle(self, other):
        """

        @param other:   point de référence plus bas et plus à gauche que tous les autres points
        @return:         l'angle entre l'horizontale passant par ancre
                        et le segment (ancre - self )
                        l'angle est en fait représenté par son cosinus
        """
        if self.y_==other.y_:
            # on évite une division par 0
            return 1
        if self.x_==other.x_:
            # on évite une division par 0
            return 0

        den = (self.x_ - other.x_) ** 2 + (self.y_ - other.y_) ** 2
        angle = (self.x_ - other.x_) / sqrt(den)

        return angle


    def getx(self):
        """ Accesseur pour x_

        @return:     attribut x_
        """
        return self.x_


    def gety(self):
        """ Accesseur pour y_

        @return:     attribut y_
        """
        return self.y_


    def distance(self, other):
        """
        calcule la distance entre deux points
        :param other: autre point
        :return: float
        """
        return sqrt((self.x_ - other.x_)**2 + (self.y_ - other.y_)**2)


if __name__=="__main__":
    pt1 = Point(2, 3)
    print(pt1)

    pt2 = Point(-1, 3)
    print(pt2)

    pt3 = Point(5, 7)
    print(pt3)

    print(pt1.calcule_angle(pt2))
    print(pt1.__lt__(pt3))