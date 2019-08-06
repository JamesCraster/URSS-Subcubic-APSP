#include <vector>
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
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
vector<vector<int>> minPlus(vector<vector<int>> A, vector<vector<int>> B)
{
    vector<vector<int>> C = {};
    for (int i = 0; i < A.size(); i++)
    {
        C.push_back({});
        for (int j = 0; j < A[i].size(); j++)
        {
            int minVal = 10000000;
            for (int k = 0; k < A.size(); k++)
            {
                minVal = min(A[i][k] + B[k][j], minVal);
            }
            C[i].push_back(minVal);
        }
    }
    return C;
}

int main(int argc, char *argv[])
{
    //Note the distinction between 0 (edge of no length) and +inf (no edge at all)
    vector<vector<int>> A = {{0, 1, 4, inf}, {1, 0, 2, 1}, {4, 2, 0, inf}, {inf, 1, inf, 0}};
    //O(n^4) algorithm for APSP comes from naively applying minPlus n times.
    vector<vector<int>> B = {{0, inf},
                             {inf, 0}};
    vector<vector<int>> C = {{1, 2}, {3, 4}};
    print2DVector(minPlus(B, C));
    //print2DVector(minPlus(minPlus(A, A), A));
    return 0;
}