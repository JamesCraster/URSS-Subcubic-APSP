
import timeit
import random
import numpy as np
import matplotlib.pyplot as plt
from MatrixAlgorithms import *


def generateMatrixOfSize(n):
    return np.random.randint(0, 100, (n, n))


repeats = 1
minrange = 30
maxrange = 90
matrices = [(generateMatrixOfSize(x), generateMatrixOfSize(x))
            for x in range(2, 100)]

passes = True
for matrix in matrices:
    '''if(strassen(matrix[0], matrix[1]) != naive(matrix[0], matrix[1])):
        passes = False'''

if passes:
    print("All tests pass")
else:
    print("Test failed")

x = 29
plt.plot([timeit.timeit(
    "np.dot(matrices[x][0], matrices[x][1])", number=repeats, globals=globals()) for x in range(minrange, maxrange)], label="Numpy Dot")

plt.plot([timeit.timeit(
    "np.matmul(matrices[x][0], matrices[x][1])",  globals=globals(), number=repeats) for x in range(minrange, maxrange)], label="Numpy Matmul")

plt.plot([timeit.timeit(
    "naive(matrices[x][0], matrices[x][1])",  globals=globals(), number=repeats) for x in range(minrange, maxrange)], label="Naive")

'''plt.plot([timeit.timeit(
    "strassen("+str(matrices[x][0])+","+str(matrices[x][1])+")", setup="from MatrixAlgorithms import strassen", number=repeats) for x in range(minrange, maxrange)], label="Strassen")'''

plt.legend()
plt.show()
