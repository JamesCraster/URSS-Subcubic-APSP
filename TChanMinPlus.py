import math
from functools import reduce
from MinPlus import matrixAdd
from itertools import *


def splitMatrixHorizontal(A, d):
    out = []
    next = []
    for x in range(0, math.ceil(len(A)/d)):
        next = []
        for y in range(0, len(A)):
            next.append(A[y][x*d:min(math.ceil(x*d+d), len(A))])

        out.append(next)
    return out


def splitMatrixVertical(A, d):
    out = []
    for x in range(0, math.ceil(len(A)/d)):
        out.append(A[x*d:min(math.ceil(x*d+d), len(A))])
    return out


def TChanMinPlus(A, B):
    d = 2
    Alist = splitMatrixHorizontal(A, d)
    Blist = splitMatrixVertical(B, d)
    print(Alist)
    print(Blist)
    C = []
    for i in range(0, len(Alist)):
        C.append(distanceProduct(
            Alist[i], Blist[i], len(Alist), len(Alist[0])))
    C = reduce(lambda x, y: matrixAdd(x, y), C)
    return C


def dominates(A, B):
    for i in range(0, len(A)):
        if(A[i] < B[i]):
            return False
    return True


def distanceProduct(A, B, n, d):
    C = [[10000]*n]*n
    for k in range(0, d):
        Xk = dominatingPairs([[(A[i][k] - A[i][j])
                               for j in range(1, d)] for i in range(1, n)], [[(B[j][i] - A[k][i])
                                                                              for j in range(1, d)] for i in range(1, n)], d)

        print(Xk)
        for (i, j) in Xk:
            C[i][j] = A[i][k] + B[k][j]
    return C


def dominatingPairs(A, B, d):
    if len(A) == 1 and len(B) == 1:
        return [(x, y) for x in A for y in B if dominates(y, x)]
    if len(A) == 0 or len(B) == 0:
        return []
    if d == 0:
        return [(x, y) for x in A for y in B if dominates(y, x)]
    # sort both
    s = sorted(A+B, key=lambda x: x[d-1])
    leftA = [x for x in A if x[d-1] <= s[len(s)//2][d-1]]
    rightA = [x for x in A if x[d-1] > s[len(s)//2][d-1]]
    leftB = [x for x in B if x[d-1] <= s[len(s)//2][d-1]]
    rightB = [x for x in B if x[d-1] > s[len(s)//2][d-1]]
    return dominatingPairs(leftA, leftB, d) + dominatingPairs(rightA, rightB, d) \
        + dominatingPairs(leftA, rightB, d-1)
