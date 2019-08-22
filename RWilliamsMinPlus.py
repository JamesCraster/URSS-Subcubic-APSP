def enforceUniqueness(A, B):
    # Enforce a unique minimum
    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            A[i][j] = addByDoubling(A[i][j], len(A)+1) + j
    for i in range(0, len(B)):
        for j in range(0, len(B[i])):
            B[i][j] = addByDoubling(B[i][j], len(A)+1)
    # Fredman's trick:
    Af = []
    for i in range(0, len(A)):
        Af.append([])
        for k in range(0, len(A[i])):
            Af[i].append([])
            for otherK in range(0, len(A[i])):
                Af[i][k].append(A[i][k]-A[i][otherK])

    Bf = []
    for k in range(0, len(B)):
        Bf.append([])
        for otherK in range(0, len(B)):
            Bf[k].append([])
            for j in range(0, len(B[0])):
                Bf[k][otherK].append(B[otherK][j]-B[k][j])

    # Finish replacement:
    return (A, B)


def addByDoubling(A, n):
    if n == 0:
        return A
    if n == 1:
        return A + A
    if n % 2 == 0:
        return addByDoubling(A + A, n/2)
    else:
        return A + addByDoubling(A + A, (n-1)/2)
