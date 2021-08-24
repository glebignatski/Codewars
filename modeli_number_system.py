def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def isNotCoprime(a, b):
    return gcd(a, b) != 1

def from_nb_2_str(n, modsys):
    # check whether all pairs of numbers in modsys are coprime
    check = True
    ln = len(modsys)
    for i in range(ln-1):
        for j in range(i+1, ln):
            if isNotCoprime(modsys[i], modsys[j]):
                return "Not applicable"
    # check whether the product is less than n
    product = 1
    for i in range(ln):
        product = product * modsys[i]
    if (product < n):
        return "Not applicable"
    xarr = "-"
    for i in range(ln-1):
        xarr = xarr + str(n%modsys[i]) + "--"
    return xarr + str(n%modsys[ln-1]) + "-"

test1 = from_nb_2_str(779, [8,7,5,3])
test2 = from_nb_2_str(15, [8,6,5,3])
test3 = from_nb_2_str(3450, [17,5,3])
test4 = from_nb_2_str(3450, [13,11,7,5,3,2])

if (test1 == "-3--2--4--2-"):
	print("Passed Test 1")
if (test2 == "Not applicable"):
	print("Passed Test 2")
if (test3 == "Not applicable"):
	print("Passed Test 3")
if (test4 == "-5--7--6--0--0--0-"):
	print("Passed Test 4")

# -------------------Other Testing-------------------
# from datetime import datetime

# arr = [i for i in range(1, 10)]
# points = []

# i = 0
# t1 = datetime.now()

# for i in range(len(arr)-1):
#     for j in range(i+1, len(arr)):
# 	    e = "({}, {})".format(arr[i], arr[j])
# 	    if e not in points:
# 	        points.append(e)

# t2 = datetime.now()
# diff = t2-t1
# print(points)
# print("The elapsed time is:", diff)


# points.clear()
# t1 = datetime.now()

# for i in range(len(arr)-1):
#     for j in range(i+1, len(arr)):
# 	    points.append("({}, {})".format(arr[i], arr[j]))
# 	    #points.append(e)

# t2 = datetime.now()
# diff2 = t2-t1
# print(points)
# print("The elapsed time is:", diff2)

# ratio = 0

# try:
# 	ratio = diff/diff2
# except ZeroDivisionError:
# 	print("Error")

# print("Option 2 is {} faster.".format(ratio))
