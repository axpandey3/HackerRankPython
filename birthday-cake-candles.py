def birthdayCakeCandles(ar):
    c = 0
    for i in range(0, len(ar)):
        if ar[i] == max(ar):
            c +=1
    return(c)