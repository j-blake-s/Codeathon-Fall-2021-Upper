#!/usr/local/bin/python3
# from random import randint
import random
case_num = int(input())



if case_num == 0:
    n_bounds = (2, 4)
    s_bounds = (2, 5)
    t = 2
elif case_num == 1:
    n_bounds = (3, 5)
    t = 3
    s_bounds = (3, 6)
else:
    n_bounds = (2, 100)
    s_bounds = (1, 10 ** 8)
    t = random.randint(2, 20)

print(t)
for _ in range(t):
    n = (random.randint(*n_bounds))
    print(n)
    for _ in range(n):
        ins_type = random.randint(0, 2)
        if ins_type == 0:
            print(random.choice("NSEW"), random.randint(*s_bounds))
        elif ins_type == 1:
            print(random.choice(["CW", "CCW"]), random.randint(1, 4) * 90)
        elif ins_type == 2:
            print(random.choice(["F", "B"]), random.randint(*s_bounds))


    
