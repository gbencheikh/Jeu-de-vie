from ezCLI import *
from Voisin import *
from Fichier import *
def jeuVie(M):
    l = len(M)
    c = len(M[0])
    temp = [[0 for p in range(len(M[0]))] for k in range(len(M))]
    for i in range(l):
        for j in range(c):
            if M[i][j] == 1 and voisin8(M,i,j) == 2 :
                temp[i][j] = M[i][j]
            elif M[i][j] == 0 and (voisin8(M,i,j) == 1 or voisin8(M,i,j) == 3):
                temp[i][j] = 1
    return temp
def neige_extraterrestre(M,iteration):
    l = len(M)
    c = len(M[0])
    temp = [[0 for p in range(len(M[0]))] for k in range(len(M))]
    for i in range(l):
        for j in range(c):
            if iteration%2 == 0 and voisin4(M,i,j) == 1 :
                temp[i][j] = 1
            if iteration%2 != 0 and voisin8(M,i,j) == 1 :
                temp[i][j] = 1
    return temp
def ultman(M):
    l = len(M)
    c = len(M[0])
    temp = [[0 for p in range(len(M[0]))] for k in range(len(M))]
    for i in range(l):
        for j in range(c):
            if voisin4(M,i,j) == 1 :
                temp[i][j] = 1
            if M[i][j] == 1 :
                temp[i][j] = 1
    return temp
def fredkin4(M):
    l = len(M)
    c = len(M[0])
    temp = [[0 for p in range(len(M[0]))] for k in range(len(M))]
    for i in range(l):
        for j in range(c):
            if voisin4(M,i,j) % 2 == 0 :
                temp[i][j] = 1
    return temp
def fredkin8(M):
    l = len(M)
    c = len(M[0])
    temp = [[0 for p in range(len(M[0]))] for k in range(len(M))]
    for i in range(l):
        for j in range(c):
            if voisin8(M,i,j) % 2 == 0 :
                temp[i][j] = 1
    return temp
def automate_cellulaire(regle,M):
    return regle(M)

M = lire("life.txt")
for i in range (3):
    temp = jeuVie(M)
    print(temp)
    M = temp
