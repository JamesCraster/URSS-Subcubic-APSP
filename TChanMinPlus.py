import math
from functools import reduce
from MinPlus import matrixAdd
import copy
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
        if(A[i]['value'] < B[i]['value']):
            return False
    return True


def removeDuplicates(B):
    A = copy.deepcopy(B)
    for i in range(0, len(A)):
        for j in range(i+1, len(A)):
            if [A[i][y]['value'] for y in range(0, len(A[i]))] == [A[j][y]['value'] for y in range(0, len(A[i]))]:
                del A[j]
    return A


def distanceProduct(A, B, n, d):
    C = [[10000]*n]*n
    for k in range(0, d):
        # Need to recover i and j for which this is true
        first = [[{"i": i, "value": A[i][k] - A[i][j]}
                  for j in range(0, d)] for i in range(0, n)]
        second = [[{"i": i, "value": B[j][i] - A[k][i]}
                   for j in range(0, d)] for i in range(0, n)]
        # Need to redefine less than
        Xk = dominatingPairs(first, second, d)

        print(Xk)
        # for a in Xk:
        #   C[a][b] = A[a.i][k] + B[k][b.i]
    return C


def dominatingPairs(A, B, d):
    if len(A) == 1 and len(B) == 1:
        return [(x, y) for x in A for y in B if dominates(y, x)]
    if len(A) == 0 or len(B) == 0:
        return []
    if d == 0:
        return [(x, y) for x in A for y in B if dominates(y, x)]
    # sort both
    s = sorted(A+B, key=lambda x: x[d-1]['value'])
    leftA = [x for x in A if x[d-1]['value'] <= s[len(s)//2][d-1]['value']]
    rightA = [x for x in A if x[d-1]['value'] > s[len(s)//2][d-1]['value']]
    leftB = [x for x in B if x[d-1]['value'] <= s[len(s)//2][d-1]['value']]
    rightB = [x for x in B if x[d-1]['value'] > s[len(s)//2][d-1]['value']]
    print(leftA)
    print(leftB)

    return dominatingPairs(leftA, leftB, d) + dominatingPairs(rightA, rightB, d) \
        + dominatingPairs(leftA, rightB, d-1)
