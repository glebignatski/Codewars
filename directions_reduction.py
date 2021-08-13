def dirReduc(arr):
    for i in range(1, len(arr), 1):
        # vertical direction
        if ((arr[i-1] == "NORTH" and arr[i] == "SOUTH") or (arr[i-1] == "SOUTH" and arr[i] == "NORTH")):
            arr[i-1] = ""
            arr[i] = ""
        # horizontal direction
        if ((arr[i-1] == "EAST" and arr[i] == "WEST") or (arr[i-1] == "WEST" and arr[i] == "EAST")):
            arr[i-1] = ""
            arr[i] = ""
    if "" in arr:
        arr_updated = []
        for i in range(len(arr)):
            if (arr[i] != ""):
                arr_updated.append(arr[i])
        return dirReduc(arr_updated)
    return arr