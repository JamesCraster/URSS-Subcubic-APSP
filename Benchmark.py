from MinPlusAPSP import *
from FloydWarshall import *
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
graphs = [generateGraphOfSize(x) for x in range(1, 100)]

repeats = 10

plt.plot([timeit.timeit(
    "minPlusAPSP("+str(graphs[x])+")", setup="from MinPlusAPSP import minPlusAPSP", number=repeats) for x in range(1, 20)], label="MinPlusAPSP")

plt.plot([timeit.timeit(
    "minPlus("+str(graphs[x])+","+str(graphs[x])+")", setup="from MinPlus import minPlus", number=repeats) for x in range(1, 20)], label="One MinPlus")

plt.plot([timeit.timeit(
    "floydWarshall("+str(graphs[x])+")", setup="from FloydWarshall import floydWarshall", number=repeats) for x in range(1, 20)], label="FloydWarshall")

plt.legend()
plt.show()
