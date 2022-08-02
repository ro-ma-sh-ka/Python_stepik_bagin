n = int(input())
mylist = []
for _ in range(n):
    s = input()
    if s not in mylist:
        mylist.append(s)
print(*mylist, sep='\n')