from itertools import accumulate, chain, dropwhile, repeat,  takewhile

def solve(n, it_pairs):
    comparisons = [[None, None] for _ in range(n)]  # Stores the two compared nodes for each node and whether this node beats it
    
    for i, j, comp in it_pairs:
        i_comp = (j, comp)
        j_comp = (i, not comp)
        comparisons[i][0 if comparisons[i][0] is None else 1] = i_comp
        comparisons[j][0 if comparisons[j][0] is None else 1] = j_comp
    # If the input is well-constructed, every cell should be populated
    # We can represent it this way because each node is in exactly two comparisons -> hence the graph is composed of cycles

    counts = [0] * n
    unexplored = set(range(n))
    while unexplored:
        unexplored -= explore_cycle(unexplored.pop(), comparisons, counts)  # Populates counts
    
    max_count = max(counts)
    max_nodes = list(filter(lambda i: counts[i] == max_count, range(n)))
    return max_nodes

def explore_cycle(start, comparisons, counts):
    is_max = lambda i: comparisons[i][0][1] and comparisons[i][1][1]       # Dominates both neighbors
    is_min = lambda i: not (comparisons[i][0][1] or comparisons[i][1][1])  # Both neighbors dominate this node
    next_i = lambda i, prev: (comparisons[i][0][0] if comparisons[i][0][0] != prev else comparisons[i][1][0], i)  # Get the neighbor that is not prev

    explored = set()

    count = 0
    cur_max = None

    first_min = None
    cycle = accumulate(repeat(None), lambda p, _: next_i(*p), initial=(start, None))  # Apply next_i to get infinite iterator
    cycle = dropwhile(lambda p: not is_min(p[0]), cycle)  # Move around to first min element
    first_min = next(cycle)[0]  # Get first element and remove it from the iterator
    cycle = transform_first(cycle, lambda p: (p[0], None))  # Make prev null on first iteration so we can filter prev != first_min
    cycle = takewhile(lambda p: p[1] != first_min, cycle)  # Take items until we return to start

    found_cycle = False

    for i, _ in cycle:
        explored.add(i)
        count += 1
        if is_min(i):
            # Reset count and cur_max, storing the current value in counts
            assert cur_max is not None
            
            if i == first_min and not found_cycle:
                count -= 1  # If there is only one cycle, decrease the count since the endpoint is the same
            found_cycle = True

            counts[cur_max] = count

            count = 0
            cur_max = None
        elif is_max(i):
            # Store current max for the end of the segment
            assert cur_max is None
            cur_max = i

    return explored

def transform_first(it, transform):
    first = transform(next(it))
    return chain([first], it)


def main():
    n = int(input())
    it_pairs = ((int(i)-1, int(j)-1, comp == ">") for i, comp, j in (input().split() for _ in range(n)))
    for line in sorted(solve(n, it_pairs)):
        print(line+1)

if __name__ == "__main__":
    main()
