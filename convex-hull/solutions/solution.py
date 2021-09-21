# Copyright 2021
# Justin Baum
# O(n log n) Solution
# Graham Scanning Algorithm

from functools import reduce

def convex_hull(points):
    # Determine if r is collinear or counterclockwise/clockwise
    # Any positive value is counterclockwise
    def turn(p, q, r):
        return (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1])

    # O(n log n)
    points = sorted(points, key=lambda x: (x[1], x[0]))
    stack = []
    # O(n)
    for point in points:
        while len(stack) > 1 and turn(stack[-2], stack[-1], point) > 0:
            stack.pop()
        stack.append(point)
    return stack

def area(points):
    shoelace = zip(points, points[1:] + points[:1])
    return sum(map(
            lambda x:
            x[0][0]*x[1][1] -
            x[1][0]*x[0][1],
            shoelace))/2.0
def solution(points):
    return area(convex_hull(points))


def main():
    n = int(input())
    points = [list(map(float, input().split(" "))) for _ in range(n)]
    print(solution(points))

if __name__ == "__main__":
    main()

