import math


def enforceUniqueness(A, B):
    n = len(A)
    d = len(A[0])
    # Enforce a unique minimum
    # Both multiplication by addition and the trivial multiplication method
    # take O(n^2) for two n-digit numbers. Therefore trivial multiplication used.
    for i in range(0, n):
        for j in range(0, d):
            A[i][j] = A[i][j] * (n+1) + j
    for i in range(0, len(B)):
        for j in range(0, len(B[i])):
            B[i][j] = B[i][j] * (len(A)+1)

    print(A)
    print(B)
    # Fredman's trick:
    Af = []
    for i in range(0, n):
        Af.append([])
        for k in range(0, d):
            Af[i].append([])
            for otherK in range(0, d):
                Af[i][k].append(A[i][k]-A[i][otherK])

    Bf = []
    for k in range(0, d):
        Bf.append([])
        for otherK in range(0, d):
            Bf[k].append([])
            for j in range(0, n):
                Bf[k][otherK].append(B[otherK][j]-B[k][j])

    print(Af)
    print(Bf)
    # Finish replacement on Af and Bf:
    S = []
    for k in range(0, len(A[0])):
        S.append([])
        for otherK in range(0, len(A[0])):
            new = sorted([(Af[i][k][otherK], i, 'A')
                          for i in range(0, n)] + [(Bf[k][otherK][i], i, 'B') for i in range(0, n)])
            print('new: ', new)
            for rank, (value, i, parentList) in enumerate(new):
                if parentList == 'A':
                    Af[i][k][otherK] = rank
                else:
                    Bf[k][otherK][i] = rank

    print(Af)
    print(Bf)
    kMatrix = []
    for i in range(0, n):
        kMatrix.append([])
        for j in range(0, n):
            kMatrix[i].append(trivialCircuitSolve(Af, Bf, d, i, j))

    out = []
    for i in range(0, len(kMatrix)):
        out.append([])
        for j in range(0, len(kMatrix[i])):
            k = kMatrix[i][j]
            out[i].append((A[i][k] + B[k][j])//(n+1))
    return out


def trivialCircuitSolve(Af, Bf, d, i, j):
    value = ""
    for l in range(0, int(math.log(d))+1):
        out = False
        for k in range(0, d):
            andResult = False
            # remove '0b'
            binK = bin(k)[2:]
            # any index out of range should point to 0.
            if not(l + 1 > len(binK)) and binK[-(l+1)] == '1':
                andResult = True
                for otherK in range(0, d):
                    comparison = Af[i][k][otherK] <= Bf[k][otherK][j]
                    andResult = andResult and comparison
                print(andResult)
            out = out or andResult
        if(out):
            value = "1" + value
        else:
            value = "0" + value
    return int(value, 2)

# Checking:
# - check that creating distance between points is done correctly DONE
# - check that Af and Bf are correct at stage 1 DONE
# - check that Af and Bf are correct at stage 2
# - check trivialCircuitSolve is correct


'''def addByDoubling(A, n):
    if n == 0:
        return A
    if n == 1:
        return A + A
    if n % 2 == 0:
        return addByDoubling(A + A, n/2)
    else:
        return A + addByDoubling(A + A, (n-1)/2)
'''
