# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 20:47:03 2021

@author: Elysio
"""

# Imports
from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from Triangle import *
from Delaunay_Copy import *

# On verrifie que PyQt5 est bien backend
matplotlib.use('QT5Agg')


# on crée la ckass canvas
class MplCanvas(Canvas):
    def __init__(self):
        """on initialise le canvas avec une figure dont les axes sont à la même échelle"""
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)
        self.ax.set_aspect(1)

    def MplTriangle(self, triangle,couleur):
        """Cette methode prend en argument un class Triangle récupère ses aretes
        et appelle la fonction MplArete pour les dessiner"""
        self.a1 = triangle.arete1_
        self.a2 = triangle.arete2_
        self.a3 = triangle.arete3_
        self.MplArete(self.a1,couleur)
        self.MplArete(self.a2,couleur)
        self.MplArete(self.a3,couleur)

    def MplSet(self, delaunay):
        """cette fonction prend en argument une triangulation de delaunay
        et recupère la liste des points, puis plot chacun de ces points
        sur l'axe"""
        for pt in delaunay.listPoints_:
            x, y = pt.x_, pt.y_
            self.ax.plot(x, y, 'bo')

    def MplArete(self, arete, couleur, mark = None ):
        """cette méthode prend en argument une arete et ajoute sur l'axe
        le plot des segments relient le point1 au point 2"""
        pt1 = arete.pt1_
        pt2 = arete.pt2_
        self.ax.plot([pt1.x_, pt2.x_], [pt1.y_, pt2.y_], couleur)

    def MplCercle(self, triangle, couleur):
        """Cette méthode prend en argument un triangle et une couleur
        elle dessine le cercle de la couleur fournie"""
        if triangle.get_centreCercle() != "pas de centre":
            x, y = triangle.centreCercle_.getx(), triangle.centreCercle_.gety()
            rayon = triangle.rayonCercle_
            Drawing = plt.Circle((x, y), rayon, fill=False, color=couleur)
            self.ax.add_artist(Drawing)

    def MplEffacer(self):
        """Cette méthode efface le contenu de l'axe"""
        self.ax.cla()

    def MplSave(self, nomImage):
        """Cette méthode prend en argument un Str et sauvegarde le canvas"""
        self.fig.savefig(nomImage, transparent=True)
        
        
    def MplCentre(self,delaunay):
        for triangle in delaunay.listTrianglesDelaunay_:

            centre = triangle.get_centreCercle()
            self.ax.plot(centre.x_, centre.y_,'o',color ='k' )


# Matplotlib widget
class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.canvas = MplCanvas()
        self.vbl = QtWidgets.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

    def redraw(self):
        """Cette méthode dessine le contenu du canvas"""
        self.canvas.draw()

    def plot_triangle(self, Triangle,couleur):
        """cette méthode appelle la méthode de la classe MplCanvas pour 
        dessiner un triangle"""
        self.canvas.MplTriangle(Triangle,couleur)

    def plot_cercle(self, triangle, couleur):
        """Cette méthode appelle la méthode de la classe MplCanvas pour
        dessiner les cercles"""
        self.canvas.MplCercle(triangle, couleur)

    def plot_set(self, delaunay):
        """Cette méthode appelle la méthode de la classe MplCanvas pour
        dessiner un set de point"""
        self.canvas.MplSet(delaunay)

    def effacer(self):
        """Cette méthode fait appel à la méthode de la classe MplCanvas pour
        effacer le contenu du canvas"""
        self.canvas.MplEffacer()

    def plot_save(self, nomImage):
        """Cette méthode fait appel à la méthode de la classe MplCanvas pour
        sauvegarder une image"""
        self.canvas.MplSave(nomImage)
        
    
    def plot_arete(self,arete,couleur):
        self.canvas.MplArete(arete,couleur)
        
        
    def plot_centre(self,delaunay):
        self.canvas.MplCentre(delaunay)