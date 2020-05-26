def birthdayCakeCandles(ar):
    c = 0
    x = max(ar)
    for i in range(0, len(ar)):
        if ar[i] == x:
            c +=1
    return(c)
