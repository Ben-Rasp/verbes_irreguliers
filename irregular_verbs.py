#!/usr/bin/python3
import random
import time

class IrregularVerbs:
    
    def __init__(self, premier, dernier, nombre):
        self.premier = premier
        self.dernier = dernier
        self.nombre = int(nombre)
        fic = open('verbes_irreguliers.txt', 'r')
        lignes = [v[:-1] for v in fic.readlines()]
        liste_globale = []
        liste_verbe   = []
        x = 0
        for l in lignes:
            liste_verbe.append(l)
            i = x % 4
            if i == 3:
                liste_globale.append(liste_verbe)
                liste_verbe = []
            x += 1
        for v in liste_globale:
            if self.premier in v[3]:
                self.debut = liste_globale.index(v)
            if self.dernier in v[3]:
                self.fin = liste_globale.index(v)+1
        self.liste_verbes= liste_globale[self.debut:self.fin]
        fichier = open('liste_verbes_irreguliers.txt', 'w')
        for v in liste_globale:
            verb = "{0},{1},{2},{3}\n".format(v[0],v[1],v[2],v[3])
            fichier.write(verb)
        fichier.close()
        random.shuffle(self.liste_verbes)
        self.liste_verbes = self.liste_verbes[:self.nombre]

    def exercice(self):
        score = 0
        for v in self.liste_verbes:
            print('')
            print(v[3],":")
            base = input("      base : ")
            pret = input("      prétérit : ")
            part = input("      participe passé : ")
            if base==v[0] and pret==v[1] and part==v[2]:
                score += 2
                print('bravo !')
            elif (base == v[0] and pret == v[1]) or (base == v[0] and part == v[2]) or (pret == v[1] and part == v[2]):
                if base == v[0] and pret == v[1]:
                    print("                 base et prétérit OK ")
                    score += 1
                    part = input("      participe passé : ")
                    if part == v[2]:
                        print("                 participe passé OK")
                        score += 0.25
                    else:
                        print("CORRECTION :",v)
                elif base == v[0] and part == v[2]:
                    print("                 base et participe passé OK ")
                    score += 1
                    pret = input("      prétérit : ")
                    if pret == v[1]:
                        print("                 prétérit OK")
                        score += 0.25
                    else:
                        print("CORRECTION :",v)
                elif pret == v[1] and part == v[2]:
                    print("                 prétérit et participe passé OK")
                    score += 1
                    base = input("      base : ")
                    if base == v[0]:
                        print("                 base OK")
                        score += 0.25
                    else:
                        print("CORRECTION :",v)
            elif base == v[0] or pret == v[1] or part == v[2]:
                score += 0.5
                if base == v[0]:
                    print("                 base OK")
                    pret = input("      prétérit : ")
                    part = input("      participe passé : ")
                    if pret == v[1]:
                        print("                 prétérit OK")
                        score += 0.25
                    if part == v[2]:
                        print("                 participe passé OK")
                        score += 0.25
                elif pret == v[1]:
                    print("                 prétérit OK")
                    base = input("      base : ")
                    part = input("      participe passé : ")
                    if base == v[0]:
                        print("                 base OK")
                        score += 0.25
                    if part == v[2]:
                        print("                 participe passé OK")
                        score += 0.25
                elif part == v[2]:
                    print("                 participe passé OK")
                    base = input("      base : ")
                    pret = input("      prétérit : ")
                    if base == v[0]:
                        print("                 base OK")
                        score += 0.25
                    if pret == v[1]:
                        print("                 prétérit OK")
                        score += 0.25
                if base != v[0] or pret != v[1] or part != v[2]:
                    print("CORRECTION:",v)
            else:
                print("         seconde chance pour base, prétérit et participe passé")
                base = input("      base : ")
                pret = input("      prétérit : ")
                part = input("      participe passé : ")
                if base==v[0] and pret==v[1] and part==v[2]:
                    print("                 OK")
                    score += 0.75
                elif base == v[0] or pret == v[1] or part == v[2]:
                    if base==v[0]:
                        print("                 base OK")
                        score += 0.25
                    if pret==v[1]:
                        print("                 prétérit OK")
                        score += 0.25
                    if part==v[2]:
                        print("                 participe passé OK")
                        score += 0.25
                if base != v[0] or pret != v[1] or part != v[2]:
                    print("CORRECTION:",v)



        self.score = score
        self.total_points = len(self.liste_verbes)*2
        print('\n\n')
        print("Ton score est de {0} sur {1}.".format(self.score,self.total_points))
        if self.total_points != 20:        
            print("...soit {0}/20.".format(round(self.score/self.total_points*20,1)))

        print('\n\n')

    def test(self):
        score = 0
        flag  = -1
        for v in self.liste_verbes:
            flag = (flag +1)%4
            print('\n\n')
            if flag == 0:
                print(       "                |base :",v[0])
                pret = input("                |                |prétérit : ")
                part = input("                |                |                |participe passé : ")
                verbe= input("verbe : ")
                if pret == v[1] and part == v[2] and verbe in v[3]:
                    score += 1
                print(score,"CORRECTION:",v)
            elif flag == 1:
                print(       "                |                |prétérit :",v[1])
                base = input("                |base : ")
                part = input("                |                |                |participe passé : ")
                verbe= input("verbe : ")
                if base == v[0] and part == v[2] and verbe in v[3]:
                    score += 1
                print(score,"CORRECTION:",v)
            elif flag == 2:
                print(       "                |                |                |participe passé :",v[2])
                base = input("                |base : ")
                pret = input("                |                |prétérit : ")
                verbe= input("verbe : ")
                if base == v[0] and pret == v[1] and verbe in v[3]:
                    score += 1
                print(score,"CORRECTION:",v)
            else:
                print("verbe :",v[3])
                base = input("                |base : ")
                pret = input("                |                |prétérit : ")
                part = input("                |                |                |participe passé : ")
                if base == v[0] and pret == v[1] and part == v[2]:
                    score += 1
                print(score,"CORRECTION:",v)
        self.score = score
        self.total_points = len(self.liste_verbes)



    def enregistrer_score(self):
        now = time.localtime(time.time())
        year, month, day, hour, minute, second, weekday, yearday, daylight = now
        phrase = (("Lun ", "Mar ", "Mer ", "Jeu ", "Ven ", "Sam ", "Dim ")[weekday]," ",day, (" Janvier ", " Février ", " Mars ", " Avril ", " Mai ", " Juin ", " Juillet ", " Août ", " Septembre ", " Octobre ", " Novembre ", " Décembre ")[month]," ", year," ", hour," ", minute,":\t\t","{0} sur {1}.".format(self.score,self.total_points),'\n')
        fichier_score = open("fichier_score", "a")
        for p in phrase:
                    fichier_score.write(str(p))
        fichier_score.close()
        print("Partie enregistrée!")
        fichier_score = open("fichier_score", "r")
        f = fichier_score.read()
        print(f)

if __name__=="__main__":
    
    while True:
        q = input("Exercice ou Test ? (e/t) :")
        if q == '':
            break
        p = input("premier verbe : ")
        if p == '':
            p = "survenir,surgir"    
        d = input("dernier verbe : ")
        if d == '':
            d = "rencontrer" 
        n = input("nombre de verbes : ")
        print('')
        c = IrregularVerbs(p,d,n)
        if q == 'e':
            c.exercice()
        else:
            c.test()
        c.enregistrer_score()

