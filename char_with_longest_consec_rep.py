def longest_repetition(chars):
    if len(chars) == 0:
        return '', 0
    s = ""
    # Add a space delimeter to the parts of the string where consecutive characters no longer repeat
    # e.g., "aaabb" becomes "aaa bb", which I could then split to see which consecutive sequence is the largest
    for i in range(len(chars)-1):
        if (chars[i] == chars[i+1]):
            s+=chars[i]
        else:
            s+=chars[i] + " "
            
    # Handle the last character of the input string
    if (chars[len(chars)-2] != chars[len(chars)-1]):
        s+=" " + chars[len(chars)-1]
    else:
        s+= chars[len(chars)-1]
    
    # Split the array of consecutive characters
    seq_arr = s.split(" ")
    if len(seq_arr) == 0:
        return chars[0], len(seq_arr)
    
    max_i = seq_arr[0][0]
    count = len(seq_arr[0])
    # Retrieve the largest consecutive character sequence

    for i in range(1, len(seq_arr)):
        if (len(seq_arr[i]) > count):
            count = len(seq_arr[i])
            max_i = seq_arr[i][0]
    # Return the result
    return max_i, count


assert longest_repetition("aaaabb") ==  ('a', 4)
assert longest_repetition("bbbaaabaaaa") == ('a', 4)
assert longest_repetition("cbdeuuu900") == ('u', 3)
assert longest_repetition("abbbbb") == ('b', 5)
assert longest_repetition("aabb") == ('a', 2)
assert longest_repetition("ba") == ('b', 1)
assert longest_repetition("") == ('', 0)
print("Passed all tests")
