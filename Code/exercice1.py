import cv2


def inverseCouleurs (image):

    copie = image.copy ()
    hauteur = copie.shape[0]
    largeur = copie.shape[1]
    
    for ligne in range (hauteur):
        for colonne in range (largeur):
            pixel = copie[ligne][colonne]

            for couleur in range (3):
                pixel[couleur] = 255 - pixel[couleur]

    return copie
