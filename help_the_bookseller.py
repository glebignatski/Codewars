def stock_list(listOfArt, listOfCat):
    if (len(listOfArt) == 0 or len(listOfCat) == 0):
        return ""
    
    # Retrive type of 'listOfArt'
    t = str(type(listOfArt))
    st = t.split(" ")
    tp = st[1][:-1]
    
    # Convert the passed set into a list
    if (tp == "\'set\'"):
        listOfArt = lis(listOfArt)
        listOfCat = lis(listOfCat)

    s = ""

    # Add the necessary book types from 'listOfArt'
    distrib = {}
    for i in listOfCat:
        distrib[i] = 0
    
    for e in listOfArt:
        arr_e = e.split(" ")
        
        # Retrieve the amount of available books
        n = int(arr_e[1])
        
        # Scan through the entire stock and
        # Attempt to increment on all book types
        # The irrelevant ones are skipped
        try:
            distrib[e[0]] = distrib[e[0]] + n
        except:
            continue
            
    for i in distrib:
        s += "(" + i + " : " + str(distrib[i]) + ")" + " - "
        
    return s[:-3] # Cut off the final three characters ' - ' and return the special string
                




stocklist = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
categories = ["A", "B"]

stocklist2 = ["Hl2w 200", "H8uy 120", "H1qq 530", "C77p 500", "Rvbz 250", "D55a 77", "Dqzm 45"]
categories2 = ["H", "C", "R"]

stocklist3 = ["Hl2w 200", "H8uy 120", "H1qq 530", "C77p 500", "Rvbz 250", "D55a 77", "Dqzm 45"]
categories3 = ["C", "R", "D"]

# ------------------------Testing------------------------
try:
    assert stock_list(stocklist, categories) == "(A : 200) - (B : 1140)"
    print("Passed Test 1")
except AssertionError:
    print("Failed Test 1")

try:
    assert stock_list(stocklist2, categories2) == "(H : 850) - (C : 500) - (R : 250)"
    print("Passed Test 2")
except AssertionError:
    print("Failed Test 2")

try:
    assert stock_list(stocklist3, categories3) == "(C : 500) - (R : 250) - (D : 122)"
    print("Passed Test 3")
except AssertionError:
    print("Failed Test 3")