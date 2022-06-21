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
            a+=1
    if a!=0:
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
def chercheLibre(T):
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
    
        
def solution(T,objets):
    print("Début de la recherche")
    global solu,histo,H
    solu=creaTab(len(T),len(T[0]))
    histo=[]
    historique=[]
    H=0
    #print("1ere",solu)
    P=len(objets)
    def soluRec(profondeur,courante,historique):
        global solu,histo,H
        #print(courante)
        if H==1:
            return None
        if surpasse(courante) or profondeur==P:
            return None
        else:
            LIBRE=chercheLibre(courante)
            
            for k in range(len(LIBRE)):
                if H==1:
                    return None
                if mettretest(courante,LIBRE[k][0],LIBRE[k][1],objets[profondeur]):
                    mettre(courante,LIBRE[k][0],LIBRE[k][1],objets[profondeur])
                    historique.append([profondeur,LIBRE[k][0],LIBRE[k][1]])
                    #print(histo)
                    
                
                
                    if estComplet(courante):
                        print("trouvée")
                        solu=copie(courante)
                        histo=copie(historique)
                        H=1
                    
                    soluRec(profondeur+1,courante,historique)
                
                    retire(courante,LIBRE[k][0],LIBRE[k][1],objets[profondeur])
                    del historique[-1]
                    soluRec(profondeur+1,courante,historique)
        
    soluRec(0,T,historique)
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



#CreaTab et Objets: 
T=creaTab(11,3)  #lignes colonnes
objets=[40,3,41,5,42,43,11]
obj=lecture(objets)
start=time.time()
print("solu",solution(T,obj))
end=time.time()
print(end-start)

    
