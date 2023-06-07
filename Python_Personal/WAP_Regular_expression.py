import re

str1 = ''
phrase = "dwfcv3242!$#@!dAsvS$TSDVFCW42r21123r"

x = re.findall("[a-zA-Z]", phrase)

lstStr = ''.join(str(ele) for ele in x)

for elem in x:
    str1 += elem

print(x)
print(lstStr)
print(str1)

y = re.findall("[0-9]", phrase)
print(y)