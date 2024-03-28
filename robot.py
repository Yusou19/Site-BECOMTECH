# Import de SYS, bibliothèque classique
# Import de PYGAME, la bibliothèque de jeu
import sys, pygame

# Definition d'une classe globale
# Une classe peut etre vue comme un "objet" avec des "propriétés"
# Ou simplement comme une bibliothèque de variables qu'on veut pouvoir appeler partout
class myGame():
    # initialisation des variables globales
    posrobot,xyrobot,screen,niveau,victoire = 0,0,0,0,0
    ground=[]
    # chargement des ressources graphiques pour pouvoir les utiliser plus tard
    robot = pygame.image.load("perso.png")
    blur  = pygame.image.load("blur.png")
    tile1 = pygame.image.load("tile1.png")
    tile2 = pygame.image.load("tile2.png")
    tile3 = pygame.image.load("tile3.png")
    tile4 = pygame.image.load("tile4.png")
    tile5 = pygame.image.load("tile5.png")
    tile6 = pygame.image.load("tile6.png")
    tile7 = pygame.image.load("tile7.png")
    tile8 = pygame.image.load("tile8.png")
    tile0 = pygame.image.load("tile0.png")
    tile31= pygame.image.load("tile31.png")
    tile32= pygame.image.load("tile32.png")
    tile40= pygame.image.load("tile40.png")
    tile41= pygame.image.load("tile41.png")
    tile42= pygame.image.load("tile42.png")
    tile43= pygame.image.load("tile43.png")
    door  = pygame.image.load("door.png")
    aie   = pygame.image.load("aie.png")
    shadow= pygame.image.load("shadow.png")
    tree1 = pygame.image.load("tree1.png")
    win1  = pygame.image.load("win1.png")
    win2  = pygame.image.load("win2.png")
    win3  = pygame.image.load("win3.png")
    win4  = pygame.image.load("win4.png")
    win5  = pygame.image.load("win5.png")
    over  = pygame.image.load("over.png")
    light = pygame.image.load("light.png")
    
    

# Fonction pour allumer le robot (et le jeu)
def allumer(niveau):
    # initialisation du jeu
    pygame.init()
    
    # définition de la taille de la fenêtre et création de celle ci
    size = width, height = 640, 640
    myGame.screen = pygame.display.set_mode(size)

    # position de départ du robot (de 0,0 à 7,7 = 64 cases, de 80 pixels de côté)
    if niveau == 1:
        myGame.xyrobot = [4,7]
    if niveau == 2:
        myGame.xyrobot = [5,7]        
    if niveau == 3:
        myGame.xyrobot = [2,7]
    if niveau == 4:
        myGame.xyrobot = [4,7]
    if niveau == 5:
        myGame.xyrobot = [1,7]
    myGame.posrobot = pygame.Rect(myGame.xyrobot[0]*80, (myGame.xyrobot[1]*80)-35, 80, 80) # le robot est 35 px au dessus de sa position réelle
    
    # enregistrement du niveau demandé
    myGame.niveau = niveau
    
    # affichage du niveau (arrière plan)
    drawniveau(niveau)
    
    # affichage du robot
    myGame.screen.blit(myGame.robot, myGame.posrobot)
    
    # affichage du premier plan
    drawfront(myGame.niveau)
    
    # on actualise l'affichage
    pygame.display.flip()
    
    
