import pygame  # necessaire pour charger les images et les sons
import random

class joueur() : # classe pour créer le vaisseau du joueur
    def __init__(self) :
        self.position = 475
        self.image = pygame.image.load("vaisseau.png")
        self.sens = "O"
        self.vitesse = 2
        self.score=0

    def deplacer(self) :
        if (self.sens == "droite") and (self.position < 930):
            self.position = self.position + self.vitesse
        elif (self.sens == "gauche") and (self.position > 0):
           self.position = self.position - self.vitesse
    def tirer(self):
        self.sens = "O"
    def marquer():
        if Balle.toucher(Ennemi):
            self.score+=1
        
class Balle() :
    def __init__(self, tireur):
        self.tireur = tireur
        self.depart = tireur.position + 16
        self.hauteur = 492
        self.image = pygame.image.load("balle.png")
        self.etat = "chargee"
    
    def bouger(self):
        if self.etat == "attente":
            self.depart = self.tireur.position + 16
            self.hauteur = 492
        elif self.etat == "tiree" :
            self.hauteur = self.hauteur - 5
        
        if self.hauteur < 0:
            self.etat = "chargee"
    def toucher(Ennemi,joueur):
        if self.hauteur==Ennemi.hauteur:
            self.hauteur=492
            self.etat="chargee"
        
class Ennemi():
    NbEnnemis = 6
    
    def __init__(self):
        self.depart = random.randint(1,700)
        self.hauteur = 10
        self.type = random.randint(1,2)
        if  (self.type == 1):
            self.image = pygame.image.load("invader1.png")
            self.vitesse = 1
        elif (self.type ==2):
            self.image = pygame.image.load("invader2.png")
            self.vitesse = 2
            
    def avancer(self):
        self.hauteur = self.hauteur + self.vitesse
    def disparaitre(self):
        if Balle.hauteur==self.hauteur:
            self.depart = random.randint(60,663)
    

