
import numpy as np
inf = 1000000


def minVal(A, B, i, j):
    minVal = inf
    for k in range(0, len(B)):
        minVal = min(A[i][k] + B[k][j], minVal)
    return minVal

# Requirement: number of rows of A == number of columns of B


def newMinPlus(A, B):
    C = np.zeros((len(A), len(B[0])), dtype=int)
    for i in range(0, len(A)):
        for j in range(0, len(B[0])):
            C[i][j] = minVal(A, B, i, j)
    return C


def minPlus(A, B):
    C = []
    for i in range(0, len(A)):
        C.append([minVal(A, B, i, j) for j in range(0, len(B[0]))])
    return C


def argMinPlus(A, B):
    C = []
    for i in range(0, len(A)):
        C.append([])
        for j in range(0, len(B[0])):
            minVal = inf
            minK = inf
            for k in range(0, len(B)):
                if(minVal > A[i][k]+B[k][j]):
                    minVal = A[i][k] + B[k][j]
                    minK = k
            C[i].append(minK)
    return C


def matrixAdd(A, B):
    for i in range(0, len(A)):
        for j in range(0, len(B)):
            A[i][j] = min(A[i][j], B[i][j])
    return A
