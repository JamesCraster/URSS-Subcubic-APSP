from MinPlus import minPlus, inf


def minPlusAPSP(A):
    result = A
    for i in range(0, len(A)):
        result = minPlus(result, A)
    return result
