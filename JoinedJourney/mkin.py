#!/usr/local/bin/python3
# from random import randint
import random
case_num = int(input())

# def gen_maze(x_dim, y_dim):


# 0 and 1 are the sample cases
mazes0 = '''##..
#.##
#...

##..
..#.
#.##'''

mazes1 = '''#..#.
####.
.....

.....
#####
..###'''
if case_num == 0:
    print(4, 3)
    print(mazes0)
elif case_num == 1:
    print(5, 3)
    print(mazes1)
else:
    # output what should be read in as input by
    # contestant code
    y = random.randint(3, 10 * case_num)
    x = random.randint(3, 10 * case_num)
    print(x, y)
    for _ in range(y):
        print("".join(random.choices(["#", "."], [.4, case_num/10], k=x)))
    print()
    for _ in range(y):
        print("".join(random.choices(["#", "."], [5, case_num/2], k=x)))

