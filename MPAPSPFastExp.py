from MinPlus import minPlus, inf


def minPlusAPSPFastExp(A):
    return expBySquaring(A, len(A))


def expBySquaring(A, n):
    if n == 0:
        return A
    if n == 1:
        return minPlus(A, A)
    if n % 2 == 0:
        return expBySquaring(minPlus(A, A), n/2)
    else:
        return minPlus(A, expBySquaring(minPlus(A, A), (n-1)/2))
