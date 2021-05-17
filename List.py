from random import *
class list:
    def __str__(self):
        return "Mot restant: " + str(self.list)

    def __init__(self):
        self.sujet = ["Sale type tu","Tes ancêtres","Vous","Oh l'autruche"]
        self.verb = ["ont","sont","est","êtes"]
        self.complement = ["stupide","bien plus laid que mes pieds","même un aveugle serait choqué","un qi négatif"]
        self.liaison = ["et","avec","en plus","alors"]
        self.final = ["je te laisse deviner...","c'est monstrueux !","enfin bon...","voilà la vérité !"]
        self.words = [self.sujet, self.verb, self.complement, self.liaison, self.final]
        self.list = []
    
    def generator(self,faiblesse1,faiblesse2):
        i = 0
        self.list.append(faiblesse1)
        self.list.append(faiblesse2)
        for cat in self.words:
            for c in range(4):
                a = randint(0,(len(self.words[i])-1))
                self.list.append(self.words[i][a])
                self.words[i].pop(a)
                self.list.sort()
            i+=1
        return self.list
        
    def printlist(self):
        i = 0
        print("\n Voici la liste des mots restants:")
        for k in self.list:
            print(i+1,":",k)
            i+=1
