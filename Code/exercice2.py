import cv2


def monochrome (image, couleurVoulue):

    couleurs = ["bleu", "vert", "rouge"]
    numCouleur = couleurs.index (couleurVoulue)
    couleursModifiees = list (range (3))
    del couleursModifiees[numCouleur]

    copie = image.copy ()
    hauteur = copie.shape[0]
    largeur = copie.shape[1]
    
    for ligne in range (hauteur):
        for colonne in range (largeur):
            pixel = copie[ligne][colonne]

            for couleur in couleursModifiees:
                pixel[couleur] = 0

    return copie


def echanger (image, source, destination):

    couleurs = ["bleu", "vert", "rouge"]
    numSource = couleurs.index (source)
    numDestination = couleurs.index (destination)

    copie = image.copy ()
    hauteur = copie.shape[0]
    largeur = copie.shape[1]
    
    for ligne in range (hauteur):
        for colonne in range (largeur):
            pixel = copie[ligne][colonne]
            pixel[numDestination], pixel[numSource] = pixel[numSource], pixel[numDestination]

    return copie
