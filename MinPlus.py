
inf = 1000000


def minVal(A, B, i, j):
    minVal = inf
    for k in range(0, len(A)):
        minVal = min(A[i][k] + B[k][j], minVal)
    return minVal


def minPlus(A, B):
    C = []
    for i in range(0, len(A)):
        C.append([minVal(A, B, i, j) for j in range(0, len(A[i]))])
    return C


def matrixAdd(A, B):
    for i in range(0, len(A)):
        for j in range(0, len(A)):
            A[i][j] = min(A[i][j], B[i][j])
    return A
