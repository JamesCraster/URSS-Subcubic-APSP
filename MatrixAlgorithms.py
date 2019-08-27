import math
import numpy as np
import copy
inf = 10000


def naive(A, B):
    d = len(A[0])
    C = np.zeros((len(A), len(B[0])))
    for i in range(0, len(A)):
        for j in range(0, len(B[0])):
            C[i][j] = np.dot(A[i, :], B[:, j])
    return C


def padMatrix(Y):
    X = [i for i in Y]
    initWidth = len(X[0])
    initHeight = len(X)
    width = nextMultipleOf2(len(X))
    height = nextMultipleOf2(len(X[0]))
    n = max(width, height)

    for i in range(0, len(X)):
        for j in range(0, n-initWidth):
            X[i].append(0)
    for i in range(0, n-initHeight):
        X.append([0] * n)
    return X


def nextPowerOf2(n):
    if n == 0:
        return 1
    if n & (n - 1) == 0:
        return n
    while n & (n - 1) > 0:
        n &= (n - 1)
    return n << 1


def nextMultipleOf2(n):
    return n + n % 2


def matrixAdd(A, B):
    C = []
    for i in range(0, len(A)):
        C.append([])
        for j in range(0, len(B)):
            C[i].append(A[i][j] + B[i][j])
    return C


def matrixSub(A, B):
    C = []
    for i in range(0, len(A)):
        C.append([])
        for j in range(0, len(B)):
            C[i].append(A[i][j] - B[i][j])
    return C


def dim(A):
    return (len(A), len(A[0]))


def strassen(C, D):
    n = len(C)
    # For small cases, it is more efficient to solve immediately
    if(len(C) < 128 and len(D[0]) < 128):
        return naive(C, D)
    else:
        A = padMatrix(C)
        B = padMatrix(D)

        h = len(A)//2
        A11 = [r[:h] for r in A[:h]]
        A12 = [r[h:] for r in A[:h]]
        A21 = [r[:h] for r in A[h:]]
        A22 = [r[h:] for r in A[h:]]

        h = len(B)//2
        B11 = [r[:h] for r in B[:h]]
        B12 = [r[h:] for r in B[:h]]
        B21 = [r[:h] for r in B[h:]]
        B22 = [r[h:] for r in B[h:]]
        M1 = strassen(matrixAdd(A11, A22), matrixAdd(B11, B22))
        M2 = strassen(matrixAdd(A21, A22), B11)
        M3 = strassen(A11, matrixSub(B12, B22))
        M4 = strassen(A22, matrixSub(B21, B11))
        M5 = strassen(matrixAdd(A11, A12), B22)
        M6 = strassen(matrixSub(A21, A11), matrixAdd(B11, B12))
        M7 = strassen(matrixSub(A12, A22), matrixAdd(B21, B22))
        C11 = matrixAdd(matrixSub(matrixAdd(M1, M4), M5), M7)
        C12 = matrixAdd(M3, M5)
        C21 = matrixAdd(M2, M4)
        C22 = matrixAdd(matrixAdd(matrixSub(M1, M2), M3), M6)

        newMatrixLeft = C11 + C21
        newMatrixRight = C12 + C22
        for i in range(0, len(newMatrixLeft)):
            newMatrixLeft[i] += newMatrixRight[i]
    return [r[:n] for r in newMatrixLeft[:n]]
