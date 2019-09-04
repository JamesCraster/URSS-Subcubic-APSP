# URSS-Subcubic-APSP

A URSS project into Ryan Williams' new randomized graph algorithm, supervised by Professor Dmitry Chistikov; paper: https://arxiv.org/pdf/1312.6680.pdf


# Algorithms

- APSP, Floyd Warshall (tested, benchmarked) - takes O(n<sup>3</sup>)
- Orthogonal vectors, trivial algorithm (complete) - takes O(n<sup>2</sup>d)
- Orthogonal vectors, randomized using circuits, Razborov-Smolensky, fast matrix multiplication - takes n<sup>2-1/O(log d)</sup>
- APSP by repeated application of min plus multiplication (O(n^4) by a naive number of applications, O(n^3 log n) using exponentiation by squaring)
- Timothy Chan's 2006 method to solve APSP in O(n^3/log(n)) time (tested, benchmarked)
- Naive matrix multiplication (O(n^3)) and Strassen's method (O(n^~2.8))
- APSP, R.Williams method (currently being implemented.)

# Resources

Useful lecture series: (in particular, lectures 4 and 5):
https://www.mpi-inf.mpg.de/departments/algorithms-complexity/teaching/summer16/poly-complexity/

Useful conference:
https://simons.berkeley.edu/workshops/schedule/1821

https://simons.berkeley.edu/talks/fabrizo-grandoni-2015-12-02 (discussion of subcubic equivalence)

Paper on T.M Chan's algorithm:
http://www.eecs.tufts.edu/~aloupis/comp260/lectures/chan-2008.pdf

Useful discussion of the polynomial method: https://people.csail.mit.edu/rrw/fsttcs-survey.pdf

# Dependencies

Matplotlib and numpy are required. Written using Python 3.6.8
