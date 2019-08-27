from MinPlus import minPlus, matrixAdd
import copy
inf = 1000000


def nextEven(n):
    return n + n % 2


def padMatrix(Y):
    X = [i for i in Y]
    initWidth = len(X[0])
    initHeight = len(X)
    width = nextEven(len(X))
    height = nextEven(len(X[0]))
    n = max(width, height)

    for i in range(0, len(X)):
        for j in range(0, n-initWidth):
            X[i].append(inf)
    for i in range(0, n-initHeight):
        X.append([inf] * n)

    for i in range(0, len(X)):
        for j in range(0, len(X[i])):
            if i == j:
                X[i][j] = 0
    return X


def fastClosure(Y):
    if(len(Y) == 1):
        return [[0]]
    initLength = len(Y)
    X = padMatrix(Y)
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
    return [r[:initLength] for r in newMatrixLeft[:initLength]]


def fastClosureAPSP(A):
    return fastClosure(A)
