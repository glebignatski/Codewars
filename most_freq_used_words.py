letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
letters = letters.split(" ")

class top_3_words(object):
    def top_3_words(self, text):

        # Base case
        if len(text) == 0:
            return []
    
        converted_text = ""
        for i in text:
            if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
                converted_text += i.lower()
            elif (ord(i) == 33 or (ord(i) >= 35 and ord(i) <= 38) or (ord(i) >= 40 and ord(i) <= 64)):
                continue
            else: # implies apostrophe (' or ")
                converted_text += i
    
        # return an empty array if the text does not contain any alpha characters
        check = 0
        for i in converted_text:
            if i in letters:
                check = 1
                break
        if check == 0:
            return []
    
        # alternative approach
        # if all([not i.isalpha() for i in converted_text]):
        #     return []
    
    
        # remove extra white space (e.g., "a   a b b   a" ==> "a a b b a")
        while True:
            if "  " in converted_text:
                converted_text = converted_text.replace("  ", " ")
            else:
                break
    
        converted_text = converted_text.rstrip()
        converted_text = converted_text.lstrip()
        ref_words = text.split(" ")
        words = converted_text.split(" ")
    
        if len(words) == 1:
            return words
    
        count = {}
    
        for i in words:
            count[i] = 0
    
        # return the list of one word if the entire list exclusively had multiple exact words
        if len(count.keys()) == 1:
            return words[:1]
    
        # count the frequency of each valid word
        for i in words:
            count[i] += 1
    
        # add the frequencies to a list that would sorted in ascending order
        freq = []
        for i in count:
            freq.append(count[i])
    
        # clear words' list, and add the unique words from the count dictionary
        words.clear()
        for i in count.keys():
            words.append(i)
    
        # Bubble Sort both the words and frequency lists
        for i in range(len(freq)-1):
            for j in range(len(freq) - 1 - i):
                if freq[j] < freq[j+1]:
                    temp = freq[j]
                    temp_word = words[j]
                    freq[j] = freq[j+1]
                    words[j] = words[j+1]
                    freq[j+1] = temp
                    words[j+1] = temp_word
        
        # special case when the number of unique words is under 3
        if len(words) < 3:
            return words[:len(words)]
    
        # return top 3 words
        return words[:3]


# ------------------------------------Testing------------------------------------


t = "ee EE Ee eE ignatski's aa  Ignatski's  aa Ignatski's Ignatski's aa b Ignatski's b c dd: erg, 1 22 &&"
t2 = "aa aa aa aa"
t3 = "won't won't wont"
t4 = ";''"
t5 = "a b a"

# Test cases taken from: https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python
t6 = "a a a  b  c c  d d d d  e e e e e"
t7 = """In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""

t8 = "#@!"
# print(top_3_words(t))
# print(top_3_words(t2))
# print(top_3_words(t3))
# print(top_3_words(t4))
# print(top_3_words(t5))

test = top_3_words()

try:
    assert test.top_3_words(t) == ["ignatski's", "ee", "aa"]
    print("Test 1 Passed")
except AssertionError:
    print("Test 1 Failed")

try:
    assert test.top_3_words(t2) == ["aa"]
    print("Test 2 Passed")
except AssertionError:
    print("Test 2 Failed")

try:
    assert test.top_3_words(t3) == ["won't", "wont"]
    print("Test 3 Passed")
except AssertionError:
    print("Test 3 Failed")

try:
    assert test.top_3_words(t4) == []
    print("Test 4 Passed")
except AssertionError:
    print("Test 4 Failed")

try:
    assert test.top_3_words(t5) == ["a", "b"]
    print("Test 5 Passed")
except AssertionError:
    print("Test 5 Failed")

try:
    assert test.top_3_words(t6) == ["e", "d", "a"]
    print("Test 6 Passed")
except AssertionError:
    print("Test 6 Failed")

try:
    assert test.top_3_words(t7) == ["a", "of", "on"]
    print("Test 7 Passed")
except AssertionError:
    print("Test 7 Failed")

try:
    assert test.top_3_words(t8) == []
    print("Test 8 Passed")
except AssertionError:
    print("Test 8 Failed")