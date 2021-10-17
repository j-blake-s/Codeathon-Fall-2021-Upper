from collections import Counter

readFile = lambda f: list(filter(lambda x: x, map(str.strip, open(f,"r").readlines())))
actual = readFile("debugging/sample-blocks11.txt")
expected = readFile("cases/input/input11.txt")
expected = expected[1:int(expected[0])+1]

### Check that the schedule is correctly chosen from the available classes
leftovers = Counter(expected)
leftovers.subtract(actual)
least_common = next(reversed(leftovers.most_common()))
if least_common[1] >= 0:
    print("The schedule is correctly chosen from the available classes")
else:
    print("The course at", least_common[0], "is used", -least_common[1], "too many times")

### Check that the course does not have any overlap
alltimes = [t for block in actual for t in block.split()]
monotonic = all(t_0 <= t_1 for t_0, t_1 in zip(alltimes, alltimes[1:]))
if monotonic:
    print("The schedule is valid")
else:
    print("The schedule has an overlap")