column_1, row_1, column_2, row_2 = int(input()), int(input()), int(input()), int(input())
if column_1 - column_2 == row_1 - row_2 or column_2 - column_1 == row_1 - row_2 or column_1 - column_2 == row_2 - row_1 or column_2 - column_1 == row_2 - row_1:
    print("YES")
else:
    print("NO")