import math
inf = 10000


def naive(A, B):
    d = len(A[0])
    C = []
    for i in range(0, len(A)):
        C.append([])
        for j in range(0, len(B[0])):
            val = 0
            for k in range(0, d):
                val += A[i][k] * B[k][j]
            C[i].append(val)
    return C


def padMatrix(X):
    initWidth = len(X[0])
    initHeight = len(X)
    width = nextPowerOf2(len(X))
    height = nextPowerOf2(len(X[0]))
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
    return math.ceil(float(n)/2) * 2


def matrixAdd(A, B):
    C = []
    for i in range(0, len(A)):
        C.append([])
        for j in range(0, len(B)):
            C[i].append(A[i][j] + B[i][j])
    return C


def matrixSub(A, B):
    print(len(A), len(A[0]), len(B), len(B[0]))
    C = []
    for i in range(0, len(A)):
        C.append([])
        for j in range(0, len(B)):
            C[i].append(A[i][j] - B[i][j])
    return C


def dim(A):
    return (len(A), len(A[0]))


def strassen(A, B):
    # For small cases, it is more efficient to solve immediately
    if(len(A) <= 20 and len(B[0]) <= 20):
        return naive(A, B)
    else:
        padMatrix(A)
        padMatrix(B)
        #print(len(A), len(A[0]), len(B), len(B[0]))
        h = len(A)//2
        A11 = [r[:h] for r in A[:h]]
        A12 = [r[h:] for r in A[:h]]
        A21 = [r[:h] for r in A[h:]]
        A22 = [r[h:] for r in A[h:]]
        #print(dim(A11), dim(A12), dim(A21), dim(A22))

        h = len(B)//2
        B11 = [r[:h] for r in B[:h]]
        B12 = [r[h:] for r in B[:h]]
        B21 = [r[:h] for r in B[h:]]
        B22 = [r[h:] for r in B[h:]]
        #print(dim(B11), dim(B12), dim(B21), dim(B22))
        M1 = strassen(matrixAdd(A11, A22), matrixAdd(B11, B22))
        print('init: ', dim(B11), dim(B12), dim(B21), dim(B22))
        M2 = strassen(matrixAdd(A21, A22), B11)
        print('end: ', dim(B11), dim(B12), dim(B21), dim(B22))
        M3 = strassen(A11, matrixSub(B12, B22))

        M4 = strassen(A22, matrixSub(B21, B11))
        M5 = strassen(matrixAdd(A11, A12), B22)
        M6 = strassen(matrixSub(A21, A11), matrixAdd(B11, B12))
        M7 = strassen(matrixSub(A12, A22), matrixAdd(B21, B22))

        '''print(dim(M1), dim(M2), dim(M3), dim(M4),
              dim(M5), dim(M6), dim(M7))

        print(dim(matrixAdd(M1, M4)))
        print(dim(matrixSub(matrixAdd(M1, M4), M5)))
        '''

        C11 = matrixAdd(matrixSub(matrixAdd(M1, M4), M5), M7)
        C12 = matrixAdd(M3, M5)
        C21 = matrixAdd(M2, M4)
        C22 = matrixAdd(matrixAdd(matrixSub(M1, M2), M3), M6)

        newMatrixLeft = C11 + C21
        newMatrixRight = C12 + C22
        for i in range(0, len(newMatrixLeft)):
            newMatrixLeft[i] += newMatrixRight[i]
    return newMatrixLeft
