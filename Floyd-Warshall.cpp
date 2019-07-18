#include <vector>
#include <iostream>
#include <gtest/gtest.h>
using namespace std;
//Adjacency matrix
int inf = 1000000;

void printVector(vector<int> input)
{
    for (int i = 0; i < input.size(); i++)
    {
        std::cout << input.at(i) << ' ';
    }
    std::cout << std::endl;
}

void print2DVector(vector<vector<int>> input)
{
    for (int i = 0; i < input.size(); i++)
    {
        printVector(input.at(i));
    }
}

//Implementation: This algo is O(V^3)
pair<vector<vector<int>>, vector<vector<int>>> floydWarshall(vector<vector<int>> graph)
{
    //build shortest-path-trees used in path reconstruction
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
TEST(Distances, Example)
{
    vector<vector<int>> graph = {{0, 2, inf, inf, 7}, {2, 0, 8, 4, inf}, {inf, 8, 0, 2, inf}, {inf, 4, 2, 0, inf}, {7, inf, inf, inf, 0}};
    EXPECT_EQ(floydWarshall(graph).first[0][3], 6);
    EXPECT_EQ(floydWarshall(graph).first[0][4], 7);
    EXPECT_EQ(floydWarshall(graph).first[0][2], 8);
    EXPECT_EQ(floydWarshall(graph).first[2][1], 6);
}
TEST(PathReconstruction, Example)
{
    vector<vector<int>> graph = {{0, 2, inf, inf, 7}, {2, 0, 8, 4, inf}, {inf, 8, 0, 2, inf}, {inf, 4, 2, 0, inf}, {7, inf, inf, inf, 0}};
    vector<int> result = {0, 1, 3, 2};
    EXPECT_TRUE(reconstructPath(0, 2, floydWarshall(graph).second) == result);
    vector<int> result2 = {0, 1, 3};
    EXPECT_TRUE(reconstructPath(0, 3, floydWarshall(graph).second) == result2);
}
//Automated benchmarking

int main(int argc, char *argv[])
{
    vector<vector<int>> graph = {{0, 2, inf, inf, 7}, {2, 0, 8, 4, inf}, {inf, 8, 0, 2, inf}, {inf, 4, 2, 0, inf}, {7, inf, inf, inf, 0}};
    auto solution = floydWarshall(graph);
    print2DVector(solution.first);
    printVector(reconstructPath(0, 3, solution.second));
    ::testing::InitGoogleTest(&argc, argv);
    std::cout << RUN_ALL_TESTS() << std::endl;
}