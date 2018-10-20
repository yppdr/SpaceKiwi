#import de la biliotheque datetime
import datetime
import random
#include de la classe hero
from Hero_class import * #hero
from Monstre_class import *

laDate = str(datetime.datetime.now().year);
leHero = Hero()
nbJour = 1
listeNomMonstre = ["Bashar Alasalad","Ouzama bananeladen","Arabricot","Kadafigue"]
listeObjet = ["Epee","Bouclier","potion"]

print("""En l'an de grâce %s, \n
une petite banane décida de se mettre en marche afin d'occire le terrible tyran Mouammar PommeDapi. \n
Etant un dieu malicieux, amusé par le courage (ou la débilité) du petit fruit,
vous décidez de supprimer toute trace d'existence de l'être jaune dans ce plan de la réalité.
"""%(laDate))
leHero.nom = input("Nom de cette pauvre banane:")
print("Celle petite banane se nommera donc %s."%leHero.nom)
while nbJour !=11 and leHero.pvActu >0:
    print('----------------------')
    print ("""Jour - %i"""%nbJour)
    laPhase = random.randint(1,5)
    if laPhase == 1 or laPhase ==2 :
        print("c'est la paix")
        leHero.gold += 20
        if(leHero.pvActu < leHero.pvMax):
            if(leHero.pvActu<10):
                leHero.pvActu += 2
            else:
                leHero.pvActu += 1
        print("Vous avez gagner 20 pépins !")
        print(leHero.afficherBourse())
        print("HP actuel: %i"%leHero.pvActu)

    elif laPhase == 3 or laPhase == 4 :
        print("c'est la guerre")
        leMontre = Monstre(listeNomMonstre[random.randint(0,len(listeNomMonstre)-1)],random.randint(5,20),random.randint(1,5),random.randint(1,5),random.randint(5,20))
        ordreTour = random.randint(0,1)
        while(leHero.pvActu > 0 and leMontre.pvActu >0):
            print("PV Hero: %i PV %s: %i"%(leHero.pvActu,leMontre.nom,leMontre.pvActu))
            if ordreTour == 0:
                leChoix = input("""Que faites-vous ? \n 1: Attaquer \n 2: defendre \n""")
                if leChoix == "1":
                    print("le hero attaque, %s perd %i PV \n \n "%(leMontre.nom,leHero.atk))
                    leMontre.pvActu = leMontre.pvActu - leHero.atk
                elif leChoix == "2":
                    print("vous vous défendez. \n \n")
                    leHero.pvActu = leHero.pvActu + leHero.deff
                    if leHero.pvActu > leHero.pvMax:
                        leHero.pvActu = leHero.pvMax
            else:
                actionMontre = random.randint(0,1)
                if actionMontre ==0:
                    print("%s attaque, %s perd %i PV \n \n"%(leMontre.nom,leHero.nom,leMontre.atk))
                    leHero.pvActu = leHero.pvActu - leMontre.atk
                else:
                    print("le monstre se défend. \n \n")
                    if(leMontre.pvActu < leMontre.pvMax):
                        leMontre.pvActu += leMontre.deff
                        if(leMontre.pvActu > leMontre.pvMax):
                            leMontre.pvActu = leMontre.pvMax
            #tour de l'autre parti
            if ordreTour == 0 : ordreTour = 1
            else: ordreTour = 0
        if leMontre.pvActu <=0:
            print("Bravo, vous avez vaincu le %s, vous recevez %i pépins \n \n"%(leMontre.nom,leMontre.gold))
            leHero.gold += leMontre.gold
        else:
            print("%s est mort, et c'est de VOTRE faute. \n \n"%leHero.nom)
    else:
        print("""c'est le shop""")
        choixShop = "0"
        print(leHero.afficherStats())
        print("""Epee: +1atk  Bouclier: +1 deff potion: +5 pv max \n
        1:Epee (10 pépins) \n 2:Bouclier (10 pépins) \n 3:Potion (15 pépins) \n 4:quitter \n \n""")
        while choixShop != "4":
            choixShop = input("Que faites vous: ")
            if choixShop == "1":
                if leHero.gold >=10:
                    leHero.gold -=10
                    leHero.atk +=1
                    print ("Vous avez améliorer votre épée. \n \n")
                else:
                    print("Vous n'avez pas assez d'argent pour améliorer votre épée \n\n")
            elif choixShop == "2":
                if leHero.gold >=10:
                    leHero.gold -=10
                    leHero.deff +=1
                    print ("Vous avez améliorer votre bouclier. \n \n")
                else:
                    print("Vous n'avez pas assez d'argent pour améliorer votre bouclier \n\n")
            elif choixShop == "3":
                if leHero.gold >=15:
                    leHero.gold -=15
                    leHero.pvMax += 5
                    print ("Vous avez améliorer votre santé. \n \n")
                else:
                    print("Vous n'avez pas assez d'argent pour améliorer votre santé \n \n")
    input('appuie pour continuer')
    nbJour +=1
print ("Fin de l'aventure")
