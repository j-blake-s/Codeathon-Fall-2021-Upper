#!/usr/bin/python3
# Copyright 2021
# Justin Baum
# O(n log n) Solution
# Graham Scanning Algorithm

from math import atan2, pi

def convex_hull(points):
    def polar_angle(p, o):
        return atan2((p[1] - o[1]), (p[0] - o[0]))

    def polar_distance(p, o):
        return (p[0] - o[0]) ** 2 + (p[1] - o[1]) ** 2

    # Determine if r is collinear or counterclockwise/clockwise
    # Any positive value is counterclockwise
    def turn(p, q, r):
        return (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1])

    # O(n log n)
    p = min(points, key=lambda pair: (pair[0], pair[1]))
    points.remove(p)
    # Sort by polar angle, then keep furthest
    points = sorted(
        points, key=lambda point: (polar_angle(point, p), -polar_distance(point, p))
    )
    stack = [p]
    # O(n)
    for point in points:
        while len(stack) > 1 and turn(stack[-2], stack[-1], point) <= 0:
            stack.pop()
        stack.append(point)
    return stack

def area(points):
    shoelace = zip(points, points[1:] + points[:1])
    return sum(map(lambda x: x[0][0] * x[1][1] - x[1][0] * x[0][1], shoelace)) * 0.5

def solution(points):
    return area(convex_hull(points))

def main():
    n = int(input())
    points = [list(map(float, input().split(" "))) for _ in range(n)]
    print(solution(points))

if __name__ == "__main__":
    main()
