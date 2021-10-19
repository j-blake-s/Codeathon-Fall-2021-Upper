n, m, k = map(int, input().split())
formulas = [input() for i in range(k)]

tailgates = [(tuple(map(int, input().split())), i) for i in range(n)]
pos = 0
seen = {}
positions = {}
for x in formulas:
    formula, step = x.split()
    formula = formula.split("+")
    step = int(step)
    letters = tuple(sorted(formula))
    id_ = tailgates[pos][1]
    if letters in seen:
        tailgates = seen[letters]
    else:
        tailgates = sorted(tailgates, key=lambda y: (sum(y[0][ord(j)-ord('a')] for j in formula), y[1]))
        seen[letters] = tailgates
        positions[letters] = {tail[1] : i for i, tail in enumerate(tailgates)}
    pos = positions[letters][id_]
    pos += step
    pos %= len(tailgates)

print(tailgates[pos][1])