# -*- coding: utf-8 -*-

# **************************************
# definitions de la classe Point
# **************************************

# -*- coding: utf-8 -*-

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
        return str((self.x_, self.y_))

    def __lt__(self, other):
        """

        :param other: Point
        :return: True si le point a tester(other) est plus bas sinon False
        """
        if other.y_ > self.y_:
            return True
        if self.y_ == other.y_:
            if other.x_ > self.x_:
                return True
        return False

    def calcule_angle(self, other):
        """
        calcule l'angle entre l'horisontal et le segment des deux points
        :param other:Pont
        :return: angle
        """

        return (other.x_ - self.x_) / sqrt((other.x_ - self.x_) ** 2 + (other.y_ - self.y_) ** 2)

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

    def __eq__(self, other):
        if self.x_ == other.x_ and self.y_ == other.y_:
            return True
        return False


if __name__ == "__main__":
    pt1 = Point(-1, 3)
    print(pt1)

    pt2 = Point(-1, 3)
    print(pt2)

    print(pt1 == pt2)

    pt3 = Point(5, 7)
    print(pt3)

    print(pt1.__lt__(pt3))
