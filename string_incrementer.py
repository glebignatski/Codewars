def increment_string(strng):
    new_str = ""
    num = ""
    n = 0
    # Base case: return "1" if an empty string was passed
    if len(strng) == 0:
        return "1"
    check = False # This variable indicates whether all valid numbers have been added
    for i in range(len(strng)-1, -1, -1): # Append from the right side to avoid inapplicable digits
        if (check == False and ord(strng[i]) >= 48 and ord(strng[i]) <= 57):
            num+= str(ord(strng[i])-48)
        else:
            check = True
            new_str+= strng[i]
    # Reverse the character and digit sequences
    new_str = new_str[::-1]
    num = num[::-1]
    if len(num) != 0:
        i = 0
        # Collect the number of zeros and the zero string
        zeros = "" 
        while(i < len(num)):
            if (num[i] == "0"):
                zeros+=num[i]
                i+=1
            else:
                break
        # The case of all digits being zero
        if i == len(num):
            n = int(num)
            n+=1
            return new_str + zeros[0:len(num)-1] + str(n)
        else:
            n_str = num[i:]
            n = int(n_str)
            n+=1
            if (len(zeros) > 0 and num[len(num)-1] == "9"): # The "9" indicates a special case
                if (len(zeros) + len(str(int(num)+1)) > len(num)): # The length of a number changes after increment (e.g., 99 becomes 100)
                    return new_str + zeros[0:len(zeros)-1] + str(n)
                else: # No change in length (e.g., 59 becomes 60)
                    return new_str + zeros + str(n)
            else:
                return new_str + zeros + str(n)
    # The digit component was absent
    return strng + "1"

print(increment_string("hello99"), "\n")
print(increment_string("hello001"), "\n")
print(increment_string("hello1"), "\n")
print(increment_string("hello00"), "\n")
print(increment_string("hello99"), "\n")
print(increment_string("hello099"), "\n")
print(increment_string("hello0099"), "\n")
print(increment_string(""))
