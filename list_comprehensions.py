print(*[word for word in input().split()], sep='\n')

print(*[i for i in input() if i.isdigit()], sep='')

print(*[int(num) ** 2 for num in input().split() if (int(num) ** 2) % 10 != 4 and int(num) % 2 == 0], sep=' ')

l = [int(i) for i in input().split()]
m = [int(i) for i in input().split()]
print(*[l[i] + m[i] for i in range(len(l))], sep=' ')

list_n = [int(i) for i in input().split()]
print(*list_n, sep='+', end=f'={sum(list_n)}')

print(max([len(i) for i in input().split()]))

print(*[i[1:] + i[0] + 'ки' for i in input().split()])