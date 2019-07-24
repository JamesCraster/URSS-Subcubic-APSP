# URSS-Subcubic-APSP
A URSS project that aims to implement Ryan Williams' new randomized graph algorithm; paper: https://arxiv.org/pdf/1312.6680.pdf

# Algorithms

* APSP, Floyd Warshall (complete, tested, not yet benchmarked) - takes O(n<sup>3</sup>)
* Orthogonal vectors, trivial algorithm - takes O(n<sup>2</sup>d) 
* Orthogonal vectors, randomized using circuits, Razborov-Smolensky, fast matrix multiplication - takes n<sup>2-1/O(log d)</sup>
* APSP, R.Williams method

# Dependencies

C++11 is needed, run `g++ -std=c++11`

Google Test/Google Benchmark are required - https://github.com/google/benchmark and https://github.com/google/googletest

