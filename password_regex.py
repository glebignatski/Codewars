import re

p = re.compile('\w*')
p2 = re.compile('\w?')
p3 = re.compile("home-?brew")
m = p.match("")
m2 = p2.match("")
m3 = p3.match("hombrew")

print(str(m) == str(m2))
print(m2)
print(m3)

# if m != None:
#     print(m.group())
#     print(m.start(), m.end())
#     print(m.span())
# else:
# 	print("Not matched!")

# print(re.search('[0-9][0-9][0-9]', 'foo456bar'))