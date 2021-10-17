#! /usr/bin/env python3

from argparse import ArgumentParser
from itertools import dropwhile
from operator import is_
from sys import stderr
import numpy as np

THRESHOLDS = [(0., 10), (0.2, 20), (0.2, 1<<12), (0.7, 1<<16), (1., 1<<20)]

def get_n(test, of_tests):
    v = test * 1./of_tests
    for threshold, value in THRESHOLDS:
        if threshold == v:
            return value
        if threshold > v:
            return int(lval + (v - lower) * (value - lval) / (threshold - lower))
        lower, lval = threshold, value
    return None

def comp(ri, rj):
    return ">" if ri > rj else "<" if ri < rj else "="

def select(*args):
    for a in args:
        if a is not None:
            return a
    return None

def main():
    argp = ArgumentParser()
    argp.add_argument("test", type=int)
    argp.add_argument("of_tests", type=int)
    argp.add_argument("--debug", action="store_true")
    argp.add_argument("--seed", type=int)
    args = argp.parse_args()

    debug = lambda *a, **kw: print(*a, **kw, file=stderr) if args.debug else None

    np.random.seed(select(args.seed, args.test))
    np.set_printoptions(threshold=20)

    n = get_n(args.test, args.of_tests)
    assert n != 1, "Cannot produce a derangement with one element"

    debug("..n =", n)
    debug("..generating rankings")
    ranking = np.random.permutation(n)     # Index of card in the absolute ranking
    debug(" ", np.argsort(ranking)+1)
    debug("..generating hand order")
    hand_order = np.random.permutation(n)  # Order of first in pair
    debug("..generating hand pairings")
    i = 1
    pairs = np.random.permutation(n)       # Which card is played against this card (must be a derangement)

    debug("..printing pairings")
    print(n)
    for i in hand_order:
        j = pairs[i]
        print("{} {} {}".format(i+1, comp(ranking[i], ranking[j]),  j+1))

if __name__ == "__main__":
    main()
