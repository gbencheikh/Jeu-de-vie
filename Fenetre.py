# ==============================================================================
"""Projet : Game of life and automate cellulaires """
# ==============================================================================
__author__  = "BENCHEIKH AND SADIK"
__version__ = "4.0"
__date__    = "15-12-2015"
# ==============================================================================
from ezCLI import *
from tkinter import *
from Fichier import *
from Automate import *
from tkinter import messagebox

import time
import random

#-------------------------------------------------------------------------------
class Interface(Frame):
    def __init__(self, fenetre):
        Frame.__init__(self,fenetre,width=300,height=400)

        #------------------------------------------
        #Creation des Frames 
        #------------------------------------------ 
        self.Frame1 = Frame(fenetre, borderwidth = 2, relief = GROOVE)
        self.Frame1.pack(side=LEFT,padx=10,pady=30)

        self.Frame2 = Frame(fenetre,borderwidth = 0 , relief = GROOVE)
        self.Frame2.pack(side=LEFT,padx=20,pady=20)
        
        self.Frame2_2 = Frame(self.Frame2,borderwidth = 2, relief = GROOVE)        
        self.Frame2_2.pack(side=BOTTOM,padx=20,pady=20)
        
        self.Frame4 = Frame(self.Frame2, borderwidth = 0, relief = GROOVE)
        self.Frame4.pack(side=TOP,padx=20,pady=10)
        
        self.Frame5 = Frame(self.Frame1, borderwidth = 0, relief = GROOVE)
        self.Frame5.pack(side=BOTTOM,padx=20,pady=30)
        
        #------------------------------------------        
        fenetre.title("Jeu de la vie")
        #------------------------------------------
        #Variables
        #------------------------------------------
        self.compt_generation = 0 #numero de l'itération 
        self.nb_vivant = 0        #nombre de cellules vivantes
        self.clic_stop = 0        #devient 1 si l'utilisateur clic sur le boutton stop
        self.regle = 1            #la règle avec lequel on génére la nouvelle population, par défaut on commence par la règle standard de jeu de la vie
        self.vitesse = 1000
        self.foret = 0            #devient 1 si l'utilisateur choisit l'automate de feu de forêt 
        #------------------------------------------
        # Construction de Frame1
        #------------------------------------------
        self.boutton_start = Button(self.Frame1,text = "Start", fg = "blue", command = self.start)
        self.boutton_start.pack(side = TOP)

        self.liste = Listbox(self.Frame1)
        self.liste.insert(1,"Seul point")
        self.liste.insert(2,"Vaisseau léger")
        self.liste.insert(3,"Vaisseau moyen")
        self.liste.insert(4,"Feu de forêt")
        self.liste.insert(5,"Planeurs")
        self.liste.insert(6,"Serpent")
        self.liste.insert(7,"Canon")
        self.liste.insert(8,"Crapaud")
        self.liste.insert(9,"Pentadecathlon")
        self.liste.insert(10,"Clignotant")
        
        self.liste.pack()

        #------------------------------------------
        # Construction de Frame2
        #------------------------------------------
        self.grid = Canvas(self.Frame2_2, width = 300, height=300,bg = 'white')
        self.grid.pack()
        #------------------------------------------
        #Construction de Frame3
        #------------------------------------------
        self.boutton_pause = Button(self.Frame4,text = "Stop", fg = "red", command = self.pause)
        self.boutton_reprendre = Button(self.Frame4,text = "Continu", fg ="green",command = self.reprendre)
        self.boutton_fast = Button(self.Frame4,text = "Faster",fg = "green",command = self.fast)
        self.boutton_slow = Button(self.Frame4,text = "Slower", fg = "green",command = self.slow)

        self.boutton_pause.pack(side = RIGHT)
        self.boutton_reprendre.pack(side = RIGHT)
        self.boutton_fast.pack(side = RIGHT)
        self.boutton_slow.pack(side = RIGHT)

        self.boutton_jeuVie = Button(self.Frame5,text="Jeu de la vie",width = 15, height = 1,fg = "grey",command = self.jeuVie)
        self.boutton_neige = Button(self.Frame5,text = "Neige extraterrestre",width = 15, height = 1,fg = "grey",command = self.neige)
        self.boutton_ultman = Button(self.Frame5,text = "Ultman",width = 15, height = 1, fg = "grey",command = self.ultman )
        self.boutton_fredkin = Button(self.Frame5,text = "Fredkin 4",width = 15, height = 1,fg = "grey", command = self.fredkin4)
        self.boutton_fredkin8 = Button(self.Frame5,text = "Fredkin 8" , width = 15, height = 1, fg = "grey", command = self.fredkin8)
        self.boutton_jeuVie.pack()
        self.boutton_neige.pack()
        self.boutton_ultman.pack()
        self.boutton_fredkin.pack()
        self.boutton_fredkin8.pack()
