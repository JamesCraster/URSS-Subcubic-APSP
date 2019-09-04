from MinPlus import minPlus, inf


def minPlusAPSP(A):
    """ Doing min-plus multiplication n times will solve APSP, provable by induction """
    result = A
    for i in range(0, len(A)):
        result = minPlus(result, A)
    return result
