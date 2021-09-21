# Copyright 2021
# Justin Baum
# O(n log n) Solution
# Graham Scanning Algorithm
# Line Algorithm for Polygon Containment

def solution(point, points):
    print(point)
    print(points)
    return True


def main():
    k = int(input())
    for _ in range(k):
        n = int(input())
        (x, y) = map(float, input().split(" "))
        points = [list(map(float, input().split(" "))) for _ in range(n)]
        print("Yes" if solution((x, y), points) else "No")

if __name__ == "__main__":
    main()

