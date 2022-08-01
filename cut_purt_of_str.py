s = input()
first_h = s.find('h')
last_h = s.rfind('h')
s = s[:first_h] + s[last_h + 1:]
print(s)