#!/usr/bin/env python3

# Copyright 2021 Charles Daniels

# Brute force solution to ScheduleShowdown. Runs in O((A+B)^2). Will break for
# inputs where A or B are more than about 64 or so since it uses an int to
# store the bit vector for what schedule indices to include or not.
#
# for i in $(seq 0 10) ; do python3 generator.py --min 500 --max 20000 ./cases/input/input$i.txt ./cases/output/output$i.txt python3 ./solutions/solution.py  ; done

import sys

state = 0  # 0 - reading A, 1 - reading Alice's times, 2 - reading B, 3 - reading Bob's times

A = None
B = None
atimes = []
btimes = []

def fmtS(s):
    M = int((s / 60) % 60)
    H = int((s / 60) / 60)
    return "{:02d}:{:02d}".format(H, M)

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

def bvsubset(bv, lst):
    # Given a bit-vector bv, and a list lst, return a new list consisting of
    # only elements lst[i] where bv & (1 << i) is True.

    res = []
    for i in range(len(lst)):
        if (bv & (1 << i)) > 0:
            res.append(lst[i])
    return res

def checksched(s):
    # Given a schedule s of tuples (start, end) in seconds, return whether
    # or not the schedule is valid.

    for i in range(len(s)):
        for j in range(len(s)):
            if i == j:
                continue

            # There are 3 cases (note that every class will take a turn being i
            # and j, since we are doing this naively).
            #
            # Both classes occur at the same time
            # |--- i ---|
            # |--- j ---|
            #
            # i starts first, but ends after j starts
            # |--- i ---|
            #    |--- j ---|
            #
            # j starts and ends within the running time of j
            # |------ i ------|
            #    |--- j ---|
            #
            # These cases are OK:
            #
            # |--- i ---|
            #               |--- j ---|
            #
            #               |--- i ---|
            # |--- j ---|
            #
            # We can easily check if a class-pair conflicts by simply seeing if
            # either the start time or end time of j falls within the bounds of
            # i.

            # start time of i falls within j
            if (s[i][0] < s[j][1]) and (s[i][0] > s[j][0]):
                return False

            # end time of i falls within j
            if (s[i][1] < s[j][1]) and (s[i][1] > s[j][0]):
                return False

            # i and j are at exactly the same time
            if (s[i][0] == s[j][0]) and (s[i][1] == s[j][1]):
                return False

    return True

def sched2str(s):
    return ", ".join([fmtS(t[0]) + " " + fmtS(t[1]) for t in s])

amax = 0
bmax = 0

print("Alice: ")
for abv in range(pow(2, len(atimes))):
    asched = bvsubset(abv, atimes)
    if not checksched(asched):
        # print("reject: {}: {}".format(len(asched), sched2str(asched)))
        continue
    print("{}: {}".format(len(asched), sched2str(asched)))

    if len(asched) > amax:
        amax = len(asched)

print("Bob: ")
for bbv in range(pow(2, len(btimes))):
    bsched = bvsubset(bbv, btimes)
    if not checksched(bsched):
        # print("reject: {}: {}".format(len(asched), sched2str(asched)))
        continue
    print("{}: {}".format(len(bsched), sched2str(bsched)))

    if len(bsched) > bmax:
        bmax = len(bsched)

print("Alice: {}, Bob: {}".format(amax, bmax))
