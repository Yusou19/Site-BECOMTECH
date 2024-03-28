print("- Bienvenue sur Fantasia World ! Crée par Mélody 2.0")
nom = input("- Avant de débuter, quel est votre nom ? ")
print("- Encore bienvenue "+nom+", j'espère que le jeu te plaira ;) Attention aucune sauvegarde n'est effectué lors du commencement, prenez le temps de finir complètement le jeu [TEMPS NÉCESSAIRE : ??]. Le jeu deviendra de plus en plus dur qui demandera des réflexions (retenez les détails ^^) et ne mourrez pas...")
print("/!\ INFORMATION IMPORTANTE : Si vous mourrez une fois, c'est fini. Il n'y a pas de seconde chance :) (pas pour l'instant en tout cas)")
print("- Petit résumé de votre vie : 18 ans, fini le lycée, bac S, insociable, beaucoup de malchance mais super courageuse et possède une gentillesse incontournable!")

question0 = input("Voulez-vous commencer ? [1]OUI [2]NON : ")
if question0 == "1":
    print("Bon courage !")
if question0 == "2":
    print("A bientôt :(")
    exit()

print("CHAPITRE 1 : La fin de la malchance ?")
print("- Le 6 juillet 2037, les vacances commencent enfin après plusieurs mois d'attentes et le bac entre les mains ! Malgré le manque d'ami en raison de votre timidité, vous décidez quand même de vous faire plaisir. Le soir, vous partez acheter de la glace au supermarché de votre ville...")
question1 = input("- Quel glace pourriez-vous acheter ? [1]De la glace à la vanille ! [2]De la glace au chocolat ! [3]De la glace à la fraise ! : ")
if question1 == "1":
    print("- J'adore cette glace, classique et basique ! J'achète !")
elif question1 == "2":
    print("- En manger beaucoup c'est pas ouf mais c'est tellement bon. J'achète !")
if question1 == "3":
    print("- Un peu de fraîcheur pourquoi pas ! J'achète !")
    
print("- Vous avez choisi une super saveur ! Maintenant il est l'heure de rentrer chez soi. Sur la route, vous rencontrez un homme alcoolisé...")
question2 = input("- Vous décidez de... [1]Changer de route en prenant un chemin plus long qui nécessitera de traverser un quartier mal fréquenter. [2]Continuer votre chemin en pensant qu'il ne va rien se passer. : ")
if question2 == "1":
    print("- L'homme alcoolisé commence à vous suivre...")
if question2 == "2":
    print("- L'homme se stoppe et commence à vous suivre...")

print("- La panique commence à monter. Vous prenez peur de plus en plus, il ne reste plus qu'à faire quelque chose.")
question3 = input("- Vous décidez de vous cacher en attendant de trouver une solution... [1]Appeler la police comme un faible. [2]Jouer à cache cache en gagnant comme Zoro. [3]Courir super vite en appelant de l'aide au passant. : ")
question4 = ""
question5 = ""

if question3 == "1":
    print("- Il n'y a pas de connexion là où vous êtes... Le coeur bat de en plus en vite car il se rapproche...")
    question4 = input("[1]Vous décidez de reprendre la dernière solution : COURIR !!! : ")
elif question3 == "2":
    print("- Vous jouez à cache cache avec l'homme, prendre Zoro comme exemple n'était pas une bonne idée. Il a 0 sens d'orientation. Vous vous retrouvez donc en face de lui...")
    question5 = input("[1]Il ne reste plus qu'à courir !!! : ")
if question3 == "3":
    print("- Vous courez à grande vitesse comme un TGV mais il n'y a personne à l'horizon.")
    
print("- Lors de votre course, vous traversez un passage piéton. Sans le remarquer, une voiture arriva et vous percuta !")
print("Fin du chapitre 1")

print("CHAPITRE 2 : Où suis-je ?")
print("- Vous vous réveillez tout doucement en ayant énormément mal à la tête. Vous remarquez que vous êtes dans une forêt inconnu.")
question6 = input("- [1] Visitons cette endroit pour en ressortir ! [2]Cette endroit est bizarre ! Vous vous en moquez et vous vous rendormez.. [3] On m'a kidnappé ? : ")
question7 = ""
question8 = ""
if question6 == "1":
    print("- Commençons par sortir de cette forêt !")
elif question6 == "2":
    print("- Etant donné que j'ai mal à la tête, dormir ne serai pas de refus haha.")
    question7 = input("[1]Quoique, avoir cette penser d'être à un endroit inconnu... Ca me stresse trop ! Trouvons une solution pour y sortir : ")
if question6 == "3":
    print("- C'est possible vu que je porte malchance, plus qu'à voir ce qui suit...")
    question8 = input("- [1]Sortons pour voir où je me trouve [2] Non, j'ai trop peur de me retrouver nez à nez avec l'homme : ")
if question8 == "2":
    print("PERDU ! Pourquoi avez-vous perdu ? "+nom+" est super courageux/courageuse et n'a donc peur de rien :)")
    exit()
    
print("- Vous marchez dès à présent pour essayer de trouver une sortie mais sans espoir... Vous tournez en rond depuis tout à l'heure. Jusqu'au moment où vous voyez une petite sorte de fée? Qui est en mauvaise posture !")
question9 = input("- [1]Vous vous approchez de cette ''bête'' [2]Vous allez lui demander des renseignements [3]Vous la laissez, elle pourrait être dangereuse : ")
question10 = ""
if question9 == "1":
    print("- Vous prenez la bête dans vos mains, elle n'a pas l'air d'être en forme")
    question10 = input("- [1]Vous l'aidez à se sentir bien de nouveau [2]Vous la laissez tomber, elle vous énerve déjà : ")
if question10 == "1":
    print("- Vous l'emmenez proche d'une rivière pour qu'elle puisse boire et autre.")
if question10 == "2":
    print("PERDU ! Pourquoi avez-vous perdu ? "+nom+" est gentil/gentille ! Elle n'abandonnerai personne, encore moins une personne qui est vulnérable !")
    exit()
if question9 == "2":
    print ("- Elle n'a pas l'air d'être en bonne santé...")
    question11 = input("- [1] Vous l'aidez à se sentir de nouveau bien [2] Vous préférez chercher quelqu'un d'autre pour avoir des renseignements : ")
if question11 == "1":
    print("- Vous l'emmenez proche d'une rivière pour qu'elle puisse boire et autre.")
if question11 == "2":
    print("PERDU ! Si vous vous en rappelez bien, avant la question précédente : ''Vous marchez dès à présent pour essayer de trouver une sortie mais sans espoir... Vous tournez en rond depuis tout à l'heure''. Soit plus attentive la prochaine fois ;)")
    exit()
if question9 == "3":
    print ("PERDU ! Pourquoi avez-vous perdu ? "+nom+" est gentil/gentille ! Elle n'abandonnerai personne, encore moins une personne qui est vulnérable !")
    exit()