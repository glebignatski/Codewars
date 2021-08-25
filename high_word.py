def high(x):
    if len(x) == 0:
        return ""
    words = x.split(" ")
    tot = [0 for i in range(len(words))]
    for i in range(len(words)):
        for ch in range(len(words[i])):
            tot[i] = tot[i] + (ord(words[i][ch])-96)
    max_word = words[0]
    t = tot[0]
    
    for i in range(1, len(tot)):
        if tot[i] > t: # To preserve order (if the inequality was '>=', then the latest element would count)
            max_word = words[i]
            t = tot[i]
    return max_word

# ------------------------Testing------------------------
try:
    assert high('man i need a taxi up to ubud') == 'taxi'
    print("Passed Test 1")
except AssertionError:
    print("Failed Test 1")

try:
    assert high('take me to semynak') == 'semynak'
    print("Passed Test 2")
except AssertionError:
    print("Failed Test 2")

try:
    assert high('aa b') == 'aa'
    print("Passed Test 3")
except AssertionError:
    print("Failed Test 3")

try:
    assert high('b aa') == 'b'
    print("Passed Test 4")
except AssertionError:
    print("Failed Test 4")

try:
    assert high('bb d') == 'bb'
    print("Passed Test 5")
except AssertionError:
    print("Failed Test 5")

try:
    assert high('d bb') == 'd'
    print("Passed Test 6")
except AssertionError:
    print("Failed Test 6")

try:
    assert high("aaa b") == "aaa"
    print("Passed Test 7")
except AssertionError:
    print("Failed Test 7")