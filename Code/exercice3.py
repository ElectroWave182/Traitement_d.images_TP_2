import cv2


def binaire (image, seuil):

    gris = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)
    hauteur = gris.shape[0]
    largeur = gris.shape[1]
    
    for ligne in range (hauteur):
        for colonne in range (largeur):
            pixel = gris[ligne][colonne]
            
            if pixel < seuil:
                gris[ligne][colonne] = 0
            else:
                gris[ligne][colonne] = 255

    return gris
