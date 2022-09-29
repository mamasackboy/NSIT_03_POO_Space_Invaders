import pygame  # necessaire pour charger les images et les sons
import random
import math

class joueur() : # classe pour créer le vaisseau du joueur
    def __init__(self) :
        self.position = 475
        self.image = pygame.image.load("vaisseau.png")
        self.sens = "O"
        self.vitesse = 5
        self.score=0
        self.lives=3
    def deplacer(self) :
        if (self.sens == "droite") and (self.position < 930):
            self.position = self.position + self.vitesse
        elif (self.sens == "gauche") and (self.position > 0):
           self.position = self.position - self.vitesse
    def tirer(self):
        self.sens = "O"
    def marquer(self):
        self.score+=1
        
class Balle() :
    def __init__(self, tireur):
        self.tireur = tireur
        self.depart = tireur.position + 16
        self.hauteur = 492
        self.image = pygame.image.load("balle.png")
        self.etat = "chargee"
        self.vitesse=8
    
    def bouger(self):
        if self.etat == "chargee":
            self.depart = self.tireur.position + 16
            self.hauteur = 492
        elif self.etat == "tiree" :
            self.hauteur = self.hauteur - self.vitesse
        if self.hauteur < 0:
            self.etat = "chargee"

    def toucher(self,vaisseau,player):
        if (math.fabs(self.depart - vaisseau.depart) < 40) and (math.fabs(self.hauteur - vaisseau.hauteur) < 40):
            return True
        else:
            if (math.fabs(self.depart - vaisseau.depart) < 40) and (math.fabs(self.hauteur - vaisseau.hauteur) < 40):
                vaisseau.disparaitre()
                player.score -= 1

        
class Ennemi():
    NbEnnemis = 9
    
    def __init__(self):
        self.depart = random.randint(1,700)
        self.hauteur = 10
        self.type = random.randint(1,4)
        if  (self.type == 1):
            self.image = pygame.image.load("invader1.png")
            self.vitesse = 0.5
        elif (self.type ==2):
            self.image = pygame.image.load("invader2.png")
            self.vitesse = 1
        elif (self.type ==3):
            self.image = pygame.image.load("invader3.png")
            self.vitesse = 1.5
        elif (self.type ==4):
            self.image = pygame.image.load("invader4.png")
            self.vitesse = 2
            
    def avancer(self):
        self.hauteur = self.hauteur + self.vitesse
    def disparaitre(self):
        self.depart = random.randint(1, 700)
        self.hauteur = 10
        self.type = random.randint(1, 4)
        if self.type == 1:
            self.image = pygame.image.load('invader1.png')
            self.vitesse = 0.75
        elif self.type == 2:
            self.image = pygame.image.load('invader2.png')
            self.vitesse = 2
        elif self.type == 3:
            self.image = pygame.image.load('invader3.png')
            self.vitesse = 1
        elif self.type == 3:
            self.image = pygame.image.load('invader4.png')
            self.vitesse = 1.5

    

