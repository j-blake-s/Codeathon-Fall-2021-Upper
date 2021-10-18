from collections import deque, defaultdict as dd
'''
This (inefficiently) solution explores the same spots over again

'''

def bfs(start_y, start_x, board):
    fringe = deque([(start_y, start_x)])
    if board[start_y][start_x] == "#":
        return False
    seen = set()
    y_dim = len(board)
    x_dim = len(board[0])
    def add_spot(new_y, new_x):
        pot = (new_y, new_x)
        if 0 <= new_y < y_dim and 0 <= new_x < x_dim and board[new_y][new_x] == '.' and pot not in seen:
            fringe.append((new_y, new_x))
            seen.add(pot)
    while fringe:
        y, x = fringe.popleft()
        if x == len(board[0]) - 1:
            return True
        for dy, dx in [(-1, 0), (1, 0), (0,1), (0, -1)]:
            add_spot(y + dy, x + dx)

    return False

def main():
    x_dim, y_dim = map(int, input().split())
    board1 = [input() for _ in range(y_dim)]
    input()
    
    board2 = [input() for _ in range(y_dim)]
    # print(board1)
    # print(board2)
    count = 0
    for y1 in range(y_dim):
        for x1 in range(x_dim):
            works1 = bfs(y1, x1, board1)
            works2 = bfs(y1, x1, board2)
            if works1 ^ works2:
                count += 1
    print(count)


if __name__ == '__main__':
    main()