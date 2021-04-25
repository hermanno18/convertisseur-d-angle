# -*- coding: utf8 -*-

#liste des modules à importer
from math import pi
#liste des fonctions
def degToRad(valeur):
    return  valeur*pi/180
def radToDeg(valeur):
    return  valeur*180/pi
#corps du programme
    #définition du menu
menu = "Options disponibles : "
menu += "\n\t1 : Convertir des degrés en radians"
menu += "\n\t2 : Convertir des radians en degrés"
menu += "\n\tq : Quitter"    
menu += "\nVotre choix :"    
    #affichage du menu
choix= input(menu)
while True:
    choix.strip # on formate bien l'entrée
    drapau = False # variable qui permettra de retenir si l'utilisateur a vait tel ou  tel choix
    if(choix == "q" or choix == "Q"):
        print("Aurevoir ! arrêt du programme...")
        exit()
    elif(choix == "1"):
        valeur = float(input("Entrez la mesure en degré de votre angle :"))
        #appel de la fonction de conversion
        print("\trésultat :  "+str(valeur)+"° = "+str(degToRad(valeur))+"rad")
        drapau = True
    elif(choix == "2"):
        valeur = float(input("Entrez la mesure en radians de votre angle :"))
        #appel de la fonction de conversion
        print("\trésultat :  "+str(valeur)+"°rad = "+str(degToRad(valeur))+"°")
        drapau = True
    else:
        choix = input('Choix non repertorié, veuillez reéssayer :')

    if drapau: # si l'utilisateur a bien fait une conversion on lui propose de recommencer ou quitter
        choix = input("voulez vous quitter le programme ? si oui, entrez 'q' sinon, entrez 'n' : ") 
        if(choix == "q" or choix == "Q" ):
            print("Aurevoir ! arrêt du programme...")
            exit()
        elif(choix == "n" or choix == "N" ):
            #affichage du menu
            choix = input(menu)




    
