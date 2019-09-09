import math
from functools import reduce
from MinPlus import *
import copy
from itertools import *
import random


def quickselect_median(l, d, pivot_fn=random.choice):
    if len(l) % 2 == 1:
        return quickselect(l, len(l) / 2, d, pivot_fn)
    else:
        return quickselect(l, len(l) / 2 - 1, d, pivot_fn)


def quickselect(l, k, d, pivot_fn):
    """
    Select the kth element in l (0 based)
    :param l: List of numerics
    :param k: Index
    :param pivot_fn: Function to choose a pivot, defaults to random.choice
    :return: The kth element of l
    """
    if len(l) == 1:
        assert k == 0
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el[d-1][1]['val'] < pivot[d-1][1]['val']]
    highs = [el for el in l if el[d-1][1]['val'] > pivot[d-1][1]['val']]
    pivots = [el for el in l if el[d-1][1]['val'] == pivot[d-1][1]['val']]

    if k < len(lows):
        return quickselect(lows, k, d, pivot_fn)
    elif k < len(lows) + len(pivots):
        # We got lucky and guessed the median
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), d,  pivot_fn)


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


def dim(A):
    return (len(A), len(A[0]))


def TChanMinPlus(A, B, d=None):
    if d is None:
        d = int(max(math.ceil(0.42 * math.log(len(A))), 1))
    # O(n^2 operations)
    Alist = splitMatrixHorizontal(A, d)
    Blist = splitMatrixVertical(B, d)
    C = []
    print('Alist', len(Alist))
    # Runs n/d times
    for i in range(0, len(Alist)):
        C.append(distanceProduct(
            Alist[i], Blist[i], len(Alist[i]), d))
    # O(n^3/d) operation
    print('len(C)', len(C))
    C = reduce(lambda x, y: matrixAdd(x, y), C)
    return C


def dominates(A, B, c):
    for i in range(0, c):
        if(A[i][1]['val'] < B[i][1]['val']):
            return False
    return True


def distanceProduct(A, B, n, d):
    C = []
    for i in range(0, n):
        C += [[10000]*n]
    for k in range(0, d):
        # Need to recover i and j for which this is true
        # O(nd)
        first = [[{"i": i, "val": A[i][k] - A[i][j]}
                  for j in range(0, d)] for i in range(0, n)]
        second = [[{"i": i, "val": B[j][i] - B[k][i]}
                   for j in range(0, d)] for i in range(0, n)]
        # O(nd)
        for a in first:
            for p in range(0, len(a)):
                a[p] = ('A', a[p])
        for b in second:
            for p in range(0, len(b)):
                b[p] = ('B', b[p])
        Xk = []
        # This line will be run n times  (must be dominating the running time)
        Xk = dominatingPairs(first, second, d)
        # extract i and j from Xk
        for a in Xk:
            i = a[0][0][1]['i']
            j = a[1][0][1]['i']
            C[i][j] = A[i][k] + B[k][j]
    return C

# This function dominates the algorithm's running time for small n.
# According to theoretical analyis, for some large n this should no longer dominate.
# It seems the revised analysis O(n^1+epsilon) is worse than O(n^3 / log(n)) for small values.


def dominatingPairs(A, B, d, sortedD=False):
    if len(A) + len(B) <= 1:
        return []
    if d == 0:
        return [(x, y) for x in A for y in B]
    if d == 1:
        return [(x, y) for x in A for y in B if dominates(x, y, 1)]
    if d == 2:
        return [(x, y) for x in A for y in B if dominates(x, y, 2)]
    leftA = []
    leftB = []
    rightA = []
    rightB = []
    #median = quickselect_median(A+B, d)
    # if not sortedD:
    #   S = sorted(A+B, key=lambda x: x[d-1][1]['val'])
    # else:
    S = A+B
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

    return dominatingPairs(leftA, leftB, d, True) + dominatingPairs(rightA, rightB, d, True) \
        + dominatingPairs(leftA, rightB, d-1, False)


def generateGraphOfSize(n):
    graph = []
    for i in range(0, n):
        graph.append([])
        for j in range(0, n):
            # It seems that it is a requirement for these algorithms that the distance from any vertex to itself must be zero. This is potentially a bug, since this is not true for all vertices.
            if i != j:
                graph[i].append(random.randint(1, 10))
            else:
                graph[i].append(0)
    return graph


# Note the distinction between 0 (edge of no length) and +inf (no edge at all) in these algorithms
repeats = 1
graphs = [generateGraphOfSize(x) for x in range(200, 201, 10)]
TChanMinPlus(graphs[0], graphs[0])
