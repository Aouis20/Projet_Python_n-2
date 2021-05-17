from List import *
from Player import *
menu = {
        "⚔️  1": "Jouer",
        "📜 2": "Règles",
        "💬 3": "A propos",
        "🚪 4": "Quitter",
}

class game:

    def __init__(self):
        #Création d'éléments
        self.p1 = Player("Joueur 1",0,100,None,None,[])
        self.p2 = Player("Joueur 2",0,100,None,None,[])
        self.thelist = list()
        self.Menu()

    def intro(self):
        print("")
        print("Bienvenue !")
        print("Commencez par définir vos personnages !")
    
    # Éléments
    def init_object(self):
        #Définition d'éléments
        self.p1.choose_name()
        self.p1.choose_perso()
        print("")
        self.p2.choose_name()
        self.p2.choose_perso()
        print("")
        #Définition aléatoire de la list
        self.thelist.generator(self.p1.faiblesse,self.p2.faiblesse)
        
    # Déroulement des tours
    def turns(self,p,thelist):
        # Afficher la liste
        thelist.printlist()

        # Afficher le joueur ayant le tour
        print(p)
        choix = p.turn()
        if choix == 'Carte blanche':
            cb = str(input("A vous de jouer: "))
            p.mylist += "" + cb
            return choix
        else:
            print(p.name,"a choisi:",thelist.list[choix])
            p.mylist += " " + thelist.list[choix]
            if thelist.list[choix] == self.p1.faiblesse or thelist.list[choix] == self.p2.faiblesse:
                print("💥💥")
                print("Aïe coup dur !")
                print("Score x2 !!!")
                p.score = p.score * 2 #Score actuel *2
            thelist.list.pop(choix)
            # Définir le score
            self.score(p)
        return p.score

    def score(self,p):
        c = 0
        for letters in p.mylist:
            c+=1
        p.score += c
        print(p.name,"est actuellement à",p.score,"PTS !")
        return p.score
        
    #Résultat 
    def result(self,p1,p2):
        p_win = None
        print("\n*** Résultats: ***")
        print("=>Phrase de:",p1.name,"(SCORE:",p1.score,"PTS)",":",p1.mylist)
        print("=>Phrase de:",p2.name,"(SCORE:",p2.score,"PTS)",":",p2.mylist)
        if p1.score > p2.score:
            p2.pv = 0
            p_win = p1
        elif p1.score == p2.score:
            p1.pv = 0
            p2.pv = 0
            print("Cette manche s'achève avec une égalité parfaite !")
            p_win = None
            return p_win
        else:
            p1.pv = 0
            p_win = p2
        print(p_win.name,"remporte cette manche avec un score de",p_win.score,"PTS !")
        return p_win

    #Duel
    def fight(self):
        thelist = self.thelist
        p1 = self.p1
        p2 = self.p2
        game_status = True
        round = 0
        while game_status:
            while p1.pv > 0 and p2.pv > 0:
                if len(thelist.list) > 0: 
                    self.turns(p1,thelist)
                    self.turns(p2,thelist)
                else:
                    self.result(p1,p2)
                    round+=1
            game_status = False

    # Lancement du jeu...
    def launch_game(self):
        self.intro()
        self.init_object()
        self.fight()


    def about(self):
        print("Jeu crée et développé en python par Aouis CHOUKRI.")
        
    #Menu
    def Menu(self):
        print("_____Bienvenue sur le Menu_____\n")
        for k in menu:
            print(k,":",(menu[k]))
        choix = int(input("\n==>Veuillez entrer un nombre afin de valider votre choix: "))
        if choix == 1:
            self.launch_game()
        elif choix == 2:
            self.rules()
        elif choix == 3:
            self.about()
        elif choix == 4:
            print("Vous pouvez fermer la fenêtre.")
        else:
            print("Veuillez entrer un choix valide !")
            choix = int(input("Veuillez entrer un nombre afin de valider votre choix: "))

        input("\n Entrez 'Entrée' pour revenir au menu principale...")
        print("\n\n\n\n")
        self.Menu()