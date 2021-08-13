def duplicate_encode(word):
    lis = list(word.upper())
    count = [1 for i in range(len(word))]
    for i in range(len(word)):
        letter = lis[i]
        for j in range(len(word)):
            if (lis[j] == letter and j != i):
                count[i]+=1
    output = ""
    for i in count:
        if i > 1:
            output+=")"
        else:
            output+="("
    return output