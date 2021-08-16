import sys
letters = ["A", "B", "C", "D", "E", "F"]

def rgb(r, g, b):   
    return getValue(r) + getValue(g) + getValue(b)

def getValue(v):
    if (v <= 0):
        fv = "00"
    elif (v >= 255):
        fv = "FF"
    else:
        vu = v // 16
        vl = v % 16
        
        if vu > 9:
            vu = str(letters[vu-10])
        else:
            vu = str(vu)
        if vl > 9:
            vl = str(letters[vl-10])
        else:
            vl = str(vl)
            
        fv = vu + vl
    return fv

print(rgb(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))