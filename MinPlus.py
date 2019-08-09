
inf = 1000000


def minPlus(A, B):
    C = []
    for i in range(0, len(A)):
        C.append([])
        for j in range(0, len(A[i])):
            minVal = inf
            for k in range(0, len(A)):
                minVal = min(A[i][k] + B[k][j], minVal)
            C[i].append(minVal)
    return C


def matrixAdd(A, B):
    for i in range(0, len(A)):
        for j in range(0, len(A)):
            A[i][j] = min(A[i][j], B[i][j])
    return A
