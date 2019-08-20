from TChanMinPlus import TChanMinPlus
from MinPlus import matrixAdd
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


def fastClosureT(X):
    if(len(X) == 1):
        return [[0]]
    padMatrix(X)
    # divide the matrix into four quadrants
    h = len(X)//2
    A = [r[:h] for r in X[:h]]
    B = [r[h:] for r in X[:h]]
    C = [r[:h] for r in X[h:]]
    D = [r[h:] for r in X[h:]]
    T1 = fastClosureT(D)
    T2 = TChanMinPlus(B, T1)
    E = fastClosureT(matrixAdd(A, TChanMinPlus(T2, C)))
    F = TChanMinPlus(E, T2)
    T3 = TChanMinPlus(T1, C)
    G = TChanMinPlus(T3, E)
    H = matrixAdd(T1, TChanMinPlus(G, T2))
    newMatrixLeft = E + G
    newMatrixRight = F + H
    for i in range(0, len(newMatrixLeft)):
        newMatrixLeft[i] += newMatrixRight[i]
    return newMatrixLeft


def fastClosureAPSPT(A):
    return unpadMatrix(fastClosureT(copy.deepcopy(A)), len(A))
