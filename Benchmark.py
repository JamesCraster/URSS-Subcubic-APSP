from MinPlusAPSP import *
from FloydWarshall import *
from MPAPSPFastExp import *
from FastClosure import *
from TChanAPSP import *
from TChanMinPlus import *
import timeit
import random
import matplotlib.pyplot as plt


from TChanMinPlus import *


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
graphs = [generateGraphOfSize(x) for x in range(2, 100, 10)]

# plt.plot([timeit.timeit(
#   "newMinPlus("+str(graphs[x])+","+str(graphs[x])+")", setup="from MinPlus import newMinPlus", number=repeats) for x in range(0, len(graphs))], label="MinPlus")
# TChanMinPlus(graphs[0], graphs[0])

'''print(timeit.timeit("minPlus("+str(graphs[0])+","+str(
    graphs[0])+")", setup="from MinPlus import minPlus", number=repeats))

'''
plt.plot([timeit.timeit(
    "minPlus("+str(graphs[x])+","+str(graphs[x])+")", setup="from MinPlus import minPlus", number=repeats) for x in range(0, len(graphs))], label="OldMinPlus")

# print(timeit.timeit(
# "TChanMinPlus("+str(graphs[0])+","+str(graphs[0])+")", setup="from TChanMinPlus import TChanMinPlus", number=repeats))

# plt.plot([timeit.timeit(
#   "TChanMinPlus("+str(graphs[x])+","+str(graphs[x])+")", setup="from TChanMinPlus import TChanMinPlus", number=repeats) for x in range(0, len(graphs))], label="TChanMinPlus")

plt.plot([timeit.timeit(
    "TChanMinPlus("+str(graphs[x])+","+str(graphs[x])+")", setup="from TChanMinPlus import TChanMinPlus", number=repeats) for x in range(0, len(graphs))], label="TChanMinPlus2")

'''
plt.plot([timeit.timeit(
    "TChanMinPlus("+str(graphs[x])+","+str(graphs[x])+")", setup="from TChanMinPlus import TChanMinPlus", number=repeats) for x in range(0, len(graphs))], label="TChanMinPlus3")

plt.plot([timeit.timeit(
    "minPlusAPSP("+str(graphs[x])+")", setup="from MinPlusAPSP import minPlusAPSP", number=repeats) for x in range(minrange, maxrange)], label="MinPlusAPSP")

plt.plot([timeit.timeit(
    "minPlusAPSPFastExp("+str(graphs[x])+")", setup="from MPAPSPFastExp import minPlusAPSPFastExp", number=repeats) for x in range(minrange, maxrange)], label="MinPlusAPSP (Exponent. by squaring)")

plt.plot([timeit.timeit(
    "fastClosureAPSP("+str(graphs[x])+")", setup="from FastClosure import fastClosureAPSP", number=repeats) for x in range(minrange, maxrange)], label="FastClosureAPSP")

plt.plot([timeit.timeit(
    "minPlus("+str(graphs[x])+","+str(graphs[x])+")", setup="from MinPlus import minPlus", number=repeats) for x in range(minrange, maxrange)], label="One MinPlus")

plt.plot([timeit.timeit(
    "fastClosureAPSPT("+str(graphs[x])+")", setup="from TChanAPSP import fastClosureAPSPT", number=repeats) for x in range(minrange, maxrange)], label="TChanAPSP")

plt.plot([timeit.timeit(
    "floydWarshall("+str(graphs[x])+")", setup="from FloydWarshall import floydWarshall", number=repeats) for x in range(minrange, maxrange)], label="FloydWarshall")
'''

plt.legend()
plt.show()
