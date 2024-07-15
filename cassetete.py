import json
import time
def creaTab(i,j):
    T=[] 
    for k in range(i):
        L=[0 for k in range(j)]
        T.append(L)
    return T

def mettre(T,i,j,obj):
#    t=creaTab(len(T),len(T[0]))
#    for k in range(i):
#        for l in range(j):
#            t[k][l]=T[k][l]
    #print(t)
    for k in range(len(obj)):
        I=i+obj[k][0]
        J=j+obj[k][1]
        if I>len(T)-1 or J>len(T[0])-1 or I<0 or J<0:
            pass
            #return T
        else:
            T[I][J]+=1
        #print(T,t)
def mettretest(T,i,j,obj):
    a=0
    for k in range(len(obj)):
        I=i+obj[k][0]
        J=j+obj[k][1]
        if I>len(T)-1 or J>len(T[0])-1 or I<0 or J<0:
            return False
    
    return True

def retire(T,i,j,obj):
#    t=creaTab(len(T),len(T[0]))
#    for k in range(i):
#        for l in range(j):
#            t[k][l]=T[k][l]
    #print(t)
    for k in range(len(obj)):
        I=i+obj[k][0]
        J=j+obj[k][1]
        if I>len(T)-1 or J>len(T[0])-1 or I<0 or J<0:
            pass
            #return T
        else:
            T[I][J]-=1
        #print(T,t)

def surpasse(T):
    a=0
    for i in range(len(T)):
        for j in range(len(T[0])):
            if T[i][j]>1:
                a+=1
    if a!=0:
        return True
    else:
        return False
        

def estComplet(T):
    a=0
    for i in range(len(T)):
        for j in range(len(T[0])):
            if T[i][j]!=1:
                a+=1
    if a!=0:
        return False
    else:
        return True
def chercheLibre(T):            # return all free places
    LIBRE=[]
    for i in range(len(T)):
        for j in range(len(T[0])):
            if T[i][j]==0:
                LIBRE.append([i,j])
    return LIBRE
def copie(T):
     L=creaTab(len(T),len(T[0]))
     for k in range(len(T)):
         for l in range(len(T[0])):
             L[k][l]=T[k][l]
     return L
def generateAllRotations(obj):
    return [rotateObj(obj, i) for i in range(8)]

def solution(T, objets):
    print("Début de la recherche")
    global solu, histo, H
    solu = creaTab(len(T), len(T[0]))
    histo = []
    historique = []
    H = 0
    P = len(objets)

    def soluRec(profondeur, courante, historique):
        global solu, histo, H
        if H == 1:
            return None
        if surpasse(courante) or profondeur == P:
            return None
        else:
            LIBRE = chercheLibre(courante)
            for k in range(len(LIBRE)):
                if H == 1:
                    return None
                for rotation in generateAllRotations(objets[profondeur]):
                    if mettretest(courante, LIBRE[k][0], LIBRE[k][1], rotation):
                        mettre(courante, LIBRE[k][0], LIBRE[k][1], rotation)
                        historique.append([profondeur, LIBRE[k][0], LIBRE[k][1], rotation])
                        if estComplet(courante):
                            solu = copie(courante)
                            histo = copie(historique)
                            H = 1
                        soluRec(profondeur + 1, courante, historique)
                        retire(courante, LIBRE[k][0], LIBRE[k][1], rotation)
                        del historique[-1]

    soluRec(0, T, historique)
    return histo 
        

                    

        
def lecture(objets):
    f=open("cataforme.txt","r")
    R=f.readlines()
    A=[]
    B=[]
    for k in R:
        if k=="":
            break

        A.append(int(k[:3]))
        B.append(json.loads(k[4:-1]))
        

    obj=[]
    for k in range(len(objets)):
        i=A.index(objets[k])
        obj.append(B[i])
    return obj

def rotateObj(obj,numberOfRotations):
    #numberOfRotations is a number between 0 and 8
    #if numberOfRotations is 0, the object is not rotated
    #if numberOfRotations is 1, the object is rotated 90 degrees
    #if numberOfRotations is 2, the object is rotated 180 degrees
    #if numberOfRotations is 3, the object is rotated 270 degrees
    #if numberOfRotations is 4, the object is rotated 90 degrees and mirrored
    #if numberOfRotations is 5, the object is rotated 180 degrees and mirrored
    #if numberOfRotations is 6, the object is rotated 270 degrees and mirrored
    #if numberOfRotations is 7, the object is mirrored

    for i in range(numberOfRotations):
        if (numberOfRotations<4):
            obj = [[-y, x] for x, y in obj]
        else :
            obj = [[y, -x] for x, y in obj]
    minY = min(obj, key=lambda x: x[1])[1]
    minX = min([x[0] for x in obj if x[1] == minY])
    obj = [[x - minX, y - minY] for x, y in obj]
    return obj


    

#CreaTab et Objets: 
T = creaTab(5, 4)
obj = [
[[0, 0], [1, 0], [2, 0], [0, 1], [1, 1]] ,
[[0, 0], [1, 0], [2, 0], [0, 1], [2, 1]] ,
[[0, 0], [-1, 1], [0, 1], [1, 1], [-1, 2]],
[[0, 0], [1, 0], [2, 0], [3, 0], [2, 1]]
]

#obj=lecture(objets)
start=time.time()
print("solu",solution(T,obj))
end=time.time()
print(end-start)

    