# On avance le robot (et le jeu)
def avancer(direction):
    # Si la victoire n'est toujours pas remportée...
    if myGame.victoire == 0:
        # 1 seconde = 1000 ms entre chaque déplacement
        pygame.time.wait(1000)
        # Cette variable déterminera si on se cogne ou pas
        cogne = 0
        # Cette variable archive la position avant le déplacement
        oldxy = myGame.xyrobot[:];
        
        # Selon la direction choisie, le sens du mouvement change
        if direction == "haut":
            myGame.xyrobot[1] = myGame.xyrobot[1] - 1
        if direction == "bas":
            myGame.xyrobot[1] = myGame.xyrobot[1] + 1
        if direction == "droite":
            myGame.xyrobot[0] = myGame.xyrobot[0] + 1
        if direction == "gauche":
            myGame.xyrobot[0] = myGame.xyrobot[0] - 1
            
        # la case visée existe-t-elle ? (si non on se cogne et on rollback)
        if myGame.xyrobot[0] > 7 or myGame.xyrobot[0] < 0 or myGame.xyrobot[1] > 7 or myGame.xyrobot[1] < 0:
            myGame.xyrobot = oldxy[:]
            cogne = 1
        # la case visée est-elle prise ? (si oui on se cogne et on rollback)
        elif myGame.ground[myGame.xyrobot[1]][myGame.xyrobot[0]] > 5:
            myGame.xyrobot = oldxy[:]
            cogne = 1
        
        # on recalcule la position du personnage
        x = myGame.xyrobot[0]*80
        y = (myGame.xyrobot[1]*80)-35
        myGame.posrobot = pygame.Rect(x, y, 80, 80)
        
        # On actualise l'affichage : d'abord le niveau
        drawniveau(myGame.niveau)
            
        # On affiche le robot
        myGame.screen.blit(myGame.robot, myGame.posrobot)
        
        # On affiche le premier plan
        drawfront(myGame.niveau)
        
        # Si on s'est cogné, on ajoute le texte "Aie!"
        if cogne == 1:
            myGame.screen.blit(myGame.aie, pygame.Rect(x, y-40, 80, 40))
            if myGame.niveau > 3:
                myGame.victoire = 2
                
        # on actualise l'affichage
        pygame.display.flip()
        
        # Si la joueuse a réussi à atteindre la case "victoire", elle gagne ! Youpi !
        if myGame.xyrobot[0] == 4 and myGame.xyrobot[1] == 0:
            myGame.victoire = 1
    
    # Et du coup puisque victoire = 1, on peut afficher le texte de victoire
    if myGame.victoire == 1:
        ressource = 0
        if myGame.niveau == 1:
            ressource = myGame.win1
        if myGame.niveau == 2:
            ressource = myGame.win2
        if myGame.niveau == 3:
            ressource = myGame.win3
        if myGame.niveau == 4:
            ressource = myGame.win4
        if myGame.niveau == 5:
            ressource = myGame.win4
        myGame.screen.blit(ressource, pygame.Rect(0, 0, 640, 640))
        pygame.display.flip()
        
    if myGame.victoire == 2:   
        myGame.screen.blit(myGame.over, pygame.Rect(0, 0, 640, 640))
        pygame.display.flip()
        
