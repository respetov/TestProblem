#Main file
def stringToMatrix(string, numColls):
    matrizfinal = []
    aux = []
    pos = 0
    for i in string:
        aux.append(i)
        if pos == numColls:
            matrizfinal.append(aux)
            aux = []
            pos = 0
        pos +=1
    return matrizfinal
