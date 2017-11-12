#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 12:55:07 2017

@author: victor
"""
import pygame
import time

class Ant(object):
    def __init__(self, x, y):
        pygame.init()
        self.fenetre = pygame.display.set_mode((1000, 1000))
        self.load_picture()
        self.fenetre.blit(self.background, (0,0))
        
        self.x = x
        self.y = y
        self.direction = 0
        self.marks = []

    def load_picture(self):
        #Charge toutes les images 
        self.background = pygame.image.load("images/background.jpg").convert()
        self.fourmie_0 = pygame.image.load("images/fourmie_0.png").convert_alpha()
        self.fourmie_1 = pygame.image.load("images/fourmie_1.png").convert_alpha()
        self.fourmie_2 = pygame.image.load("images/fourmie_2.png").convert_alpha()
        self.fourmie_3 = pygame.image.load("images/fourmie_3.png").convert_alpha()
        self.black = pygame.image.load("images/black.jpg").convert()
        self.write = pygame.image.load("images/write.jpg").convert()
    
    def black_mark(self):
        self.fenetre.blit(self.black, (self.x, self.y))
    
    def write_mark(self):
        self.fenetre.blit(self.write, (self.x, self.y))
        
    def show_ant(self):
        #Afficher la fourmie dans la bonne direction
        #0 = haut, 1 = bas, 2 = droite, 3 = gauche  
        if self.direction == 0:
            self.fenetre.blit(self.fourmie_0, (self.x, self.y))
        elif self.direction == 1:
            self.fenetre.blit(self.fourmie_1, (self.x, self.y))
        elif self.direction == 2:
            self.fenetre.blit(self.fourmie_2, (self.x, self.y))
        elif self.direction == 3:
            self.fenetre.blit(self.fourmie_3, (self.x, self.y))
    
    def color_mark(self):
        #Retourne True sur un marqueur noir et False sur un marque blanc
        for mark in self.marks:
            if (self.x, self.y) == mark:
                return True
        return False
    
    def choose_move(self):
        #Choisi le movement approprie en fonction de color_mark
        color = self.color_mark()
        if color == True:
            #Si marqueur noir
            self.black_move()
        
        elif color == False:
            #Si marqueur blanc
            self.write_move()
    
    def write_move(self):
        #Sur une case blanche la fourmie va vers la droite
        #0 = haut, 1 = bas, 2 = droite, 3 = gauche  
        #Fourmie vers le haut
        if self.direction == 0:
            #La droite est a droite
            self.x = self.x+10
            self.direction = 2
            
        #Fourmie vers le bas
        elif self.direction == 1:
            #La droite est a gauche
            self.x = self.x-10
            self.direction = 3
            
        #Fourmie a  droite
        elif self.direction == 2:
            #La droite est vers le bas
            self.y = self.y+10
            self.direction = 1
            
        #Fourmie a gauche
        elif self.direction == 3:
            #La droite est vers le haut
            self.y = self.y-10
            self.direction = 0
    
    def black_move(self):
        #Sur une case noire la fourmie va vers la gauche
        #0 = haut, 1 = bas, 2 = droite, 3 = gauche  
        #Fourmie vers le haut
        if self.direction == 0:
            #La gauche est a gauche
            self.x = self.x-10
            self.direction = 3
            
        #Fourmie vers le bas
        elif self.direction == 1:
            #La gauche est a droite
            self.x = self.x+10
            self.direction = 2
            
        #Fourmie a  droite
        elif self.direction == 2:
            #La gauche est vers le haut
            self.y = self.y-10
            self.direction = 0
            
        #Fourmie a gauche
        elif self.direction == 3:
            #La droite est vers le bas
            self.y = self.y+10
            self.direction = 1
    
    def edite_mark(self):
        #Ajoute ou supprime une marque en fonction de color mark
        color = self.color_mark()
        if color == True:
            #Marqueur noir
            self.marks.remove((self.x, self.y))
            self.write_mark()
            
        elif color == False:
            #Marqueur blanc
            self.marks.append((self.x, self.y))
            self.black_mark()
            
if __name__ == "__main__":
    ant = Ant(300, 300)
    t = 0
    while True:
        t+=1
        print t
        ant.edite_mark()
        ant.choose_move()
        ant.show_ant()
        pygame.display.flip()
        time.sleep(0.001)
        

    
