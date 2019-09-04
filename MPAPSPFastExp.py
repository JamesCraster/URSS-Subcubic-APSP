from MinPlus import minPlus, inf


def minPlusAPSPFastExp(A):
    """ can reduce number of minPlus products to log(n) many using exponentiation by squaring """
    return expBySquaring(A, len(A))


def expBySquaring(A, n):
    # Note this is exponentiation by squaring in tropical algebra
    if n == 0:
        return A
    if n == 1:
        return minPlus(A, A)
    if n % 2 == 0:
        return expBySquaring(minPlus(A, A), n/2)
    else:
        return minPlus(A, expBySquaring(minPlus(A, A), (n-1)/2))
