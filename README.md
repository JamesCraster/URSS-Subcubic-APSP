# URSS-Subcubic-APSP

A URSS project that aims to implement Ryan Williams' new randomized graph algorithm, supervised by Professor Dmitry Chistikov; paper: https://arxiv.org/pdf/1312.6680.pdf

# Algorithms

- APSP, Floyd Warshall (tested, benchmarked) - takes O(n<sup>3</sup>)
- Orthogonal vectors, trivial algorithm (complete) - takes O(n<sup>2</sup>d)
- Orthogonal vectors, randomized using circuits, Razborov-Smolensky, fast matrix multiplication - takes n<sup>2-1/O(log d)</sup>
  (likely won't be necessary.)
- Timothy Chan's 2006 method to solve APSP in O(n^3/log(n)) time (tested, benchmarked)
- APSP, R.Williams method (currently being implemented.)

# Dependencies

Matplotlib is required.
