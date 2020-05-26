def plusMinus(arr):
    p = 0
    n = 0
    z = 0
    for i in range(0, len(arr)):
        if arr[i] > 0:
            p += 1
        elif arr[i] < 0:
            n += 1
        else:
            z += 1
    print((1/len(arr)*p))
    print((1/len(arr)*n))
    print((1/len(arr)*z))