import math
from functools import reduce
from MinPlus import *
import copy
from itertools import *


def splitMatrixHorizontal(A, d):
    out = []
    next = []
    for x in range(0, math.ceil(len(A[0])/d)):
        next = []
        for y in range(0, len(A)):
            row = A[y][x*d:min(math.ceil(x*d+d), len(A))]
            while(len(row) < d):
                row.append(1000000)
            next.append(row)

        out.append(next)
    return out


def splitMatrixVertical(A, d):
    out = []
    for x in range(0, math.ceil(len(A)/d)):
        next = A[x*d:min(math.ceil(x*d+d), len(A))]
        while(len(next) < d):
            next.append([1000000]*len(next[0]))
        out.append(next)
    return out


def TChanMinPlus(A, B):
    d = max(math.ceil(0.42 * math.log(len(A))), 1)
    Alist = splitMatrixHorizontal(A, d)
    Blist = splitMatrixVertical(B, d)
    C = []
    for i in range(0, len(Alist)):
        # problem rests with this line
        C.append(distanceProduct(
            Alist[i], Blist[i], len(Alist[i]), d))
    C = reduce(lambda x, y: matrixAdd(x, y), C)
    return C


def dominates(A, B):
    for i in range(0, len(A)):
        if(A[i][1]['val'] < B[i][1]['val']):
            return False
    return True


def distanceProduct(A, B, n, d):
    # which (column/row) does k need to iterate over?
    C = []
    for i in range(0, n):
        C += [[10000]*n]
    for k in range(0, d):
        # Need to recover i and j for which this is true
        first = [[{"i": i, "val": A[i][k] - A[i][j]}
                  for j in range(0, d)] for i in range(0, n)]
        second = [[{"i": i, "val": B[j][i] - B[k][i]}
                   for j in range(0, d)] for i in range(0, n)]
        for a in first:
            for p in range(0, len(a)):
                a[p] = ('A', a[p])
        for b in second:
            for p in range(0, len(b)):
                b[p] = ('B', b[p])
        Xk = dominatingPairs(first, second, d)
        # extract i and j from Xk
        for a in Xk:
            i = a[0][0][1]['i']
            j = a[1][0][1]['i']
            C[i][j] = A[i][k] + B[k][j]
    return C


def dominatingPairs(A, B, d):
    if len(A) + len(B) <= 1:
        return [(x, y) for x in A for y in B if dominates(y, x)]
    if d == 0:
        return [(x, y) for x in A for y in B if dominates(y, x)]
    leftA = []
    leftB = []
    rightA = []
    rightB = []
    S = sorted(A+B, key=lambda x: x[d-1][1]['val'])
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

    return dominatingPairs(leftA, leftB, d) + dominatingPairs(rightA, rightB, d) \
        + dominatingPairs(leftA, rightB, d-1)