#-----------------------------------------------------------------------------
    def jeuVie(self):
        if self.foret == 0:
            self.regle = 1
    def neige(self):
        if self.foret == 0:
            self.regle = 2
    def ultman(self):
        if self.foret == 0:
            self.regle = 3
    def fredkin4(self):
        if self.foret == 0:
            self.regle = 4
    def fredkin8(self):
        if self.foret == 0:
            self.regle = 5
#-----------------------------------------------------------------------------
    def pause(self):
        if self.clic_stop == 0:
            self.clic_stop = 1
            
    def reprendre(self):
        if self.clic_stop == 1:
            self.clic_stop = 0
            self.process()
    def fast(self):
        if self.vitesse - 10 >0 :
            self.vitesse - 10
    def slow(self):
        if self.vitesse + 10 < 2000:
            self.vitesse + 10
#-----------------------------------------------------------------------------
    def start(self):
        name = ""
        self.compt_generation = 0
        n = self.liste.curselection()
        self.grid.destroy()
        self.grid = Canvas(self.Frame2_2, width = 300, height=300,bg = 'white')
        self.grid.pack(side = TOP)

        choix = self.liste.get(n)
        # Choix de la structure
        if choix != "Feu de forêt":
            self.foret = 0
        if choix == "Seul point" :
            name = "life.txt"
        elif choix == "Vaisseau léger":
            name = "Vaisseaul.txt"
        elif choix == "Vaisseau moyen":
            name = "Vaisseaum.txt"
        elif choix == "Feu de forêt":
            name = "Feu.txt"
            self.foret = 1
        elif choix == "Planeurs":
            name = "Planeurs.txt"
        elif choix == "Serpent":
            name = "Serpent.txt"
        elif choix == "Canon":
            name = "Canon.txt"
        elif choix == "Crapaud":
            name = "Crapaud.txt"
        elif choix == "Pentadecathlon":
            name = "Pentadecatlon.txt"
        elif choix == "Clignotant":
            name = "Clignotant.txt"
        else:
            messagebox.showinfo( "Erreur", "Vous n'avez pas choisis la structure")

        self.M = lire(name)     #  lire le fichier 
        self.l = len(self.M)    # le nombre de lignes de la matrice
        self.c = len(self.M[0]) # le nombre de colonnes de la matrice

        self.cellule_dimx = 300/self.c  # 
        self.cellule_dimy = 300/self.l  # les dimensions de chauque cellule 
        
        self.cell = [[0 for row in range(self.c)] for col in range(self.l)] # matrice de la population sous forme de grille

       
        for i in range(self.l):
            for j in range(self.c):
                y = i * self.cellule_dimy
                x = j * self.cellule_dimx
                self.cell[i][j] = self.grid.create_oval(x,y,x+self.cellule_dimx,y+self.cellule_dimy,fill = "white")

        self.update_grille()
        self.process()
#---------------------------------------------------------------------------------
    def process(self):
        if self.foret == 1 and self.clic_stop == 0:
            self.feu_foret()
            self.update_grille()
            self.compt_generation = self.compt_generation +1
            fenetre.after(self.vitesse,self.process)
        if self.regle == 1 and self.clic_stop == 0 and self.foret == 0:
            self.jeudeVie()
            self.update_grille()
            self.compt_generation = self.compt_generation +1
            fenetre.after(self.vitesse,self.process)
        elif self.regle == 2 and self.clic_stop == 0 and self.foret == 0:
            self.neige_extraterrestre()
            self.update_grille()
            self.compt_generation = self.compt_generation +1
            fenetre.after(self.vitesse,self.process)
        elif self.regle == 3 and self.clic_stop == 0 and self.foret == 0:
            self.ultman()
            self.update_grille()
            self.compt_generation = self.compt_generation +1
            fenetre.after(self.vitesse,self.process)
        elif self.regle == 4 and self.clic_stop == 0 and self.foret == 0:
            self.fredkin4()
            self.update_grille()
            self.compt_generation = self.compt_generation +1
            fenetre.after(self.vitesse,self.process)
        elif self.regle == 5 and self.clic_stop == 0 and self.foret == 0:
            self.fredkin8()
            self.update_grille()
            self.compt_generation = self.compt_generation +1
            fenetre.after(self.vitesse,self.process)
        
