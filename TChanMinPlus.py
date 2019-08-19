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


def distanceProduct(A, B, n, d):
    # which (column/row) does k need to iterate over?
    C = []
    for i in range(0, n):
        C += [[10000]*d]
    for k in range(0, d):
        # Need to recover i and j for which this is true
        first = [[{"i": i, "value": A[i][k] - A[i][j]}
                  for j in range(0, d)] for i in range(0, n)]
        second = [[{"i": i, "value": B[j][i] - B[k][i]}
                   for j in range(0, d)] for i in range(0, n)]
        Xk = dominatingPairs(first, second, d)
        # extract i and j from Xk
        for a in Xk:
            i = a[0][0]['i']
            j = a[1][0]['i']
            C[i][j] = A[i][k] + B[k][j]
    return C


def dominatingPairs(D, C, d):
    A = copy.deepcopy(D)
    B = copy.deepcopy(C)
    if len(A) == 1 or len(B) == 1:
        return [(x, y) for x in A for y in B if dominates(y, x)]
    if len(A) == 0 or len(B) == 0:
        return []
    if d == 0:
        return [(x, y) for x in A for y in B if dominates(y, x)]
    leftA = []
    leftB = []
    rightA = []
    rightB = []
    # label elements from A and from B
    for a in A:
        for k in range(0, len(a)):
            a[k] = ('A', a[k])
    for b in B:
        for k in range(0, len(b)):
            b[k] = ('B', b[k])
    S = sorted(A+B, key=lambda x: x[d-1][1]['value'])
    # how splitting works: elements equal to the median before the median are put into left
    # elements equal to the median after the median, or at the median itself, are put into right
    for i in range(0, len(S)):
        if S[i][d-1][0] == 'A':
            if i < len(S)//2:
                leftA.append(S[i])
            else:
                rightA.append(S[i])
        if S[i][d-1][0] == 'B':
            if i < len(S)//2:
                leftB.append(S[i])
            else:
                rightB.append(S[i])
    leftE = [[x[1] for x in a] for a in leftA]
    leftF = [[x[1] for x in a] for a in leftB]
    rightE = [[x[1] for x in a] for a in rightA]
    rightF = [[x[1] for x in a] for a in rightB]

    return dominatingPairs(leftE, leftF, d) + dominatingPairs(rightE, rightF, d) \
        + dominatingPairs(leftE, rightF, d-1)
