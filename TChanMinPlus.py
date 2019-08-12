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
    C = []
    for i in range(0, len(Alist)):
        C.append(distanceProduct(Alist[i], Blist[i], len(Alist[0])))
    C = reduce(lambda x, y: matrixAdd(x, y), C)
    return C


def dominatingPairs(red, blue):
    pass


def dominates(A, B):
    for i in range(0, len(A)):
        if(A[i] < B[i]):
            return False
    return True


def distanceProduct(A, B, d):
    if len(A) == 1 and len(B) == 1:
        return [(x, y) for x in A for y in B if dominates(y, x)]
    if len(A) == 0 or len(B) == 0:
        return []
    if d == 0:
        return [(x, y) for x in A for y in B if dominates(y, x)]
    # sort both
    s = sorted(A+B, key=lambda x: x[d-1])
    # get access to left/right
    # print(s)
    left = s[:len(s)//2]
    right = s[len(s)//2:]
    leftA = [x for x in A if x[d-1] <= s[len(s)//2][d-1]]
    rightA = [x for x in A if x[d-1] > s[len(s)//2][d-1]]
    leftB = [x for x in B if x[d-1] <= s[len(s)//2][d-1]]
    rightB = [x for x in B if x[d-1] > s[len(s)//2][d-1]]
    # print(left)
    # print(right)
    print(leftA)
    print(leftB)
    # print(rightA)
    # print(rightB)
    # merge calls to smaller cases
    # recursion error here when run on distanceProduct([[5,6], [3,4]],[[1,2],[7,8]],2)
    # distanceProduct(leftA, leftB, d) +
    return distanceProduct(leftA, leftB, d) + distanceProduct(rightA, rightB, d) \
        + distanceProduct(leftA, rightB, d-1)