#---------------------------------------------------------------------------------
    def update_grille(self):
        for x in range(self.l):
            for y in range(self.c):
                if self.M[x][y] == 0:
                    self.grid.itemconfig(self.cell[x][y],fill = "white")
                elif self.M[x][y] == 1 :
                    self.grid.itemconfig(self.cell[x][y],fill = "blue")
                elif self.M[x][y] == 2 :
                    self.grid.itemconfig(self.cell[x][y],fill = "red")
                elif self.M[x][y] == 3 :
                    self.grid.itemconfig(self.cell[x][y],fill = "green")
                    
#---------------------------------------------------------------------------------
    def jeudeVie(self):
        V = [[0 for p in range(self.c)] for k in range(self.l)]
        for i in range(self.l):
            for j in range(self.c):
                if self.M[i][j] == 1 and voisin8(self.M,i,j) == 2 :
                    V[i][j] = self.M[i][j]
                elif self.M[i][j] == 0 and (voisin8(self.M,i,j) == 1 or voisin8(self.M,i,j) == 3):
                    V[i][j] = 1
        for i in range(self.l):
            for j in range(self.c):
                self.M[i][j] = V[i][j]
#---------------------------------------------------------------------------------
    def neige_extraterrestre(self):
        temp = [[0 for p in range(self.c)] for k in range(self.l)]
        for i in range(self.l):
            for j in range(self.c):
                if self.compt_generation%2 == 0 and voisin4(self.M,i,j) == 1 :
                    temp[i][j] = 1
                if self.compt_generation%2 != 0 and voisin8(self.M,i,j) == 1 :
                    temp[i][j] = 1
        for i in range(self.l):
            for j in range(self.c):
                self.M[i][j] = temp[i][j]
#---------------------------------------------------------------------------------
    def ultman(self):
        temp = [[0 for p in range(self.c)] for k in range(self.l)]
        for i in range(self.l):
            for j in range(self.c):
                if voisin4(self.M,i,j) == 1 :
                    temp[i][j] = 1
                if self.M[i][j] == 1 :
                    temp[i][j] = 1
        for i in range(self.l):
            for j in range(self.c):
                self.M[i][j] = temp[i][j]
#---------------------------------------------------------------------------------
    def fredkin4(self):
        temp = [[0 for p in range(self.c)] for k in range(self.l)]
        for  i in range(self.l):
            for j in range(self.c):
                if voisin4(self.M,i,j) % 2 == 0 :
                    temp[i][j] = 1
        for i in range(self.l):
            for j in range(self.c):
                self.M[i][j] = temp[i][j]
#---------------------------------------------------------------------------------
    def fredkin8(self):
        temp = [[0 for p in range(self.c)] for k in range(self.l)]
        for i in range(self.l):
            for j in range(self.c):
                if voisin8(self.M,i,j) % 2 == 0 :
                    temp[i][j] = 1
        for i in range(self.l):
            for j in range(self.c):
                self.M[i][j] = temp[i][j]
#---------------------------------------------------------------------------------
    def feu_foret(self):
        temp = [[0 for p in range(self.c)] for k in range(self.l)]
        for i in range(self.l):
            for j in range(self.c):
                if self.M[i][j] == 3 and voisin_Foret(self.M,i,j) == 1:
                    temp[i][j] = 2
                if self.M[i][j] == 3 and voisin_Foret(self.M,i,j) == 0:
                    temp[i][j] = 3
                if self.M[i][j] == 2 :
                    temp[i][j] = 1
                if self.M[i][j] == 1 :
                    temp[i][j] = 1
                if self.M[i][j] == 0:
                    temp[i][j] = 0
        for i in range(self.l):
            for j in range(self.c):
                self.M[i][j] = temp[i][j]
#---------------------------------------------------------------------------------
if __name__ == "__main__" :
    fenetre = Tk()
    interface = Interface(fenetre)
    interface.mainloop()
    interface.destroy()
