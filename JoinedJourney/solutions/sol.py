from collections import deque

x_dim, y_dim = map(int, input().split())
board1 = [input() for _ in range(y_dim)]
input()

board2 = [input() for _ in range(y_dim)]

leads_to_exit1 = set()
leads_to_exit2 = set()


adj = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def search_from_right(board, y, x, seen):
    #start_y, start_x
    if board[y][x] == "#":
        return
    seen.add((y, x))
    fringe = deque([(y, x)])
    while len(fringe) > 0:
        cur_y, cur_x = fringe.popleft()
        for dy, dx in adj:
            if not(0 <= cur_y + dy < len(board) and 0 <= cur_x + dx < len(board[0])):
                continue
            next_spot = (cur_y + dy, cur_x + dx)
            if next_spot in seen or board[next_spot[0]][next_spot[1]] == "#":
                continue
            seen.add(next_spot)
            fringe.append(next_spot)

for y in range(y_dim):
    search_from_right(board1, y, x_dim-1, leads_to_exit1)
# print(leads_to_exit1)
# print("---")
for y in range(y_dim):
    search_from_right(board2, y, x_dim-1, leads_to_exit2)
# print(leads_to_exit2)
# points = (sorted(leads_to_exit1 ^ leads_to_exit2))
# for p in points:
#     print(*p)
print(len(leads_to_exit1 ^ leads_to_exit2))
