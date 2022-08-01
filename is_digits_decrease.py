n = int(input())
flag = "YES"
while n != 0:
    last_digit = n % 10
    n //= 10
    if last_digit > n % 10 and n > 0:
        flag = "NO"
print(flag)