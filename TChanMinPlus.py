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
        # Need to redefine less than
        print("first: ", first)
        print("second: ", first)
        Xk = dominatingPairs(first, second, d)
        print("Xk: ", Xk)
        # extract i and j from Xk
        for a in Xk:
            i = a[0][0]['i']
            j = a[1][0]['i']
            print('k: ', k)
            print(i)
            print(j)
            print(A)
            print(B)
            print(C[0][0])
            print(C[i][j])
            C[i][j] = A[i][k] + B[k][j]
            print(C[0][0])
    return C


def dominatingPairs(A, B, d):
    if len(A) == 1 or len(B) == 1:
        return [(x, y) for x in A for y in B if dominates(y, x)]
    if len(A) == 0 or len(B) == 0:
        return []
    if d == 0:
        return [(x, y) for x in A for y in B if dominates(y, x)]
    # sort both
    s = sorted(A+B, key=lambda x: x[d-1]['value'])
    # how splitting works: elements equal to the median before the median are put into left
    # elements equal to the median after the median, or at the median itself, are put into right
    leftA = [A[x] for x in range(0, len(A)) if A[x][d-1]['value'] < s[len(s)//2]
             [d-1]['value'] or (A[x][d-1]['value'] == s[len(s)//2][d-1]['value'] and x < len(s)//2)]
    rightA = [A[x] for x in range(0, len(A)) if A[x][d-1]['value'] > s[len(s)//2]
              [d-1]['value'] or (A[x][d-1]['value'] == s[len(s)//2][d-1]['value'] and x >= len(s)//2)]
    leftB = [B[x] for x in range(0, len(B)) if B[x][d-1]['value'] < s[len(s)//2]
             [d-1]['value'] or (B[x][d-1]['value'] == s[len(s)//2][d-1]['value'] and len(A) + x < len(s)//2)]
    rightB = [B[x] for x in range(0, len(B)) if B[x][d-1]['value'] > s[len(s)//2]
              [d-1]['value'] or (B[x][d-1]['value'] == s[len(s)//2][d-1]['value'] and len(A) + x >= len(s)//2)]

    return dominatingPairs(leftA, leftB, d) + dominatingPairs(rightA, rightB, d) \
        + dominatingPairs(leftA, rightB, d-1)


def dominatingPairsInt(A, B, d):
    if len(A) == 1 or len(B) == 1:
        return [(x, y) for x in A for y in B if dominatesInt(y, x)]
    if len(A) == 0 or len(B) == 0:
        return []
    if d == 0:
        return [(x, y) for x in A for y in B if dominatesInt(y, x)]
    # sort both
    s = sorted(A+B, key=lambda x: x[d-1])
    # how splitting works: elements equal to the median before the median are put into left
    # elements equal to the median after the median, or at the median itself, are put into right
    leftA = [A[x] for x in range(0, len(A)) if A[x][d-1] < s[len(s)//2]
             [d-1] or (A[x][d-1] == s[len(s)//2][d-1] and x < len(s)//2)]
    rightA = [A[x] for x in range(0, len(A)) if A[x][d-1] > s[len(s)//2]
              [d-1] or (A[x][d-1] == s[len(s)//2][d-1] and x >= len(s)//2)]
    leftB = [B[x] for x in range(0, len(B)) if B[x][d-1] < s[len(s)//2]
             [d-1] or (B[x][d-1] == s[len(s)//2][d-1] and len(A) + x < len(s)//2)]
    rightB = [B[x] for x in range(0, len(B)) if B[x][d-1] > s[len(s)//2]
              [d-1] or (B[x][d-1] == s[len(s)//2][d-1] and len(A) + x >= len(s)//2)]
    print(rightA)
    print(rightB)
    return dominatingPairsInt(leftA, leftB, d) + dominatingPairsInt(rightA, rightB, d) \
        + dominatingPairsInt(leftA, rightB, d-1)


def dominatesInt(A, B):
    for i in range(0, len(A)):
        if(A[i] < B[i]):
            return False
    return True
