import random
from MinPlusAPSP import *
from FloydWarshall import *
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
graphs = [generateGraphOfSize(x) for x in range(1, 20)]

passes = True
for graph in graphs:
    if(minPlusAPSP(graph) != floydWarshall(graph)[0]):
        print(graph)
        print(minPlusAPSP(graph))
        print(floydWarshall(graph)[0])
        passes = False

if passes:
    print("All tests pass")
else:
    print("Test failed")
