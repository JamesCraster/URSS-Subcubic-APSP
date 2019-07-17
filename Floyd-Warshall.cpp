#include <vector>
#include <iostream>
#include "catch.hpp"
using namespace std;
//Adjacency matrix
int inf = 1000000;
vector<vector<int>> graph = {{0, 2, inf, inf, 7}, {2, 0, 8, 4, inf}, {inf, 8, 0, 2, inf}, {inf, 4, 2, 0, inf}, {7, inf, inf, inf, 0}};

void printVector(vector<int> input)
{
    for (int i = 0; i < input.size(); i++)
    {
        std::cout << input.at(i) << ' ';
    }
}

void print2DVector(vector<vector<int>> input)
{
    for (int i = 0; i < input.size(); i++)
    {
        printVector(input.at(i));
        std::cout << std::endl;
    }
}

//Implementation: This algo is O(V^3)
pair<vector<vector<int>>, vector<vector<int>>> floydWarshall(vector<vector<int>> graph)
{

    //build used in path reconstruction
    vector<vector<int>> next;
    next.resize(graph.size(), vector<int>());
    for (int i = 0; i < next.size(); i++)
    {
        next[i].resize(graph.size(), -1);
        next[i][i] = i;
    }
    for (int i = 0; i < graph.size(); i++)
    {
        for (int j = 0; j < graph.size(); j++)
        {
            if (graph[i][j] != inf)
            {
                next[i][j] = j;
            }
        }
    }

    auto dist = graph;
    for (int k = 0; k < graph.size(); k++)
    {
        for (int i = 0; i < graph.size(); i++)
        {
            for (int j = 0; j < graph.size(); j++)
            {
                if (dist[i][j] > dist[i][k] + dist[k][j])
                {
                    dist[i][j] = dist[i][k] + dist[k][j];
                    next[i][j] = next[i][k];
                }
            }
        }
    }
    return make_pair(dist, next);
}

//Path reconstruction (Using shortest path tree)
vector<int> reconstructPath(int u, int v, vector<vector<int>> next)
{
    if (next[u][v] == -1)
    {
        return vector<int>();
    }
    vector<int> path = {u};
    while (u != v)
    {
        u = next[u][v];
        path.push_back(u);
    }
    return path;
}
//Automated testing

//Automated benchmarking

int main(int argc, char *argv[])
{
    //Random graph generation
    auto solution = floydWarshall(graph);
    print2DVector(solution.first);
    printVector(reconstructPath(0, 3, solution.second));
}