class RomanNumerals:
    roman = {"M": 1000,"D": 500,"C": 100,"L": 50,"X": 10,"V": 5,"I": 1}

    def findSubtracted(arr, n):
        subtractedNums = []
        if (n > 1):
            for i in range(len(arr)-1):
                if arr[i] < arr[i+1]:
                    subtractedNums.append(i+1)
                    i+=1
        return subtractedNums
    
    def hundreds(v):
        hs = ""
        if v >= 100 and v < 400:
            for i in range(0, v//100, 1):
                hs+="C"
        elif v >= 400 and v < 500:
            hs+="CD"
        elif v >= 500 and v < 600:
            hs+="D"
        elif v >= 600 and v < 900:
            hs+="D"
            for i in range(0, (v-500)//100, 1):
                hs+="C"
        elif v == 900:
            hs+="CM"
        return hs

    def tens(v):
        ts = ""
        if v >= 10 and v < 40:
            for i in range(0, v//10, 1):
                ts+="X"
        elif v == 40:
            ts+="XL"
        elif v == 50:
            ts+="L"
        elif v >= 60 and v < 90:
            ts+="L"
            for i in range(0, (v-50)//10, 1):
                ts+="X"
        elif v == 90:
            ts+="XC"
        return ts

    def ones(v):
        os = ""
        if v >= 1 and v < 4:
            for i in range(0, v, 1):
                os+="I"
        elif v == 4:
            os+="IV"
        elif v == 5:
            os+="V"
        elif v >= 6 and v < 9:
            os+="V"
            for i in range(0, v-5, 1):
                os+="I"
        elif v == 9:
            os+="IX"
        return os
    
    def to_roman(self, n):
        arr_n4 = [0 for i in range(len(str(n)))]

        for i in range(len(arr_n4)):
            arr_n4[i] = int(str(n)[i])*(10**(len(arr_n4)-i-1))

        if len(arr_n4) > 3: # number is at least 1000
            ms = ""
            ths = 0
            for i in range(0, len(arr_n4)-3, 1):
                ths+=arr_n4[i]//1000
            for i in range(ths):
                ms+="M"
            ms+=RomanNumerals.hundreds(arr_n4[len(arr_n4)-3]) + RomanNumerals.tens(arr_n4[len(arr_n4)-2]) + RomanNumerals.ones(arr_n4[len(arr_n4)-1])
            return ms
        elif len(arr_n4) == 3:
            s = ""
            s += RomanNumerals.hundreds(arr_n4[len(arr_n4)-3]) + RomanNumerals.tens(arr_n4[len(arr_n4)-2]) + RomanNumerals.ones(arr_n4[len(arr_n4)-1])
            return s
        elif len(arr_n4) == 2:
            s = ""
            s += RomanNumerals.tens(arr_n4[len(arr_n4)-2]) + RomanNumerals.ones(arr_n4[len(arr_n4)-1])
            return s
        elif len(arr_n4) == 1:
            s = ""
            s += RomanNumerals.ones(arr_n4[len(arr_n4)-1])
            return s
        
    def from_roman(self, n):
        nums = []
        for i in n:
            nums.append(RomanNumerals.roman[i])
        arr = RomanNumerals.findSubtracted(nums, len(nums))
        tot = 0
        for i in range(len(nums)):
            if i in arr:
                tot+=nums[i] - nums[i-1]

        for i in range(len(arr)):
            arr.append(arr[i]-1)

        for i in range(len(nums)):
            if i not in arr:
                tot+=nums[i]
        return tot

#-----------------------------Testing-----------------------------

r = RomanNumerals()

try:
    assert r.to_roman(123) == 'CXXIII'
    print("Passed Test 1")
except AssertionError:
    print("Failed Test 1")

try:
    assert r.to_roman(823) == 'DCCCXXIII'
    print("Passed Test 2")
except AssertionError:
    print("Failed Test 2")

try:
    assert r.to_roman(11283) == 'MMMMMMMMMMMCCLXXXIII'
    print("Passed Test 3")
except AssertionError:
    print("Failed Test 3")

try:
    assert r.to_roman(19) == 'XIX'
    print("Passed Test 4")
except AssertionError:
    print("Failed Test 4")

try:
    assert r.to_roman(49) == 'XLIX'
    print("Passed Test 5")
except AssertionError:
    print("Failed Test 5")

try:
    assert r.from_roman('VII') == 7
    print("Passed Test 6")
except AssertionError:
    print("Failed Test 6")

try:
    assert r.from_roman('CXCII') == 192
    print("Passed Test 7")
except AssertionError:
    print("Failed Test 7")

try:
    assert r.from_roman('MCMXCIX') == 1999
    print("Passed Test 8")
except AssertionError:
    print("Failed Test 8")

try:
    assert r.from_roman('MMMMMIV') == 5004
    print("Passed Test 9")
except AssertionError:
    print("Failed Test 9")

try:
    assert r.from_roman('MDCLXVI') == 1666
    print("Passed Test 10")
except AssertionError:
    print("Failed Test 10")
