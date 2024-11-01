import cv2
from pathlib import Path
from matplotlib import pyplot

from exercice1 import *
from exercice2 import *
from exercice3 import *
from exercice4 import *


def main ():

    # Read images

    cheminImages = str (Path (__file__).resolve ().parent) + "/images/"
    
    cercles = cv2.imread (cheminImages + "circles_in_a_circle.jpg")
    lena = cv2.imread (cheminImages + "lena.jpg")
    lenaBruitBinaire1 = cv2.imread (cheminImages + "lena_sp1.png")
    lenaBruitBinaire2 = cv2.imread (cheminImages + "lena_sp2.png")
    lenaBruitGauss1 = cv2.imread (cheminImages + "lena_gauss1.jpg")
    lenaBruitGauss2 = cv2.imread (cheminImages + "lena_gauss2.jpg")


    # Treat them
    
    # Exercice 1

    cerclesInverse = inverseCouleurs (cercles)
    lenaInverse = inverseCouleurs (lena)
    lenaInverseGris = cv2.cvtColor (lenaInverse, cv2.COLOR_BGR2GRAY)
    
    
    # Exercice 2
    
    cerclesBleu = monochrome (cercles, "bleu")
    cerclesVert = monochrome (cercles, "vert")
    cerclesRouge = monochrome (cercles, "rouge")

    lenaBleu = monochrome (lena, "bleu")
    lenaVert = monochrome (lena, "vert")
    lenaRouge = monochrome (lena, "rouge")

    lenaBleuNivGris = cv2.cvtColor (lenaBleu, cv2.COLOR_BGR2GRAY)
    lenaVertNivGris = cv2.cvtColor (lenaVert, cv2.COLOR_BGR2GRAY)
    lenaRougeNivGris = cv2.cvtColor (lenaRouge, cv2.COLOR_BGR2GRAY)

    """
    Résultats des tests Photopea :
    rouge -> vert
    vert -> bleu
    bleu -> rouge
    """
    cerclesChelou = echanger (echanger (cercles, "rouge", "vert"), "rouge", "bleu")
    
    
    # Exercice 3
    
    cerclesNoirBlanc0 = binaire (cercles, 0)
    cerclesNoirBlanc64 = binaire (cercles, 64)
    cerclesNoirBlanc128 = binaire (cercles, 128)
    cerclesNoirBlanc192 = binaire (cercles, 192)
    cerclesNoirBlanc256 = binaire (cercles, 256)
    
    cerclesGris = cv2.cvtColor (cercles, cv2.COLOR_BGR2GRAY)
    cerclesBinaires = cv2.threshold (cerclesGris, 127, 255, cv2.THRESH_BINARY)
    
    
    # Exercice 4
    
    lenaFlou = flou1 (lena)
    lenaFlouflou = flou2 (lena)
    lenaTropFlou = flou6 (lena)
    
    lbb1FlouMoyen = cv2.blur (lenaBruitBinaire1, (10, 10))
    lbb2FlouMoyen = cv2.blur (lenaBruitBinaire2, (10, 10))
    lbg1FlouMoyen = cv2.blur (lenaBruitGauss1, (10, 10))
    lbg2FlouMoyen = cv2.blur (lenaBruitGauss2, (10, 10))
    
    lbb1FlouGaussien = cv2.GaussianBlur (lenaBruitBinaire1, (9, 9), cv2.BORDER_DEFAULT)
    lbb2FlouGaussien = cv2.GaussianBlur (lenaBruitBinaire2, (9, 9), cv2.BORDER_DEFAULT)
    lbg1FlouGaussien = cv2.GaussianBlur (lenaBruitGauss1, (9, 9), cv2.BORDER_DEFAULT)
    lbg2FlouGaussien = cv2.GaussianBlur (lenaBruitGauss2, (9, 9), cv2.BORDER_DEFAULT)
    
    lbb1FlouMedian = cv2.medianBlur (lenaBruitBinaire1, 9)
    lbb2FlouMedian = cv2.medianBlur (lenaBruitBinaire2, 9)
    lbg1FlouMedian = cv2.medianBlur (lenaBruitGauss1, 9)
    lbg2FlouMedian = cv2.medianBlur (lenaBruitGauss2, 9)
    
    matriceFiltre = list ()
    matriceFiltre.append ([0   , -0.5, 0   ])
    matriceFiltre.append ([-0.5, 3   , -0.5])
    matriceFiltre.append ([0   , -0.5, 0   ])
    matriceFiltre = array (matriceFiltre)
    
    lbb1Filtre2D = cv2.filter2D (lenaBruitBinaire1, -1, matriceFiltre)
    lbb2Filtre2D = cv2.filter2D (lenaBruitBinaire2, -1, matriceFiltre)
    lbg1Filtre2D = cv2.filter2D (lenaBruitGauss1, -1, matriceFiltre)
    lbg2Filtre2D = cv2.filter2D (lenaBruitGauss2, -1, matriceFiltre)


    # Show result
    
    nbLignes = 5
    nbColonnes = 9
    position = 1
    
    # Exercice 1

    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (lenaInverseGris, cmap = "gray", vmin = 0, vmax = 255)
    pyplot.title ("1.1)")
    position += 1

    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (cerclesInverse, cv2.COLOR_BGR2RGB))
    pyplot.title ("1.2)")
    position += 1
    
    
    # Exercice 2
    
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (lenaBleuNivGris, cmap = "gray", vmin = 0, vmax = 255)
    pyplot.title ("2.1) bleu")
    position += 1

    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (lenaVertNivGris, cmap = "gray", vmin = 0, vmax = 255)
    pyplot.title ("2.1) vert")
    position += 1

    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (lenaRougeNivGris, cmap = "gray", vmin = 0, vmax = 255)
    pyplot.title ("2.1) rouge")
    position += 1

    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (lenaBleu, cv2.COLOR_BGR2RGB))
    pyplot.title ("2.2) bleu")
    position += 1

    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (lenaVert, cv2.COLOR_BGR2RGB))
    pyplot.title ("2.2) vert")
    position += 1

    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (lenaRouge, cv2.COLOR_BGR2RGB))
    pyplot.title ("2.2) rouge")
    position += 1

    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (cerclesChelou, cv2.COLOR_BGR2RGB))
    pyplot.title ("2.3)")
    position += 1
    
    
    # Exercice 3
    
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (cerclesNoirBlanc0, cv2.COLOR_BGR2RGB))
    pyplot.title ("3.1) seuil à 0")
    position += 1
    
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (cerclesNoirBlanc64, cv2.COLOR_BGR2RGB))
    pyplot.title ("3.1) seuil à 64")
    position += 1
    
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (cerclesNoirBlanc128, cv2.COLOR_BGR2RGB))
    pyplot.title ("3.1) seuil à 128")
    position += 1
    
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (cerclesNoirBlanc192, cv2.COLOR_BGR2RGB))
    pyplot.title ("3.1) seuil à 192")
    position += 1
    
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (cerclesNoirBlanc256, cv2.COLOR_BGR2RGB))
    pyplot.title ("3.1) seuil à 256")
    position += 1
    
    """
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cerclesBinaires, cmap = "gray", vmin = 0, vmax = 255)
    pyplot.title ("3.2)")
    position += 1
    """
    
    
    # Exercice 4
    
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (lenaFlou, cv2.COLOR_BGR2RGB))
    pyplot.title ("4.1)")
    position += 1
    
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (lenaFlouflou, cv2.COLOR_BGR2RGB))
    pyplot.title ("4.2)")
    position += 1
    
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (lenaTropFlou, cv2.COLOR_BGR2RGB))
    pyplot.title ("4.3)")
    position += 1
    
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (lbb1FlouMoyen, cv2.COLOR_BGR2RGB))
    pyplot.title ("4.4) Bruit binaire 1")
    position += 1
    
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (lbb2FlouMoyen, cv2.COLOR_BGR2RGB))
    pyplot.title ("4.4) Bruit binaire 2")
    position += 1
    
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (lbg1FlouMoyen, cv2.COLOR_BGR2RGB))
    pyplot.title ("4.4) Bruit gaussien 1")
    position += 1
    
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (lbg2FlouMoyen, cv2.COLOR_BGR2RGB))
    pyplot.title ("4.4) Bruit gaussien 2")
    position += 1
    
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (lbb1FlouGaussien, cv2.COLOR_BGR2RGB))
    pyplot.title ("4.5) Bruit binaire 1")
    position += 1
    
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (lbb2FlouGaussien, cv2.COLOR_BGR2RGB))
    pyplot.title ("4.5) Bruit binaire 2")
    position += 1
    
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (lbg1FlouGaussien, cv2.COLOR_BGR2RGB))
    pyplot.title ("4.5) Bruit gaussien 1")
    position += 1
    
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (lbg2FlouGaussien, cv2.COLOR_BGR2RGB))
    pyplot.title ("4.5) Bruit gaussien 2")
    position += 1
    
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (lbb1FlouMedian, cv2.COLOR_BGR2RGB))
    pyplot.title ("4.6) Bruit binaire 1")
    position += 1
    
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (lbb2FlouMedian, cv2.COLOR_BGR2RGB))
    pyplot.title ("4.6) Bruit binaire 2")
    position += 1
    
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (lbg1FlouMedian, cv2.COLOR_BGR2RGB))
    pyplot.title ("4.6) Bruit gaussien 1")
    position += 1
    
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (lbg2FlouMedian, cv2.COLOR_BGR2RGB))
    pyplot.title ("4.6) Bruit gaussien 2")
    position += 1
    
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (lbb1Filtre2D, cv2.COLOR_BGR2RGB))
    pyplot.title ("4.7) Bruit binaire 1")
    position += 1
    
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (lbb2Filtre2D, cv2.COLOR_BGR2RGB))
    pyplot.title ("4.7) Bruit binaire 2")
    position += 1
    
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (lbg1Filtre2D, cv2.COLOR_BGR2RGB))
    pyplot.title ("4.7) Bruit gaussien 1")
    position += 1
    
    pyplot.subplot (nbLignes, nbColonnes, position)
    pyplot.imshow (cv2.cvtColor (lbg2Filtre2D, cv2.COLOR_BGR2RGB))
    pyplot.title ("4.7) Bruit gaussien 2")
    position += 1
    
    
    pyplot.show ()


main ()
