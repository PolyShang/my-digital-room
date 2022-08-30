roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
s = 'MMV'
num = int(0)

i = 0
while i < len(s):
    if s[i] == 'M' or s[i] == 'D':
        num += roman_dict[s[i]]
        i += 1
    elif s[i] == 'C':
        if i + 1 < len(s):
            if s[i + 1] in ['M', 'D']:
                num -= 100
                i += 1
            else:
                num += 100
                i += 1
        else:
            num += 100
            i += 1
    elif s[i] == 'L':
        num += 50
        i += 1
    elif s[i] == 'X':
        if i + 1 < len(s):
            if s[i + 1] in ['L', 'C']:
                num -= 10
                i += 1
            else:
                num += 10
                i += 1
        else:
            num += 10
            i += 1
    elif s[i] == 'V':
        num += 5
        i += 1
    elif s[i] == 'I':
        if i + 1 < len(s):
            if s[i + 1] in ['V', 'X']:
                num -= 1
                i += 1
            else:
                num += 1
                i += 1
        else:
            num += 1
            i += 1

print(num)