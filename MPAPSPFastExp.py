from MinPlus import minPlus, inf


def minPlusAPSPFastExp(A):
    return expByDoubling(A, len(A))


def expByDoubling(A, n):
    if n == 0:
        return A
    if n == 1:
        return minPlus(A, A)
    if n % 2 == 0:
        return expByDoubling(minPlus(A, A), n/2)
    else:
        return minPlus(A, expByDoubling(minPlus(A, A), (n-1)/2))
