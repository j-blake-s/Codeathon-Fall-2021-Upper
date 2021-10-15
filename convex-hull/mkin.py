#!/usr/bin/python3
import random

R = 50000
n = int(input())

random.seed(n)

points = [(random.uniform(-R, R), random.uniform(-R,R)) for _ in range(n)]

print(n)
for point in points:
    print("{} {}".format(*point))
