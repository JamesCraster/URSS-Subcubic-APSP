
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
    # Potential bug area:
    # Finish replacement on Af and Bf:
    S = []
    for k in range(0, len(A[0])):
        S.append([])
        for otherK in range(0, len(A[0])):
            new = sorted([(Af[i][k][otherK], 'A', i)
                          for i in range(0, n)] + [(Bf[k][otherK][i], 'B', i) for i in range(0, n)])
            print(new, k, otherK)
            for rank, (value, parentList, index) in enumerate(new):
                if parentList == 'A':
                    Af[index][k][otherK] = rank
                else:
                    Bf[k][otherK][index] = rank

    print(Af)
    print(Bf)
    # Everything above this line runs (both theoretically and in practice) in O(n·d^2·logn)
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
            out[i].append((A[i][k] + B[k][j] - k)//(n+1))
    return kMatrix


def trivialCircuitSolve(Af, Bf, d, i, j):
    value = ""
    bitCount = int(math.log(d)) + 1
    print('########################', d, i, j)
    for l in range(0, bitCount):
        out = False
        for k in range(0, d):
            andResult = False
            # remove '0b'
            binK = bin(k)[2:].zfill(bitCount)
            print(binK)
            # any index out of range should point to 0.
            if binK[-(l+1)] == '1':
                print('tried')
                andResult = True
                for otherK in range(0, d):
                    print(i, k, otherK, j, len(Af), Af, Bf)
                    comparison = Af[i][k][otherK] <= Bf[k][otherK][j]
                    print('comparison', i, k, otherK, j,
                          Af[i][k][otherK], Bf[k][otherK][j])
                    andResult = andResult and comparison
            out = out ^ andResult
        if(out):
            value = "1" + value
        else:
            value = "0" + value
    print('value', value)
    return int(value, 2)
