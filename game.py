# Pour utiliser le robot de Clara, on doit télécharger PYGAME
# Outils > Gérer les paquets > chercher pygame > l'installer

import robot # Cette ligne permet d' "importer" robot.py, le code de Clara ! (Tu peux y jeter un oeil mais il est très compliqué !)

robot.allumer(5) # Cette ligne permet de lancer le jeu. Le chiffre correspond au niveau : 1 à 5.

# Et maintenant, c'est à toi de jouer :)
# Tu dois faire sortir le robot par la porte.
# Ci-dessous, toutes les "fonctions" que tu peux utiliser !

# Les déplacements :
#   robot.avancer("haut")  => remplacer "haut" par "bas", "droite", "gauche"
# Les conditions :
#   robot.haut() => équivaut à "libre" si la case est libre, sinon "bloquée"


# tu peux aussi utiliser des conditions !
# exemple :
if robot.haut() == "libre": # Si la case du haut est libre, alors...
    robot.avancer("haut")


  
# et pour finir, tu peux utiliser les boucles !
# exemple :
while robot.haut() == "libre": # Aussi longtemps que la case du haut sera bloquée, alors...
    robot.avancer("haut")
while robot.haut() == "bloqué" and robot.droite() == "libre":
    robot.avancer("droite")
while robot.bas() == "libre":
    robot.avancer("bas")
while robot.haut() == "bloqué" and robot.droite() == "libre":
    robot.avancer("droite")
while robot.droite() == "libre":
    robot.avancer("droite")
while robot.haut() == "bloqué" and robot.droite() == "libre":
    robot.avancer("haut")
while robot.haut() == "libre":
    robot.avancer("haut")
while robot.gauche() == "bloqué" and robot.gauche() == "libre":
    robot.avancer("gauche")
while robot.gauche() == "libre":
    robot.avancer("gauche")
while robot.haut() == "libre":
    robot.avancer("haut")
while robot.haut() == "bloqué" and robot.droite() == "libre":
    robot.avancer("droite")
while robot.haut() == "libre":
    robot.avancer("haut")
    
        

   
# A toi de jouer !
# Ecris un script le plus court possible qui fasse sortir le robot du labyrinthe *^-^*
# Attention : aux niveau 4 et 5, tu n'as plus le droit de te cogner !



