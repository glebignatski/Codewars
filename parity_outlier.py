def find_outlier(integers):
    countEven = []
    countOdd = []
    for i in range(len(integers)):
        if (integers[i] % 2) == 0:
            countEven.append(integers[i])
        else:
            countOdd.append(integers[i])
    if len(countEven) == 1:
        return countEven[0]
    else:
        return countOdd[0]