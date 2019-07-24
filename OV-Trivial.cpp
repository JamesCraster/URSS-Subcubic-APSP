#include <vector>
#include <iostream>
using namespace std;

void printVector(vector<bool> input)
{
    for (int i = 0; i < input.size(); i++)
    {
        std::cout << input.at(i) << ' ';
    }
    std::cout << std::endl;
}

//Implementation of OV: Note all boolean vectors should be of the same length.
bool trivialOV(std::vector<std::vector<bool>> A, std::vector<std::vector<bool>> B)
{
    for (int i = 0; i < A.size(); i++)
    {
        for (int j = 0; j < B.size(); j++)
        {
            bool orthogonal = true;
            for (int k = 0; k < A[i].size(); k++)
            {
                if (A[i][k] == 1 && B[j][k] == 1)
                {
                    orthogonal = false;
                }
            }
            if (orthogonal)
            {
                printVector(A[i]);
                printVector(B[j]);
                return true;
            }
        }
    }
    return false;
}
int main(int argc, char *argv[])
{
    std::vector<std::vector<bool>> A = {{1, 1, 1}, {1, 1, 0}, {1, 0, 1}, {0, 0, 1}};
    std::vector<std::vector<bool>> B = {{0, 1, 0}, {0, 1, 1}, {1, 0, 1}, {1, 1, 1}};
    std::cout << trivialOV(A, B) << std::endl;
}