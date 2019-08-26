
import timeit
import random
import matplotlib.pyplot as plt
from MatrixAlgorithms import *


def generateMatrixOfSize(n):
    graph = []
    for i in range(0, n):
        graph.append([])
        for j in range(0, n):
            graph[i].append(random.randint(0, 10))
    return graph


repeats = 1
minrange = 10
maxrange = 30
matrices = [(generateMatrixOfSize(x), generateMatrixOfSize(x))
            for x in range(1, 50)]

passes = True
for matrix in matrices:
    print(strassen(matrix[0], matrix[1]) != naive(matrix[0], matrix[1]))

if passes:
    print("All tests pass")
else:
    print("Test failed")

'''plt.plot([timeit.timeit(
    "naive("+str(matrices[x][0])+","+str(matrices[x][1])+")", setup="from MatrixAlgorithms import naive", number=repeats) for x in range(minrange, maxrange)], label="Naive")

plt.plot([timeit.timeit(
    "strassen("+str(matrices[x][0])+","+str(matrices[x][1])+")", setup="from MatrixAlgorithms import strassen", number=repeats) for x in range(minrange, maxrange)], label="Naive")
'''

plt.legend()
plt.show()
