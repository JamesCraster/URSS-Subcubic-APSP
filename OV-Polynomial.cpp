#include <vector>
#include <iostream>
#include <cmath>
using namespace std;

void printVector(vector<bool> input)
{
    for (int i = 0; i < input.size(); i++)
    {
        std::cout << input.at(i) << ' ';
    }
    std::cout << std::endl;
}

void print2DVector(vector<vector<bool>> input)
{
    for (int i = 0; i < input.size(); i++)
    {
        printVector(input.at(i));
    }
}
//epsilon used to decide subset size (must be smaller that 1)
//const float epsilon = 0.5;
vector<vector<vector<bool>>> subproblems(std::vector<std::vector<bool>> A)
{
    //this measure of subset size does not make sense? Tends to 1 regardless of d.
    /*double subsetSize = pow(A.size(), epsilon / log2(A[0].size()));*/
    int subsetSize = 1;
    int numberOfSubsets = ceil(A.size() / subsetSize);
    vector<vector<vector<bool>>> subproblemsA;
    for (int i = 0; i < numberOfSubsets; i++)
    {
        vector<vector<bool>> subproblem = {};
        for (int j = 0; j < floor(subsetSize); j++)
        {
            subproblem.push_back(A[i * floor(subsetSize) + j]);
        }
        subproblemsA.push_back(subproblem);
    }
    return subproblemsA;
}
bool polynomialOV(std::vector<std::vector<bool>> A, std::vector<std::vector<bool>> B)
{
    //1. Divide the sets into subproblems.
    vector<vector<vector<bool>>> subproblemsA = subproblems(A);
    vector<vector<vector<bool>>> subproblemsB = subproblems(B);
    //2. Circuit construction.

    return false;
}
int main(int argc, char *argv[])
{
    std::vector<std::vector<bool>> A = {{1, 1, 1}, {1, 1, 0}, {1, 0, 1}, {0, 0, 1}};
    std::vector<std::vector<bool>> B = {{0, 1, 0}, {0, 1, 1}, {1, 0, 1}, {1, 1, 1}};
    std::cout << polynomialOV(A, B) << std::endl;
}