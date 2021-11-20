def birthdayCakeCandles(candles):
    max_cand = max(candles)
    count = 0
    for i in range(len(candles)):
        if candles[i] == max_cand:
            count+=1
    print (count)
birthdayCakeCandles([3,2,1,3,3])