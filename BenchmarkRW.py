from MinPlusAPSP import *
from FloydWarshall import *
from MPAPSPFastExp import *
from FastClosure import *
from TChanAPSP import *
import timeit
import random
import matplotlib.pyplot as plt


def generateGraphOfSize(n):
    graph = []
    for i in range(0, n):
        graph.append([])
        for j in range(0, n):
            # It seems that it is a requirement for these algorithms that the distance from any vertex to itself must be zero. This is potentially a bug, since this is not true for all vertices.
            if i != j:
                graph[i].append(random.randint(0, 10))
            else:
                graph[i].append(0)
    return graph


# Note the distinction between 0 (edge of no length) and +inf (no edge at all) in these algorithms
repeats = 1
minrange = 0
maxrange = 20
graphs = [generateGraphOfSize(x) for x in range(1, 120)]

plt.plot([timeit.timeit(
    "minPlusAPSP("+str(graphs[x])+")", setup="from MinPlusAPSP import minPlusAPSP", number=repeats) for x in range(minrange, maxrange)], label="MinPlusAPSP")

plt.plot([timeit.timeit(
    "minPlusAPSPFastExp("+str(graphs[x])+")", setup="from MPAPSPFastExp import minPlusAPSPFastExp", number=repeats) for x in range(minrange, maxrange)], label="MinPlusAPSP (Exponent. by squaring)")

plt.plot([timeit.timeit(
    "fastClosureAPSP("+str(graphs[x])+")", setup="from FastClosure import fastClosureAPSP", number=repeats) for x in range(minrange, maxrange)], label="FastClosureAPSP")

plt.plot([timeit.timeit(
    "floydWarshall("+str(graphs[x])+")", setup="from FloydWarshall import floydWarshall", number=repeats) for x in range(minrange, maxrange)], label="FloydWarshall")

plt.plot([timeit.timeit(
    "RWilliamsMinPlus("+str(graphs[x])+","+str(graphs[x])+")", setup="from RWilliamsMinPlus import RWilliamsMinPlus", number=repeats) for x in range(minrange, maxrange)], label="RWilliams")

plt.legend()
plt.show()
