
import math
import copy
import random
from MinPlus import *
from functools import reduce


def splitMatrixHorizontal(A, d):
    # O(n^2) op
    out = []
    next = []
    for x in range(0, int(math.ceil(len(A[0])/d))):
        next = []
        for y in range(0, len(A)):
            row = A[y][x*d:min(math.ceil(x*d+d), len(A))]
            while(len(row) < d):
                row.append(1000000)
            next.append(row)

        out.append(next)
    return out


def splitMatrixVertical(A, d):
    # O(n^2) op
    out = []
    for x in range(0, math.ceil(len(A)/d)):
        next = A[x*d:min(math.ceil(x*d+d), len(A))]
        while(len(next) < d):
            next.append([1000000]*len(next[0]))
        out.append(next)
    return out


def RWilliamsMinPlus(A, B, d=None):
    if d is None:
        d = int(max(math.ceil(0.42 * math.log(len(A))), 1))
    # O(n^2 operations)
    Alist = splitMatrixHorizontal(A, d)
    Blist = splitMatrixVertical(B, d)
    C = []
    # Runs n/d times
    for i in range(0, len(Alist)):
        C.append(rectangularMinPlus(Alist[i], Blist[i]))
    # O(n^3/d) operation
    C = reduce(lambda x, y: matrixAdd(x, y), C)
    return C


def rectangularMinPlus(C, D):
    n = len(C)
    d = len(C[0])
    # Enforce a unique minimum
    # Both multiplication by addition and the trivial multiplication method
    # take O(n^2) for two n-digit numbers. Therefore trivial multiplication used.
    A = []
    for i in range(0, n):
        A.append([])
        for j in range(0, d):
            A[i].append(C[i][j] * (n+1) + j)
    B = []
    for i in range(0, d):
        B.append([])
        for j in range(0, n):
            B[i].append(D[i][j] * (n+1))
    # Fredman's trick:
    Af = []
    for i in range(0, n):
        Af.append([])
        for k in range(0, d):
            Af[i].append([])
            for otherK in range(0, d):
                Af[i][k].append(A[i][k]-A[i][otherK])

    Bf = []
    for k in range(0, d):
        Bf.append([])
        for otherK in range(0, d):
            Bf[k].append([])
            for j in range(0, n):
                Bf[k][otherK].append(B[otherK][j]-B[k][j])

    # Finish replacement on Af and Bf:
    S = []
    for k in range(0, len(A[0])):
        S.append([])
        for otherK in range(0, len(A[0])):
            new = sorted([(Af[i][k][otherK], 'A', i)
                          for i in range(0, n)] + [(Bf[k][otherK][i], 'B', i) for i in range(0, n)])
            for rank, (value, parentList, index) in enumerate(new):
                if parentList == 'A':
                    Af[index][k][otherK] = rank
                else:
                    Bf[k][otherK][index] = rank

    # Everything above this line runs (both theoretically and in practice) in O(n·d^2·logn)
    # Here we begin to use circuits to solve our problem
    kMatrix = []
    for i in range(0, n):
        kMatrix.append([])
        for j in range(0, n):
            kMatrix[i].append(circuitSolve(Af, Bf, d, i, j))

    out = []
    for i in range(0, len(kMatrix)):
        out.append([])
        for j in range(0, len(kMatrix[i])):
            k = kMatrix[i][j]
            out[i].append((A[i][k] + B[k][j] - k)//(n+1))
    return out


def trivialCircuitSolve(Af, Bf, d, i, j):
    value = ""
    bitCount = int(math.log2(d)) + 1
    for l in range(0, bitCount):
        out = False
        for k in range(0, d):
            andResult = False
            binK = bin(k)[2:].zfill(bitCount)
            # any index out of range should point to 0.
            if binK[-(l+1)] == '1':
                andResult = True
                for otherK in range(0, d):
                    comparison = Af[i][k][otherK] <= Bf[k][otherK][j]
                    andResult = andResult and comparison
            # Note here we use XOR
            out = out ^ andResult
        if(out):
            value = "1" + value
        else:
            value = "0" + value
    return int(value, 2)


def circuitSolve(Af, Bf, d, i, j):
    value = ""
    bitCount = int(math.log2(d)) + 1
    for l in range(0, bitCount):
        out = False
        for k in range(0, d):
            andResult = False
            binK = bin(k)[2:].zfill(bitCount)
            # any index out of range should point to 0.
            if binK[-(l+1)] == '1':
                andResult = RazborovSmolensky(
                    [Af[i][k][otherK] <= Bf[k][otherK][j] for otherK in range(0, d)])

            # Note here we use XOR
            out = out ^ andResult
        if(out):
            value = "1" + value
        else:
            value = "0" + value
    return min(int(value, 2), d-1)


def RazborovSmolensky(atoms):
    e = int(math.log2(len(atoms))) + 9
    coefficients = []
    for i in range(0, e):
        coefficients.append([])
        for j in range(0, len(atoms)):
            coefficients[i].append(round(random.random()))

    out = True
    for i in range(0, e):
        innerResult = False
        for j in range(0, len(atoms)):
            innerResult = innerResult ^ (coefficients[i][j] * (not atoms[j]))
        out = out and (not innerResult)
    return out


def leq(a, b):
    # compare entries of a and b as bit strings
    pass


A = [[0, 8, 7, 7, 10], [10, 0, 3, 8, 6], [
    3, 2, 0, 10, 4], [0, 8, 8, 0, 10], [10, 0, 8, 8, 0]]
RWilliamsMinPlus(copy.deepcopy(A), copy.deepcopy(A))
