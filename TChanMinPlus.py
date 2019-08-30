import math
from functools import reduce
from MinPlus import *
import copy
from itertools import *
import random

# O(n^2 op)


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

# O(n^2) op


def splitMatrixVertical(A, d):
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
    if(len(A) <= 18 and len(B[0]) <= 18):
        return minPlus(A, B)
    print('n ', len(A))
    if d is None:
        d = int(max(math.ceil(0.42 * math.log(len(A))), 1))
    # O(n^2 operations)
    Alist = splitMatrixHorizontal(A, d)
    Blist = splitMatrixVertical(B, d)
    C = []
    print('Alist', len(Alist))
    # Runs n/d times
    for i in range(0, len(Alist)):
        # What is the running time of this?
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


def dominatingPairs(A, B, d):
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

# plt.plot([timeit.timeit(
#   "newMinPlus("+str(graphs[x])+","+str(graphs[x])+")", setup="from MinPlus import newMinPlus", number=repeats) for x in range(0, len(graphs))], label="MinPlus")
TChanMinPlus(graphs[0], graphs[0])
