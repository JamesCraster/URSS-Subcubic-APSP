inf = 1000000


def minVal(A, B, i, j):
    minVal = inf
    for k in range(0, len(B)):
        minVal = min(A[i][k] + B[k][j], minVal)
    return minVal


def minPlus(A, B):
    """ The only requirement of min-plus multiplication is that the number of rows of A == number of columns of B """
    C = []
    for i in range(0, len(A)):
        C.append([minVal(A, B, i, j) for j in range(0, len(B[0]))])
    return C


def argMinPlus(A, B):
    """ Returns the matrix of k values st C[i][j] = A[i][k] + B[k][j], that is, those k values producing the minimum values"""
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
    """ In tropical algebra, adding matrices is equivalent to taking the elementwise minimum """
    for i in range(0, len(A)):
        for j in range(0, len(B)):
            A[i][j] = min(A[i][j], B[i][j])
    return A
