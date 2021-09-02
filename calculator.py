nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]

class Calculator(object):
    def evaluate(self, string):
        s = " " + string + " "
        #s = Calculator.format_e(s)
        #print(s)
        while ("(" in s) or ("/" in s) or ("*" in s) or ("+" in s) or (" - " in s):
            if "(" in s:
                s = Calculator.computeResult(s, "(", -1)
            elif "/" in s:
                ind = s.index("/")
                s = Calculator.computeResult(s, "/", ind)
            elif "*" in s:
                ind = s.index("*")
                s = Calculator.computeResult(s, "*", ind)
            elif "+" in s:
                ind = s.index("+")
                s = Calculator.computeResult(s, "+", ind)
            elif " - " in s:
                ind = s.index(" - ")
                s = Calculator.computeResult(s, "-", ind)
            #print(s)
        #return s
        return float(s.strip())
    
    def format_e(s3):
        delimeters = ["/", "*", "+", "(", ")"]
        s4 = ""

        end = -1
        if (s3[0] != " "):
            s3 = " " + s3 + " "
        end = len(s3) - 1

        for i in range(1, len(s3)-1, 1):
            if s3[i] in delimeters:
                l = ""
                r = ""
                if s3[i-1] != " ":
                    l = " "
                if s3[i+1] != " ":
                    #s4 = s4 + s3[i] + " "
                    r = " "
                s4 = s4 + l + s3[i] + r
            else:
                s4 = s4 + s3[i]

        s4 = s4.replace("  ", " ")
        print(s4)
        return s4

    def findIndexOfLastLeftBracket(s):
        i = 0
        while True:
            try:
                i = s.index("(", i)
                i+=1
            except:
                break
        return i-1
    
    def findIndexOfCorrespondingRightBracket(s, i):
        i = i + 1
        while s[i] != ")":
            i+=1
        return i
    
    def computeResult(s, op, ind):
        if op == "(":
            l = Calculator.findIndexOfLastLeftBracket(s)
            r = Calculator.findIndexOfCorrespondingRightBracket(s, l)

            return Calculator.calculateResultInBracket(s, l, r)
        
        lind = ind-2
        loperand = ""
        while (s[lind] in nums): #or s[lind] == "-"):
            loperand += s[lind]
            lind-=1
        loperand = loperand[::-1]

        rind = ind+2
        roperand = ""
        while (s[rind] in nums): # or s[rind] == "-"):
            roperand += s[rind]
            rind+=1

        if op == "/":
            res = float(loperand) / float(roperand)
        elif op == "*":
            res = float(loperand) * float(roperand)
        elif op == "+":
            res = float(loperand) + float(roperand)
        elif op == "-":
            res = float(loperand) - float(roperand)
    
        s_before = s[:lind+1]
        rem_s = s[rind:]
        old_len = len(s)
        s = ""
        if lind == 0:
            s = s_before + " " + str(res) + rem_s    
        else:
            s = s_before + str(res) + rem_s
        return s
    
    def calculateResultInBracket(s, l, r): # e.g., ( 3 + 2 )
        e = s[l:r+1]
        before = s[:l]
        rem = s[r+1:]
        if "/" in e:
            ops = e.split("/")
        
            ops[0] = ops[0].replace("(", "")
            ops[0] = ops[0].strip()

            ops[1] = ops[1].replace(")", "")
            ops[1] = ops[1].strip()

            return before + str(float(ops[0]) / float(ops[1])) + rem
        elif "*" in e:
            ops = e.split("*")

            ops[0] = ops[0].replace("(", "")
            ops[0] = ops[0].strip()

            ops[1] = ops[1].replace(")", "")
            ops[1] = ops[1].strip()

            return before + str(float(ops[0]) * float(ops[1])) + rem
        elif "+" in e:
            ops = e.split("+")

            ops[0] = ops[0].replace("(", "")
            ops[0] = ops[0].strip()

            ops[1] = ops[1].replace(")", "")
            ops[1] = ops[1].strip()

            return before + str(float(ops[0]) + float(ops[1])) + rem
        elif "-" in e:
            ops = e.split(" - ")

            ops[0] = ops[0].replace("(", "")
            ops[0] = ops[0].strip()

            ops[1] = ops[1].replace(")", "")
            ops[1] = ops[1].strip()

            return before + str(float(ops[0]) - float(ops[1])) + rem

        else: # e.g., ( 4 ) ==> 4
            e = e.replace("(", "")
            e = e.replace(")", "")
            e = e.strip()
            return before + e + rem



# -----------------------------------Testing-----------------------------------
c = Calculator()
#print(c.evaluate("( 2.5 * ( -2.1 * ( 2 * ( 2 * 1 ) ) ) )"))

try:
    assert c.evaluate("( 3 )") == 3.0
    print("Test 1 Passed")
except AssertionError:
    print("Test 1 Failed")

try:
    assert c.evaluate("10 * 2 + ( 3 + 3 )") == 26
    print("Test 2 Passed")
except AssertionError:
    print("Test 2 Failed")

try:
    assert c.evaluate("( 0 + 3 )") == 3.0
    print("Test 3 Passed")
except AssertionError:
    print("Test 3 Failed")

try:
    assert c.evaluate("14 + 3") == 17
    print("Test 4 Passed")
except AssertionError:
    print("Test 4 Failed")

try:
    assert c.evaluate("( ( ( ( 5 - 5 ) ) ) )") == 0
    print("Test 5 Passed")
except AssertionError:
    print("Test 5 Failed")

try:
    assert c.evaluate("( 6 - 2 ) + 5 / 2") == 6.5
    print("Test 6 Passed")
except AssertionError:
    print("Test 6 Failed")

try:
    assert c.evaluate("( 2.5 * ( -2.1 * ( 2 * ( 2 * 1 ) ) ) )") == -21.0
    print("Test 7 Passed")
except AssertionError:
    print("Test 7 Failed")

try:
    assert c.evaluate("( -2 * -2 )") == 4.0
    print("Test 8 Passed")
except AssertionError:
    print("Test 8 Failed")

def format_e(s3):
    delimeters = ["/", "*", "+", "(", ")"]
    s4 = ""
    end = -1
    if (s3[0] != " "):
        s3 = " " + s3 + " "
    end = len(s3) - 1
    for i in range(1, end, 1):
        if s3[i] in delimeters:
            l = ""
            r = ""
            if s3[i-1] != " ":
                #s4 = s4 + " " + s3[i]
                l = " "
            if s3[i+1] != " ":
                #s4 = s4 + s3[i] + " "
                r = " "
            s4 = s4 + l + s3[i] + r
        else:
            s4 = s4 + s3[i]
    s4 = s4.replace("  ", " ")
    #print(s4)
    return s4

s5 = format_e("10 * 2")
s6 = format_e("10 * 2 + ( 3 + 3 )")
# print("s6", s6)
# print(c.evaluate(s6))

# print(format_e("( 6 / 2 ) - ( 5 / 2 )"))
# print(c.evaluate("( 6 / 2 ) + ( 5 / 2 )"))

#print(float(" 5.0"))