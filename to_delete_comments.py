s = input()
for _ in range(int(s[1:])):
    txt = input()
    if txt.find('#') > -1:
        txt = txt[:txt.find('#')]
    print(txt.rstrip())