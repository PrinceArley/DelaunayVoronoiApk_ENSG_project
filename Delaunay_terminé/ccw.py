# -*- coding: iso-8859-1 -*-

# *******************************
def ccw (point1, point2, point3):
# *******************************

# fonction qui calcule si pour passer du point1, au point2
# puis au point3 on tourne dans le sens des aiguilles d'une montre (-1)
# ou dans le sens contraire des aiguilles d'une montre (1) 
# rend 0 s'ils sont sur la meme ligne */
# ccw : counterclockwise */

    dx1 = point2.getx() - point1.getx() ;		#  dy/dx : pente de la droite 
    dy1 = point2.gety() - point1.gety() ;
    dx2 = point3.getx() - point1.getx() ;
    dy2 = point3.gety() - point1.gety() ;

    if (dx1*dy2 > dy1*dx2):
        return +1
    if (dx1*dy2 < dy1*dx2):
        return -1
    if (dx1*dx2 < 0 or dy1*dy2 < 0):
        return -1
    if ((dx1*dx1 + dy1*dy1) < (dx2*dx2 + dy2*dy2)):
        return +1
    return 0

