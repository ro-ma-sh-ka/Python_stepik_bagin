n, k = 7, 5

n_list = [i for i in range(1, n + 1)]
print(n_list)
gap = 0
while len(n_list) > 1:
    killer_list = [n_list[i] for i in range(1 + gap, len(n_list), k)]
    print(killer_list)

    for kill in killer_list:
        n_list.remove(kill)
    print(n_list)
    # gap = 