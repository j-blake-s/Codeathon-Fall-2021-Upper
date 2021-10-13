#!/usr/bin/env python3

# Copyright 2021 Charles Daniels

# Test case generator for Schedule Showdown.

import argparse
import subprocess
import random
import pathlib

parser = argparse.ArgumentParser()

parser.add_argument("input", type=pathlib.Path, help="Path to write generated input to.")

parser.add_argument("output", type=pathlib.Path, help="Path to write generated output to.")

parser.add_argument("solution_command", nargs="+", help="An implementation of the solution, which is used to generate expected correct outputs.")

parser.add_argument("--min", "-m", type=int, default=10, help="Minimum number of classes for either schedule.")

parser.add_argument("--max", "-M", type=int, default=20, help="Maximum number of classes for either schedule.")

args = parser.parse_args()

assert args.min < args.max

A = random.randrange(args.min, args.max)
B = random.randrange(args.min, args.max)

s = ""

def fmtS(s):
    M = int((s / 60) % 60)
    H = int((s / 60) / 60)
    return "{:02d}:{:02d}".format(H, M)

s += "{}\n".format(A)
for i in range(A):
    start = random.randrange(0, 24*60*60-60)
    end = random.randrange(start+1, 24*60*60-10)
    s += "{} {}\n".format(fmtS(start), fmtS(end))

s += "{}\n".format(B)
for i in range(B):
    start = random.randrange(0, 24*60*60-60)
    end = random.randrange(start+1, 24*60*60-10)
    s += "{} {}\n".format(fmtS(start), fmtS(end))

with open(args.input, "w") as f:
    f.write(s)

with open(args.output, "w") as f:
    subprocess.run(args.solution_command, stdout=f, input=s, encoding="utf8", check=True)
