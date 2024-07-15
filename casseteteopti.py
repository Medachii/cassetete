import json
import time

def creaTab(i, j):
    return [[0] * j for _ in range(i)]

def mettre(T, i, j, obj):
    for di, dj in obj:
        T[i + di][j + dj] += 1

def mettretest(T, i, j, obj):
    for di, dj in obj:
        I, J = i + di, j + dj
        if not (0 <= I < len(T) and 0 <= J < len(T[0])) or T[I][J] != 0:
            return False
    return True

def retire(T, i, j, obj):
    for di, dj in obj:
        T[i + di][j + dj] -= 1

def surpasse(T):
    return any(cell > 1 for row in T for cell in row)

def estComplet(T):
    return all(cell == 1 for row in T for cell in row)

def chercheLibre(T):
    return [(i, j) for i, row in enumerate(T) for j, cell in enumerate(row) if cell == 0]

def copie(T):
    return [row[:] for row in T]

def generateAllRotations(obj):
    rotations = []
    obj = sorted(obj)  # Sort to handle symmetry by initial position
    for _ in range(4):  # 4 possible rotations
        obj = rotateObj(obj, 1)
        rotations.append(sorted(obj))  # Ensure to handle symmetry by sorting
    obj = mirrorObj(obj)  # Mirror and rotate again
    for _ in range(4):  # 4 more possible rotations of the mirrored piece
        obj = rotateObj(obj, 1)
        rotations.append(sorted(obj))
    return rotations

def rotateObj(obj, numberOfRotations):
    for _ in range(numberOfRotations):
        obj = [[-y, x] for x, y in obj]
    minX = min(x for x, y in obj)
    minY = min(y for x, y in obj)
    return [[x - minX, y - minY] for x, y in obj]

def mirrorObj(obj):
    return [[-x, y] for x, y in obj]

def solution(T, objets):
    print("Début de la recherche")
    global solu, histo, H
    solu = creaTab(len(T), len(T[0]))
    histo = []
    historique = []
    H = 0
    P = len(objets)
    
    # Pré-calculer toutes les rotations des objets
    all_rotations = [generateAllRotations(obj) for obj in objets]

    def soluRec(profondeur, courante, historique):
        global solu, histo, H
        if H == 1:
            return
        if surpasse(courante) or profondeur == P:
            return
        LIBRE = chercheLibre(courante)
        for i, j in LIBRE:
            if H == 1:
                return
            for rotation in all_rotations[profondeur]:
                if mettretest(courante, i, j, rotation):
                    mettre(courante, i, j, rotation)
                    historique.append((profondeur, i, j, rotation))
                    if estComplet(courante):
                        solu = copie(courante)
                        histo = historique[:]
                        H = 1
                        return
                    soluRec(profondeur + 1, courante, historique)
                    retire(courante, i, j, rotation)
                    historique.pop()

    soluRec(0, T, historique)
    return histo

# Exemple d'utilisation
T = creaTab(5, 5)
obj = [
    [[0, 0], [1, 0], [2, 0], [3, 0], [0, 1]] ,
[[0, 0], [1, 0], [2, 0], [0, 1], [1, 1]] ,
[[0, 0], [1, 0], [2, 0], [0, 1], [2, 1]] ,
[[0, 0], [1, 0], [1, 1], [1, 2], [2, 2]] ,
[[0, 0], [0, 1], [1, 1], [2, 1], [0, 2]]
]

start = time.time()
print("solu", solution(T, obj))
end = time.time()
print(end - start)
