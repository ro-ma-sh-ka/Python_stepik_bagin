n = int(input())
mylist = []
for _ in range(n):
    mylist.append(input())

k = int(input())
searchlist = []
for _ in range(k):
    searchlist.append(input())

for txt in mylist:
    counter = 0
    for search in searchlist:
        if search.lower() in txt.lower():
            counter += 1
        if counter == k:
            print(txt)