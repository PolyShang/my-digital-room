roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
I, V, X, L, C, D, M = 1, 5, 10, 50, 100, 500, 1000
s = input('Please input your number in Roman format: ')

ans = s.count('M') * M + s.count('D') * D + s.count('C') * C + s.count('L') * L + \
      s.count('X') * X + s.count('V') * V + s.count('I') * I - 2 * (s.count('IV') * I + s.count('IX') * I +
      s.count('XL') * X + s.count('XC') * X + s.count('CD') * C + s.count('CM') * C)

print(ans)