s = input()
first_h = s.find('h')
last_h = s.rfind('h')
s = s[:first_h + 1] + s[last_h - 1: first_h:-1] + s[last_h:]
print(s)