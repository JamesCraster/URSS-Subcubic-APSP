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

//Implementation
vector<vector<int>> floydWarshall(vector<vector<int>> graph)
{
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
                }
            }
        }
    }
    return dist;
}

int main(int argc, char *argv[])
{
    auto solution = floydWarshall(graph);
    print2DVector(solution);
}