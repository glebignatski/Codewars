def find_summands(n):
    if n == 1:
        return [1]
    cube = n ** 3
    components = [0 for i in range(n)]
    components[0] = 1
    for i in range(1, n, 1):
        components[i] = components[i-1] + 2
    #print(components)
    tot = 0
    while cube != tot:
        for i in range(n):
            tot = tot + components[i]
        #print(tot)
        if tot == cube:
            return components
        else:
            for i in range(n):
                components[i]+=2
            tot = 0
    return [1]

print(find_summands(50))