# Affiche le décor et les tiles
def drawniveau(niveau):
    # 1-5 are grass
    if niveau == 1:
        myGame.ground = [[6,7,6,31,0,32,6,2],
                         [4,5,8,4,1,1,2,6],
                         [1,4,6,2,2,1,3,8],
                         [2,3,8,5,5,4,3,6],
                         [6,7,6,5,1,4,2,8],
                         [8,4,3,2,2,3,1,6],
                         [6,2,1,5,1,2,4,8],
                         [2,6,7,6,2,6,7,6]]

    if niveau == 2:
        myGame.ground = [[6,7,6,31,0,32,6,2],
                         [4,2,3,6,1,1,2,6],
                         [1,40,42,2,6,1,3,8],
                         [2,41,43,3,8,4,3,6],
                         [6,7,6,7,6,4,2,8],
                         [8,4,3,2,2,3,1,6],
                         [6,2,1,5,1,2,4,8],
                         [6,7,6,7,6,2,6,6]]
        
    if niveau == 3:
        myGame.ground = [[6,7,6,31,0,32,6,2],
                         [4,2,3,6,1,1,2,6],
                         [1,40,42,2,6,1,3,8],
                         [2,41,43,3,8,4,3,6],
                         [6,7,6,7,6,4,2,8],
                         [8,4,3,2,2,3,1,6],
                         [6,2,1,5,1,2,4,8],
                         [3,6,2,6,7,6,7,6]]
        
    if niveau == 4:
        myGame.ground = [[31,31,32,31, 0,32,32,31],
                         [40,42, 6, 2, 2, 6,40,40],
                         [41,43, 8, 2, 6, 8,41,41],
                         [41,43, 6, 2, 2, 6,41,41],
                         [41,43, 8, 6, 2, 8,41,41],
                         [41,43, 6, 2, 2, 6,41,41],
                         [41,43, 8, 2, 6, 8,41,41],
                         [41,43, 6, 2, 2, 6,41,41]]
        
    if niveau == 5:
        myGame.ground = [[6,7,6,7,6,31,0,32],
                         [6,5,2,4,6,5,2,6],
                         [8,4,6,2,8,1,3,8],
                         [6,3,6,5,6,4,6,6],
                         [8,5,8,5,8,4,2,8],
                         [6,4,6,2,6,6,1,6],
                         [8,2,8,5,1,2,4,8],
                         [6,2,6,7,6,7,6,6]]

    for i in range (0,8):
        for j in range (0,8):
            pos = pygame.Rect(j*80, i*80, 80, 80)
            if myGame.ground[i][j] == 1: 
                myGame.screen.blit(myGame.tile1, pos)
            if myGame.ground[i][j] == 2:
                myGame.screen.blit(myGame.tile2, pos)
            if myGame.ground[i][j] == 3: 
                myGame.screen.blit(myGame.tile3, pos)
            if myGame.ground[i][j] == 4: 
                myGame.screen.blit(myGame.tile4, pos)
            if myGame.ground[i][j] == 5: 
                myGame.screen.blit(myGame.tile5, pos)
                
    for i in range (0,8):
        for j in range (0,8):
            if myGame.ground[i][j] == 6:
                pos = pygame.Rect(j*80, (i*80)-15, 80, 120)
                myGame.screen.blit(myGame.tile6, pos)
            if myGame.ground[i][j] == 7:
                pos = pygame.Rect(j*80, i*80, 80, 80)
                myGame.screen.blit(myGame.tile7, pos)
            if myGame.ground[i][j] == 8:
                pos = pygame.Rect(j*80, (i*80)-14, 80, 80)
                myGame.screen.blit(myGame.tile8, pos)
            if myGame.ground[i][j] == 0:
                pos = pygame.Rect(j*80, (i*80)+15, 80, 80)
                myGame.screen.blit(myGame.tile0, pos)
                myGame.screen.blit(myGame.door, pos)
            if myGame.ground[i][j] == 31:
                pos = pygame.Rect(j*80, (i*80)+15, 80, 80)
                myGame.screen.blit(myGame.tile31, pos)
            if myGame.ground[i][j] == 32:
                pos = pygame.Rect(j*80, (i*80)+15, 80, 80)
                myGame.screen.blit(myGame.tile32, pos)
            if myGame.ground[i][j] == 40:
                pos = pygame.Rect(j*80, i*80, 80, 80)
                myGame.screen.blit(myGame.tile40, pos)
            if myGame.ground[i][j] == 41:
                pos = pygame.Rect(j*80, i*80, 80, 80)
                myGame.screen.blit(myGame.tile41, pos)
            if myGame.ground[i][j] == 42:
                pos = pygame.Rect(j*80, i*80, 80, 80)
                myGame.screen.blit(myGame.tile42, pos)
            if myGame.ground[i][j] == 43:
                pos = pygame.Rect(j*80, i*80, 80, 80)
                myGame.screen.blit(myGame.tile43, pos)               

