import random
import copy
from MinPlus import *
import numpy as np
from MinPlusAPSP import *
from MPAPSPFastExp import *
from FloydWarshall import *
from FastClosure import *
from RWilliamsMinPlus import *
import random


def generateGraphOfSize(n):
    graph = []
    for i in range(0, n):
        graph.append([])
        for j in range(0, n):
            if i != j:
                graph[i].append(random.randint(0, 10))
            else:
                graph[i].append(0)
    return graph


# Note the distinction between 0 (edge of no length) and +inf (no edge at all) in these algorithms
graphs = [generateGraphOfSize(x) for x in range(1, 10)]

passes = True
for graph in graphs:
    if(argMinPlus(graph, graph) != enforceUniqueness(copy.deepcopy(graph), copy.deepcopy(graph))):
        print('graph', graph)
        print('minPlus', argMinPlus(graph, graph))
        print('RWilliams', enforceUniqueness(
            copy.deepcopy(graph), copy.deepcopy(graph)))
        passes = False

if passes:
    print("All tests pass")
else:
    print("Test failed")
