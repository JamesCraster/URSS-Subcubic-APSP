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
    if(argMinPlus(graph, graph) != enforceUniqueness(graph, graph)):
        print('graph', graph)
        print('minPlus', argMinPlus(graph, graph))
        print('RWilliams', enforceUniqueness(
            copy.deepcopy(graph), copy.deepcopy(graph)))
        passes = False
'''for graph in graphs:
    if(minPlusAPSP(graph) != floydWarshall(graph)[0] or minPlusAPSPFastExp(graph) != minPlusAPSP(graph) or fastClosureAPSP(graph) != minPlusAPSP(graph) or fastClosureAPSPT(graph) != fastClosureAPSP(graph)):
        print(graph)
        print(minPlusAPSP(graph))
        print(fastClosureAPSP(graph))
        print('minPlus problem')
        passes = False
    print('graph: ', graph)
    if(len(graph) > 1):
        if(minPlus(graph, graph) != TChanMinPlus(graph, graph)):
            print(minPlus(graph, graph))
            print(TChanMinPlus(graph, graph))
            print('TChan problems')
            passes = False
            break'''

'''for graph in graphs:
    if(not np.array_equal(minPlus(graph, graph), (oldMinPlus(graph, graph)))):
        passes = False'''

if passes:
    print("All tests pass")
else:
    print("Test failed")