def drawfront(niveau):
    # les trucs jolis qui dépendent de chaque niveau
    if niveau == 1:
        # le blur
        myGame.screen.blit(myGame.blur, pygame.Rect(0, 0, 640, 555))
        # l'arbre 
        myGame.screen.blit(myGame.tree1, pygame.Rect(30, -120, 240, 408))
        # le toit du batiment
        myGame.screen.blit(myGame.tile31, pygame.Rect(240, -65, 80, 80))
        myGame.screen.blit(myGame.tile31, pygame.Rect(320, -65, 80, 80))
        myGame.screen.blit(myGame.tile31, pygame.Rect(400, -65, 80, 80))
        myGame.screen.blit(myGame.light, pygame.Rect(280, -45, 160, 160))
    
    if niveau == 2:
        # le toit du batiment
        myGame.screen.blit(myGame.tile31, pygame.Rect(240, -65, 80, 80))
        myGame.screen.blit(myGame.tile31, pygame.Rect(320, -65, 80, 80))
        myGame.screen.blit(myGame.tile31, pygame.Rect(400, -65, 80, 80))
        myGame.screen.blit(myGame.light, pygame.Rect(280, -45, 160, 160))
        
    if niveau == 3:
        # l'arbre 
        myGame.screen.blit(myGame.tree1, pygame.Rect(10, -140, 240, 408))
        # le toit du batiment
        myGame.screen.blit(myGame.tile31, pygame.Rect(240, -65, 80, 80))
        myGame.screen.blit(myGame.tile31, pygame.Rect(320, -65, 80, 80))
        myGame.screen.blit(myGame.tile31, pygame.Rect(400, -65, 80, 80))
        myGame.screen.blit(myGame.light, pygame.Rect(280, -45, 160, 160))

    if niveau == 4:
        # le toit du batiment
        myGame.screen.blit(myGame.tile31, pygame.Rect(0, -65, 80, 80))
        myGame.screen.blit(myGame.tile31, pygame.Rect(80, -65, 80, 80))
        myGame.screen.blit(myGame.tile31, pygame.Rect(160, -65, 80, 80))
        myGame.screen.blit(myGame.tile31, pygame.Rect(240, -65, 80, 80))
        myGame.screen.blit(myGame.tile31, pygame.Rect(320, -65, 80, 80))
        myGame.screen.blit(myGame.tile31, pygame.Rect(400, -65, 80, 80))
        myGame.screen.blit(myGame.tile31, pygame.Rect(480, -65, 80, 80))
        myGame.screen.blit(myGame.tile31, pygame.Rect(560, -65, 80, 80))
        myGame.screen.blit(myGame.light, pygame.Rect(280, -45, 160, 160))

    if niveau == 5:
        # le toit du batiment
        myGame.screen.blit(myGame.tile31, pygame.Rect(400, -65, 80, 80))
        myGame.screen.blit(myGame.tile31, pygame.Rect(480, -65, 80, 80))
        myGame.screen.blit(myGame.tile31, pygame.Rect(560, -65, 80, 80))
        myGame.screen.blit(myGame.light, pygame.Rect(280, -45, 160, 160))
        
# Regarde s'il y a de la place en haut
def haut():
    x = myGame.xyrobot[0]
    y = myGame.xyrobot[1] - 1
    if myGame.ground[y][x] > 5:
        return "bloqué"
    else:
        return "libre"

# Regarde s'il y a de la place en bas
def bas():
    x = myGame.xyrobot[0]
    y = myGame.xyrobot[1] + 1
    if myGame.ground[y][x] > 5:
        return "bloqué"
    else:
        return "libre"

# Regarde s'il y a de la place à droite
def droite():
    x = myGame.xyrobot[0] + 1
    y = myGame.xyrobot[1]
    if myGame.ground[y][x] > 5:
        return "bloqué"
    else:
        return "libre"

# Regarde s'il y a de la place à gauche
def gauche():
    x = myGame.xyrobot[0] - 1
    y = myGame.xyrobot[1]
    if myGame.ground[y][x] > 5:
        return "bloqué"
    else:
        return "libre"
