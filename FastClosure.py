from MinPlus import minPlus, matrixAdd
import copy
inf = 1000000


def nextPowerOf2(n):
    if n == 0:
        return 1
    if n & (n - 1) == 0:
        return n
    while n & (n - 1) > 0:
        n &= (n - 1)
    return n << 1


def padMatrix(X):
    n = nextPowerOf2(len(X))
    initLength = len(X)
    # pad the matrix up to the next power of two
    for i in range(0, len(X)):
        for j in range(0, n-len(X)):
            X[i].append(inf)
    for i in range(initLength, n):
        X.append([])
        for j in range(0, n):
            X[i].append(inf)
    for i in range(0, len(X)):
        for j in range(0, len(X[i])):
            if i == j:
                X[i][j] = 0
    return X


def unpadMatrix(X, initLength):
    C = []
    for i in range(0, initLength):
        C.append([])
        for j in range(0, initLength):
            C[i].append(X[i][j])
    return C


def fastClosure(X):
    if(len(X) == 1):
        return [[0]]
    padMatrix(X)
    # divide the matrix into four quadrants
    h = len(X)//2
    A = [r[:h] for r in X[:h]]
    B = [r[h:] for r in X[:h]]
    C = [r[:h] for r in X[h:]]
    D = [r[h:] for r in X[h:]]
    T1 = fastClosure(D)
    T2 = minPlus(B, T1)
    E = fastClosure(matrixAdd(A, minPlus(T2, C)))
    F = minPlus(E, T2)
    T3 = minPlus(T1, C)
    G = minPlus(T3, E)
    H = matrixAdd(T1, minPlus(G, T2))
    newMatrixLeft = E + G
    newMatrixRight = F + H
    for i in range(0, len(newMatrixLeft)):
        newMatrixLeft[i] += newMatrixRight[i]
    return newMatrixLeft


def fastClosureAPSP(A):
    return unpadMatrix(fastClosure(copy.deepcopy(A)), len(A))
