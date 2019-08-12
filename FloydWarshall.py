inf = 1000000

# Implementation: This algo is O(V^3)


def floydWarshall(graph):
    # build shortest-path-trees used in path reconstruction
    next = []
    for i in range(0, len(graph)):
        next.append([])

    for i in range(0, len(next)):
        for j in range(0, len(graph)):
            next[i].append(-1)
        next[i][i] = i

    for i in range(0, len(graph)):
        for j in range(0, len(graph)):
            if (graph[i][j] != inf):
                next[i][j] = j

    dist = graph
    for k in range(0, len(graph)):
        for i in range(0, len(graph)):
            for j in range(0, len(graph)):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next[i][j] = next[i][k]
    return (dist, next)

# Path reconstruction(Using shortest path tree)


def reconstructPath(u, v, next):
    if (next[u][v] == -1):
        return []
    path = [u]
    while (u != v):
        u = next[u][v]
        path.append(u)
    return path
