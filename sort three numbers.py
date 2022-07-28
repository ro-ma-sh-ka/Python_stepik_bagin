num1, num2, num3 = int(input()), int(input()), int(input())
print(max(num1, num2, num3), num1 + num2 + num3 - max(num1, num2, num3) - min(num1, num2, num3), min(num1, num2, num3), sep='\n')