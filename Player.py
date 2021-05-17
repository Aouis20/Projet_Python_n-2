from random import *
roles = ["politicien","fermier","étudiant","ouvrier"]
faiblesse = ["riche","chomeur","raté","aveugle"]
class Player:

    def __str__(self):
        print("\n=> Tour de",self.name)
        return "NOM: " + str(self.name) + "\n" + "SCORE: " + str(self.score) + " PTS" + "\n" + "Phrase: " + self.mylist + "\n" + "Carte blanche disponible: " + str(self.carte_blanche)
        
    def __init__(self,name,score,pv,role,faiblesse,mylist):
        self.name = name
        self.score = score
        self.pv = pv
        self.role = role
        self.faiblesse = faiblesse
        self.mylist = ""
        self.carte_blanche = 1


    #Name
    def choose_name(self):
        random_name = ["Bob","John","Jack","Ethan","Steve","Bill","James"]
        print("\n*",self.name,"*")
        print("\n => Veuillez choisir votre nom...")
        print("(Si aucun nom est entrée un nom par défaut vous sera attribué.)")
        name = str(input("Nom: "))
        if name:
            self.name = name
        else:
            self.name = random_name[randint(0,len(random_name)-1)]
            print("Vous vous appeler Bob")
        return self.name

    #Role / Faiblesse
    def choose_perso(self):
        print("\n => Choisissez maintenant un role, chaque rôle à une certaine faiblesse (↘️  ).")
        print("Voici les rôles restants:")
        for role in range(0,len(roles),1):
            print(role+1,":",roles[role],"(↘️ ",faiblesse[role],")")
        choix = int(input("Choisissez votre rôle: "))-1
        self.role = roles[choix]
        print("=>Rôle de",self.name,":",self.role)
        self.faiblesse = faiblesse[choix]
        print("=>Faiblesse :",self.faiblesse)
        roles.pop(choix)
        faiblesse.pop(choix)
        return roles


    #score
    def myscore(self):
        c = 0
        for letters in self.mylist:
            c+=1
        self.score += c
        print(self.name,"est actuellement à",self.score,"PTS !") 

    #Tour player
    def turn(self):
        choix = input("Choisis maintenant un mot de la liste ci-dessus: ")
        if choix == 'Carte blanche':
            if self.carte_blanche > 0:
                self.carte_blanche -=1
                print("Carte blanche activé !")
            else:
                print("Tu n'as pas de carte blanche disponible, tu es obligé de choisir un mot de la liste !")
                choix = input("Choisis maintenant un mot de la liste ci-dessus: ")
        else:
            choix = int(choix)-1
        return choix