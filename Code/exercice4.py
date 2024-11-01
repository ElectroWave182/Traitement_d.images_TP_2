import cv2
from numpy import *


def moyenne (pixels):

    nombre = len (pixels)
    
    pixelMoyen = array ([
        round (sum (pixels[:][couleur]) / nombre)
        for couleur in range (3)
    ], dtype = uint8)
    
    return pixelMoyen


def flou1 (image):

    copie = image.copy ()
    hauteur = copie.shape[0]
    largeur = copie.shape[1]
    
    
    for ligne in range (hauteur):
        for colonne in range (largeur):
            pixel = copie[ligne][colonne]
            
            
            # Listage des 5 voisins
            
            voisins = [image[ligne][colonne]]
            
            if ligne != 0:
                voisins.append (image[ligne - 1][colonne])
                
            if ligne != copie.shape[0] - 1:
                voisins.append (image[ligne + 1][colonne])
                
            if colonne != 0:
                voisins.append (image[ligne][colonne - 1])
                
            if colonne != copie.shape[1] - 1:
                voisins.append (image[ligne][colonne + 1])
                
                
            pixel = moyenne (voisins)
            

    return copie


def flou2 (image):

    copie = image.copy ()
    hauteur = copie.shape[0]
    largeur = copie.shape[1]
    
    
    for ligne in range (hauteur):
        for colonne in range (largeur):
            pixel = copie[ligne][colonne]
            
            
            # Listage des 9 voisins
            
            voisins = [image[ligne][colonne]]
            
            if ligne != 0:
                voisins.append (image[ligne - 1][colonne])
                
                if colonne != 0:
                    voisins.append (image[ligne - 1][colonne - 1])
                
            if ligne != copie.shape[0] - 1:
                voisins.append (image[ligne + 1][colonne])
                
                if colonne != copie.shape[1] - 1:
                    voisins.append (image[ligne + 1][colonne + 1])
                
            if colonne != 0:
                voisins.append (image[ligne][colonne - 1])
                
                if ligne != copie.shape[0] - 1:
                    voisins.append (image[ligne + 1][colonne - 1])
                
            if colonne != copie.shape[1] - 1:
                voisins.append (image[ligne][colonne + 1])
                
                if ligne != 0:
                    voisins.append (image[ligne - 1][colonne + 1])


            pixel = moyenne (voisins)
            

    return copie


def flou6 (image):

    copie = image.copy ()
    
    for _ in range (3):
        copie = flou2 (copie)
        
    return copie
