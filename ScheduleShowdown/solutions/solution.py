#!/usr/bin/env python3

# Copyright 2021 Charles Daniels

# Optimal solution to ScheduleShowdown. Runs in O(n log(n)) assuming n = A+B.
# This solution is based on Algorithms, by Jeff Erickson §4.2.
#
# http://jeffe.cs.illinois.edu/teaching/algorithms/

import sys

state = 0  # 0 - reading A, 1 - reading Alice's times, 2 - reading B, 3 - reading Bob's times

A = None
B = None
atimes = []
btimes = []

# We use a simple state machine to read in the input one line at a time.
for line in sys.stdin:
    if state == 0:
        A = int(line)
        state = 1

    elif state == 2:
        B = int(line)
        state = 3

    elif state in [1,3]:
        start, end = line.strip().split()
        startH, startM = [int(x) for x in start.split(":")]
        endH, endM = [int(x) for x in end.split(":")]
        startS = startH * 60 * 60 + startM * 60
        endS = endH * 60 * 60 + endM * 60

        if state == 1:
            atimes.append((startS, endS))
        elif state == 3:
            btimes.append((startS, endS))

        if (state == 1) and (len(atimes) >= A):
            state = 2

def GreedySchedule(s):
    # Note that s contains (start, end) tuples, which makes it easier to "sort
    # F and permute S to match". We could imagine S = [t[0] for t in s] and F =
    # [t[1] for t in s].
    s = sorted(s, key=lambda pair: pair[1])  # sort by end time
    count = 0
    X = [0]
    # Mind the translation from 1 indexing to 0 indexing.
    for i in range(1, len(s)):
        if s[i][0] >= s[X[count]][1]:
            count += 1
            X.append(i)
    return X

asched = GreedySchedule(atimes)
bsched = GreedySchedule(btimes)

if len(asched) > len(bsched):
    print("Alice")
    print(len(asched))

elif len(bsched) > len(asched):
    print("Bob")
    print(len(bsched))

else:
    print("Tie")
    print(len(bsched))


