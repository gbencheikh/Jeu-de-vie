from ezCLI import *
def lire(name):
    file = open(name)
    M = []
    for line in file:
        M.append( [int (x) for x in line.split(' ') ])    
    return M
