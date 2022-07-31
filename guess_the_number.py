from random import *

def answer(num):
    if n_user == n_pass:
        return 'You are right, congrats!'
    elif n_user > n_pass:
        return 'Too big, lets try again'
    else:
        return 'Too small, lets try again'

n_pass = randrange(1, 101)
n_user = 0
counter = 1

while n_user != n_pass:
    n_user = int(input(f'Attempt {counter}. Please, input your choice: '))
    counter += 1
    print(answer(n_user))