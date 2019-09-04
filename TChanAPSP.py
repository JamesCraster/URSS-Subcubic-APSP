'''
T.Chan's algorithm:
The reduction to min-plus matrix multiplication:

The first step is to reduce APSP to min-plus matrix multiplication neatly.
The simplest way to is to min-plus product the adjacency matrix with itself n times (the proof that this provides a solution to APSP is simple by induction)
Unfortunately, this would take O(n * n^3) = O(n^4), worse that Floyd-Warshall.
This can be done faster using exponentiation by repeated squaring, requiring log(n) many min-plus products, but again this logarithmic factor is too large.

The best method I've found is featured in The Design and Analysis of Computer Algorithms (Aho, Hopcroft, Ullman) sec. 5.9, Corollary 2 and works something like this:

Corollary 2: The time necessary to compute the closure of a matrix of nonnegative reals is of the same order as the time to compute the product of 2 matrices of this type.
[Aho, A.V., Hopcroft, J.E., Ullman, J.D.: The Design and Analysis of Computer Algorithms. Addison–Wesley, Reading (1974)]
NB: You do not need to pad to the nearest power of two! Simply padding to the next even number is sufficient and results in negligible penalty for square matrices.

Running time Analysis:
Experimentally, this method of computing the closure of a matrix is three to four times slower than a single min-plus product, which fits with the theory.
The recurrence relation: (letting the size of the matrix = 2^k for some k; we pad the matrix until such a k exists.)
Two closures, six multiplications, two additions (let M(n) be time taken to multiply two matrices of size n.)
T(1)= 1,
T(2^k) <= 2T(2^(k-1)) + 6M(2^(k-1)) + 2*(2^(2k-2)) for k > 1

Claim: there exists c such that T(2^k) <= cM(2^k)
It is proven (theoretically) that such a c exists, provided M(2n) >= 4*M(n), which is clearly true in this case.
I would expect in practice that c <= 8, because the dimension, n, is at worst doubled (to next power of 2) and then 
eight O(n^3) operations are applied to the four quarters (of dimension one half), so 6 times slower than min-plus product.

Solving dominating pairs:
[Preparata, F.P., Shamos, M.I.: Computational Geometry: An Introduction. Springer, New York (1985)]

NB: when it comes to sorting, finding the median in O(nlogn) is sufficient, because n^(1+epsilon) dominates nlogn, 
for all epsilon > 0.
Finding the median in linear time would require a linear-time sweep to partition elements into left, middle, right,
and then taking left + some middle, right + rest of middle.
'''

from TChanMinPlus import TChanMinPlus
from MinPlus import matrixAdd
import copy
inf = 1000000


def nextEven(n):
    return n + n % 2


def padMatrix(Y):
    X = [i for i in Y]
    initWidth = len(X[0])
    initHeight = len(X)
    width = nextEven(len(X))
    height = nextEven(len(X[0]))
    n = max(width, height)

    for i in range(0, len(X)):
        for j in range(0, n-initWidth):
            X[i].append(inf)
    for i in range(0, n-initHeight):
        X.append([inf] * n)

    for i in range(0, len(X)):
        for j in range(0, len(X[i])):
            if i == j:
                X[i][j] = 0
    return X


def dim(A):
    return (len(A), len(A[0]))


def fastClosureT(Y):
    if(len(Y) == 1):
        return [[0]]
    initLength = len(Y)
    X = padMatrix(Y)
    # divide the matrix into four quadrants
    h = len(X)//2
    A = [r[:h] for r in X[:h]]
    B = [r[h:] for r in X[:h]]
    C = [r[:h] for r in X[h:]]
    D = [r[h:] for r in X[h:]]
    T1 = fastClosureT(D)
    T2 = TChanMinPlus(B, T1)
    E = fastClosureT(matrixAdd(A, TChanMinPlus(T2, C)))
    F = TChanMinPlus(E, T2)
    T3 = TChanMinPlus(T1, C)
    G = TChanMinPlus(T3, E)
    H = matrixAdd(T1, TChanMinPlus(G, T2))
    newMatrixLeft = E + G
    newMatrixRight = F + H
    for i in range(0, len(newMatrixLeft)):
        newMatrixLeft[i] += newMatrixRight[i]
    return [r[:initLength] for r in newMatrixLeft[:initLength]]


def fastClosureAPSPT(A):
    return fastClosureT(A)
