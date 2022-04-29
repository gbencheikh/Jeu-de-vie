from ezCLI import *
def voisin8(M,i,j):
    l = len(M)
    c = len(M[0])
    somme = 0;
    if i < l-1 and i > 0:
        if j > 0 and j < c-1:
            somme = M[i-1][j] + M[i-1][j+1] + M[i-1][j-1]+ M[i][j-1] + M[i][j+1] + M[i+1][j] + M[i+1][j+1] + M[i+1][j-1];
        elif j == 0:
            somme = M[i-1][j] + M[i-1][j+1]+ M[i][j+1]+ M[i+1][j] + M[i+1][j+1];
        elif j == c-1:
            somme = M[i-1][j] + M[i-1][j-1]+ M[i][j-1]+ M[i+1][j] + M[i+1][j-1];
    elif i == 0:
        if j > 0 and j < c-1:
            somme = M[i][j-1]+ M[i][j+1]+ M[i+1][j-1] + M[i+1][j] + M[i+1][j+1];
        elif j == 0:
            somme = M[i][j+1]+ M[i+1][j] + M[i+1][j+1];
        elif j == c-1:
            somme = M[i][j-1]+ M[i+1][j-1] + M[i+1][j];
    elif i == l-1:
        if j > 0 and j < c-1:
            somme = M[i-1][j-1] + M[i-1][j] + M[i-1][j+1]+ M[i][j-1]+ M[i][j+1];
        if j == 0:
            somme = M[i-1][j] + M[i-1][j+1]+ M[i][j+1];
        if j == c-1:
            somme = M[i-1][j] + M[i-1][j-1]+ M[i][j-1];
    return somme;
def voisin4(M,i,j):
    l = len(M)
    c = len(M[0])
    somme = 0;
    if i < l-1 and i > 0:
        if j > 0 and j < c-1:
            somme = M[i+1][j+1] + M[i+1][j-1] + M[i-1][j+1] + M[i-1][j-1]
        elif j == 0:
            somme = M[i+1][j+1] + M[i-1][j+1]
        elif j == c-1:
            somme = M[i+1][j-1] + M[i-1][j-1]
    elif i == 0:
        if j > 0 and j < c-1:
            somme = M[i+1][j+1] + M[i+1][j-1]
        elif j == 0:
            somme = M[i+1][j+1]
        elif j == c-1:
            somme = M[i+1][j-1]
    elif i == l-1:
        if j > 0 and j < c-1:
            somme = M[i-1][j+1] + M[i-1][j-1]
        elif j == 0:
            somme = M[i-1][j+1]
        elif j == c-1:
            somme = M[i-1][j-1]
    return somme

def voisin_Foret(M,i,j):
    l = len(M)
    c = len(M[0])
    if i < l-1 and i > 0:
        if j > 0 and j < c-1 :
            if M[i-1][j] == 2 or M[i-1][j+1] == 2 or M[i-1][j-1] == 2 or M[i][j-1] == 2 or M[i][j+1] == 2 or M[i+1][j] == 2 or M[i+1][j+1]==2 or M[i+1][j-1] == 2:
                return 1
            else:
                return 0
        elif j == 0:
            if M[i-1][j] == 2 or  M[i-1][j+1]==2 or M[i][j+1]== 2 or M[i+1][j]==2 or M[i+1][j+1] == 2:
                return 1
            else:
                return 0
        elif j == c-1:
            if M[i-1][j] == 2 or M[i-1][j-1]==2 or M[i][j-1]==2 or M[i+1][j]==2 or M[i+1][j-1]==2:
                return 1
            else:
                return 0
    elif i == 0 :
        if j > 0 and j < c-1:
            if M[i][j-1]== 2 or M[i][j+1] == 2 or M[i+1][j-1]== 2 or  M[i+1][j]== 2 or  M[i+1][j+1]== 2:
                return 1
            else:
                return 0
        elif j == 0 :
            if M[i][j+1]==2 or M[i+1][j]==2 or M[i+1][j+1]==2:
                return 1
            else:
                return 0
        elif j == c-1:
            if M[i][j-1]==2 or M[i+1][j-1]== 2 or M[i+1][j]==2:
                return 1
            else :
                return 0
    elif i == l-1:
        if j > 0 and j < c-1:
            if M[i-1][j-1]==2 or M[i-1][j] ==2 or  M[i-1][j+1]==2 or M[i][j-1] == 2 or M[i][j+1]== 2 :
                return 1
            else :
                return 0
        if j == 0:
            if M[i-1][j]== 2 or  M[i-1][j+1]== 2 or  M[i][j+1]== 2 :
                return 1
            else:
                return 0
        if j == c-1:
            if M[i-1][j]== 2 or  M[i-1][j-1] == 2 or M[i][j-1] == 2 :
                return 1
            else :
                return 0
